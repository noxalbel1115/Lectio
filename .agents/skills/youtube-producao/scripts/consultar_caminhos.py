"""Consulta compacta ao inventário antigo sem carregar 405 caminhos no contexto."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('termos', nargs='*', help='Todos os termos devem ocorrer no caminho.')
    parser.add_argument('--root', type=Path, help='Raiz da cópia do projeto no runtime atual.')
    parser.add_argument('--limit', type=int, default=12)
    parser.add_argument('--offset', type=int, default=0)
    args = parser.parse_args()
    if args.limit < 1 or args.offset < 0:
        parser.error('limit deve ser positivo e offset não negativo')
    index = Path(__file__).resolve().parents[1] / 'references/caminhos-do-projeto.json'
    data = json.loads(index.read_text(encoding='utf-8'))
    if not args.termos:
        print(json.dumps({k: data[k] for k in ('date', 'original_root', 'file_count', 'total_bytes', 'key_paths')}, ensure_ascii=False, indent=2))
        return
    terms = [term.casefold() for term in args.termos]
    matches = [item for item in data['files'] if all(term in item['relative_path'].casefold() for term in terms)]
    selected = []
    for item in matches[args.offset:args.offset + args.limit]:
        row = dict(item)
        if args.root:
            candidate = args.root.expanduser().resolve() / item['relative_path']
            row.update(mapped_path=str(candidate), exists_here=candidate.is_file())
        selected.append(row)
    print(json.dumps({'matches': len(matches), 'offset': args.offset, 'items': selected}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

"""Resume um vídeo com ffprobe, amostras opcionais e teste de decodificação."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--decode', action='store_true')
    parser.add_argument('--amostras', type=Path)
    parser.add_argument('--saida', type=Path)
    args = parser.parse_args()
    video = args.video.expanduser().resolve()
    if not video.is_file():
        parser.error(f'Arquivo não encontrado: {video}')
    for binary in ['ffprobe'] + (['ffmpeg'] if args.decode or args.amostras else []):
        if not shutil.which(binary):
            parser.error(f'Executável ausente: {binary}')
    if args.saida and args.saida.expanduser().resolve() == video:
        parser.error('O relatório não pode sobrescrever o vídeo')
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                            'format=duration,size:stream=codec_type,codec_name,width,height,avg_frame_rate,duration,sample_rate,channels',
                            '-of', 'json', str(video)], capture_output=True, text=True)
    if probe.returncode:
        parser.exit(1, 'ffprobe falhou: ' + probe.stderr[-1500:] + '\n')
    metadata = json.loads(probe.stdout)
    streams = metadata.get('streams', [])
    if not any(stream.get('codec_type') == 'video' for stream in streams):
        parser.exit(1, 'O arquivo não contém faixa de vídeo\n')
    duration = float(metadata.get('format', {}).get('duration', 0))
    result = {'file': str(video), 'duration_seconds': duration,
              'bytes': video.stat().st_size, 'streams': streams,
              'decode_tested': args.decode, 'samples': [], 'errors': [],
              'visual_review': 'não realizada pelo script',
              'audio_listening': 'não realizada pelo script'}
    if args.decode:
        decoded = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-xerror', '-i', str(video),
                                  '-map', '0:v:0', '-map', '0:a?', '-f', 'null', '-'],
                                 capture_output=True, text=True)
        result['decode_ok'] = decoded.returncode == 0
        if decoded.returncode:
            result['errors'].append({'stage': 'decode', 'detail': decoded.stderr[-1500:]})
    if args.amostras:
        if duration <= 0:
            result['errors'].append({'stage': 'samples', 'detail': 'Duração indisponível'})
        else:
            folder = args.amostras.expanduser().resolve()
            folder.mkdir(parents=True, exist_ok=True)
            for fraction in (0.1, 0.5, 0.9):
                position = duration * fraction
                target = folder / f'{video.stem}-{round(fraction * 100):02d}.jpg'
                if target.exists():
                    result['errors'].append({'stage': 'samples', 'detail': f'Amostra já existe: {target}'})
                    continue
                extracted = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-n', '-ss', str(position),
                                            '-i', str(video), '-frames:v', '1', '-vf', 'scale=640:-2', str(target)],
                                           capture_output=True, text=True)
                if extracted.returncode or not target.is_file():
                    result['errors'].append({'stage': 'samples', 'detail': extracted.stderr[-1500:] or 'Nenhum quadro produzido'})
                else:
                    result['samples'].append({'seconds': position, 'file': str(target)})
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.saida:
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        args.saida.write_text(text, encoding='utf-8')
    print(text, end='')
    return bool(result['errors'])


if __name__ == '__main__':
    raise SystemExit(main())

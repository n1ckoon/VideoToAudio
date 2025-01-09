from moviepy.editor import VideoFileClip
from pathlib import Path

video_file = Path('sample_files/my_video.mp4')

# Открываем видеофайл
video = VideoFileClip(str(video_file))

# Извлекаем аудио из видео
audio = video.audio

# Сохраняем аудио в mp3
audio.write_audiofile(f'{video_file.stem}.mp3')

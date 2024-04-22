from pytube import YouTube
import os
import subprocess

def download_video(url, output_path):
    yt = YouTube(url)

    # Скачиваем аудио и видео отдельно
    video_stream = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(only_audio=True).first()

    video_filename = video_stream.download(output_path, filename_prefix='video_')
    audio_filename = audio_stream.download(output_path, filename_prefix='audio_')

    # Объединяем аудио и видео с помощью FFmpeg
    output_filename = os.path.join(output_path, f"{yt.title}.mp4")
    subprocess.run(['ffmpeg', '-i', video_filename, '-i', audio_filename, '-c', 'copy', output_filename])

    # Удаляем временные файлы
    os.remove(video_filename)
    os.remove(audio_filename)

# Пример использования функции
download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "/path/to/download/directory")
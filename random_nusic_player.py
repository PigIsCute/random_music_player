import os
import random
import pygame

def get_ramdom_playlist(music_folder):
    playlist = [f for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]
    random.shuffle(playlist)
    return playlist

music_folder  = input("歌單位置：")
if not music_folder:
    print("❌ 請提供有效的歌單位置。")
    exit(1)
music_folder  = music_folder.replace("\\", "/")

# 取得所有 mp3 或 wav 檔案
playlist = get_ramdom_playlist(music_folder)

# 初始化 pygame 音樂模組
pygame.mixer.init()

if not playlist:
    print("❌ 沒有找到音樂檔案。")
else:
    while True:
        # 播放音樂
        music = playlist.pop(0)  
        full_path = os.path.join(music_folder, music)
        print(f"▶️ 正在播放：{music}")
        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play()

        # 等待音樂播放結束
        while pygame.mixer.music.get_busy():
            continue
        
        if playlist == []:
            playlist = get_ramdom_playlist(music_folder)
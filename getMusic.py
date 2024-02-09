import os

def Get_Music():
    music = []
    for root, dirs, files in os.walk('music/'):
        for file in files:
            if file.endswith('.mp3'):
                music.append(file[:-4])  # Remove the '.mp3' from the filename
    print(music)
    return music








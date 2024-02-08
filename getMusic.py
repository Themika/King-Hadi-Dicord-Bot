import os

def Get_Music():
    music = []
    for root, dirs, files in os.walk('music/'):
        for file in files:
            if file.endswith('.mp3'):
                x  = file.split('.mp3')
                music.append(x)
                print(music)
    return music








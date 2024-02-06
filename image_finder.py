import random
hadi_photos = ["Photos\Photo 2023-01-19, 11 59 58 AM.png", 
               "Photos\Photo 2023-01-19, 12 00 04 PM.png",
               "Photos\Photo 2023-01-20, 3 28 14 PM.png",
               "Photos\Hadi_Attack.png",
               "Photos\Hadi_Banana.png",
               "Photos\Hadi_Chad.png",
               "Photos\Hadi_GIGACHAD.png",
               "Photos\Hadi_Hyper_Giga_Chad.png",
               "Photos\Hadi_Red_Sweater.png",
               "Photos\Hadi_Stare.png",
               "Photos\Hadi_Laying_Down.png",
               "Photos\Hadi_HADI.png",
               ]

def getHadi():
    y = random.randint(0, len(hadi_photos) -1)
    print(hadi_photos[y])
    return hadi_photos[y]


import pgzrun
import random

# Oyun penceresi
WIDTH = 6
HEIGHT = 650
TITLE = "Glitchcore" # Oyun penceresinin başlığı
FPS = 30 # Saniyedeki Kare Sayısı


# Nesneler
bg = Actor('background')
shineta = Actor('shineta')
tetris = Actor('tetris')
bonus_1= Actor('glitchkristali1')
bonus_2= Actor('glitchkristali2')
muz = Actor('muz')
glitchcore = Actor('glitchcore')
win = Actor('win')


# Değişkenler
users_health = 100
gcs_health = 500
users_damage = 10
gcs_damage = 50
users_glitchpoint = 0 #bunun sayesinde glitchcore'un sağlığını azaltacağız
gcs_glitchpoint = 0 #glitchcore's glitch point bunun sayesinde atak geçirip bizim sağlığımızı azaltacak)




#bonuslar


# Glitch puanı
def for_bonus_1():
    users_health += 10
    users_glitchpoint +=2
 
    
def for_bonus_2():
    users_health += 2
    users_glitchpoint +=10



  
  


def draw():
    bg.draw()
    shineta.draw()
    glitchcore.draw()
    
# Tıklamaları işleme
def on_mouse_down(button, pos):
    global users_damage,users_glitchpoint,gcs_glitchpoint,gcs_health,users_health,gcs_damage
    #Oyundaki tıklamalar
    if button == mouse.LEFT:
        # Nesneye tıklama
        if tetris.collidepoint(pos) or duck.collidepoint(pos) or muz.collidepoint(pos):
            damage += 3
            health -= 5


pgzrun.go()
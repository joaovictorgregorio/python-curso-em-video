import pygame
import os

def clear_console():
    os.system('cls')

clear_console()

pygame.init()
pygame.mixer.music.load('crash.mp3')
pygame.mixer.music.play()
pygame.event.wait()


import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SoundManager:
    def __init__(self):
        self.jump = pygame.mixer.Sound(os.path.join(BASE_DIR, "sfx", "jump.mp3"))
        self.jump.set_volume(0.2)

    def play_jump(self):
        self.jump.play()
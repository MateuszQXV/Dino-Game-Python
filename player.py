import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Player:
    def __init__(self, ground_y):
        self.run1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "Dino1.png"))
        self.run2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "Dino2.png"))
        self.jump_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "DinoJumping.png"))
        self.duck1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "DinoDucking1.png"))
        self.duck2 = pygame.image.load(os.path.join(BASE_DIR, "assets", "DinoDucking2.png"))

        self.x = 160
        self.y = ground_y

        self.ground_y = ground_y

        self.vel_y = 0
        self.gravity = 0.5
        self.jump_power = -12

        self.ducking = False

        self.width = self.run1.get_width()
        self.height = self.run1.get_height()

    def get_hitbox(self):
        if self.ducking:
            return pygame.Rect(self.x, self.y + 15, self.width, self.height - 20)
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        if self.y >= self.ground_y:
            self.vel_y = self.jump_power

    def update(self):
        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vel_y = 0

    def run(self, screen):
        self.ducking = False
        img = self.run1 if (pygame.time.get_ticks() // 200) % 2 == 0 else self.run2
        screen.blit(img, (self.x, self.y))

    def duck(self, screen):
        self.ducking = True
        img = self.duck1 if (pygame.time.get_ticks() // 200) % 2 == 0 else self.duck2
        screen.blit(img, (self.x, self.y + 12))
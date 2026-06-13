import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Mapa:
    def __init__(self):
        self.GROUND_Y = 400
        self.CACTUS_Y = 390
        self.BIRD_Y = 330

        self.ground_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "ground.png"))
        self.cloud_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "cloud.png"))

        self.gx1 = 0
        self.gx2 = self.ground_img.get_width()

        self.clouds = [[150,110],[320,140],[500,90]]

        self.distance = 0
        self.speed = 5
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def update(self):
        self.distance += 1
        self.speed = min(14, 5 + self.distance // 350)

        self.gx1 -= self.speed
        self.gx2 -= self.speed

        if self.gx1 <= -self.ground_img.get_width():
            self.gx1 = self.gx2 + self.ground_img.get_width()

        if self.gx2 <= -self.ground_img.get_width():
            self.gx2 = self.gx1 + self.ground_img.get_width()

        for c in self.clouds:
            c[0] -= 2
            if c[0] < -50:
                c[0] = 700
        self.distance += 1
        self.score = self.distance // 40
    def draw(self, screen):
        screen.blit(self.ground_img, (self.gx1, 435))
        screen.blit(self.ground_img, (self.gx2, 435))
        text = self.font.render(f"Score: {self.score}", True, "white")
        screen.blit(text, (10, 30))
        screen.blit(self.ground_img, (self.gx1, 435))
        screen.blit(self.ground_img, (self.gx2, 435))

        for c in self.clouds:
            screen.blit(self.cloud_img, c)
        
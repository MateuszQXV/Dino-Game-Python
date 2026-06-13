import pygame

class Cactus:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, speed):
        self.x -= speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
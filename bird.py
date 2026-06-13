import pygame

class Bird:
    def __init__(self, images, x, y):
        self.images = images
        self.index = 0
        self.image = images[0]

        self.x = x
        self.y = y

        self.rect = self.image.get_rect(topleft=(x, y))

        self.anim = 0

    def update(self, speed):
        self.x -= speed
        self.rect.x = self.x

        self.anim += 1
        if self.anim > 8:
            self.anim = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
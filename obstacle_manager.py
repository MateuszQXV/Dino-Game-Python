import pygame
import random
import os
from cactus import Cactus
from bird import Bird

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ObstacleManager:
    def __init__(self, mapp):
        self.mapp = mapp

        self.cactus_images = [
            pygame.image.load(os.path.join(BASE_DIR, "cacti", "cactus1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "cacti", "cactus2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "cacti", "cactus3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "cacti", "cactus4.png")),
            pygame.image.load(os.path.join(BASE_DIR, "cacti", "cactus5.png")),
            pygame.image.load(os.path.join(BASE_DIR, "cacti", "cactus6.png")),
        ]

        self.bird_images = [
            pygame.image.load(os.path.join(BASE_DIR, "assets", "Ptero1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "assets", "Ptero2.png")),
        ]

        self.obstacles = []
        self.timer = 0

    def spawn(self):
        if random.random() < 0.25:
            self.obstacles.append(
                Bird(self.bird_images, 750, self.mapp.BIRD_Y)
            )
        else:
            img = random.choice(self.cactus_images)
            self.obstacles.append(
                Cactus(img, 750, self.mapp.CACTUS_Y)
            )

    def update(self, speed):
        self.timer += 1

        if self.timer > 70:
            self.spawn()
            self.timer = 0

        for o in self.obstacles:
            o.update(speed)

        self.obstacles = [o for o in self.obstacles if o.x > -200]

    def draw(self, screen):
        for o in self.obstacles:
            o.draw(screen)

    def check_collision(self, player_hitbox):
        for o in self.obstacles:
            if player_hitbox.colliderect(o.rect):
                return True
        return False
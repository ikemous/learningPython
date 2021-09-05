import pygame
from pygame.sprite import Sprite;
from random import randint;

IMAGE_SIZE = 60;

class Enemy(Sprite):

    def __init__(self, app):
        super().__init__();

        self.screen = app.screen;
        self.screenRect = app.screen.get_rect();
        self.settings = app.settings;
        stage = app.stats.stage;
        enemyNumber = randint(0, len(self.settings.enemyGroups[stage]) - 1);
        enemySettings = self.settings.enemyGroups[stage][enemyNumber];
        self.points = enemySettings["points"];
        self.health = enemySettings["health"];
        self.speed = enemySettings["speed"];
        imagePath = enemySettings["imagePath"];
        self.image = pygame.image.load(imagePath);
        direction = randint(1,4);
        self.direction = 4;
        self.rect = self.image.get_rect();
        
        if direction == 1:
            self.direction = 'N';
            self.rect.x = randint(0, self.screenRect.right);
            self.rect.y = self.screenRect.bottom - IMAGE_SIZE;
        elif direction == 2:
            self.direction = 'E';
            self.rect.x = 0;
            self.rect.y = randint(0, self.screenRect.bottom);
        elif direction == 3:
            self.direction = 'S';
            self.rect.x = randint(0, self.screenRect.right);
            self.rect.y = 0;
        elif direction == 4:
            self.direction = 'W';
            self.rect.x = self.screenRect.right - IMAGE_SIZE;
            self.rect.y = randint(0, self.screenRect.bottom);

        self.x = float(self.rect.x);
        self.y = float(self.rect.y);
        
    def update(self):
        if self.direction == 'N':
            self.y -= self.speed;
        if self.direction == 'E':
            self.x += self.speed;
        if self.direction == 'S':
            self.y += self.speed;
        if self.direction == 'W':
            self.x -= self.speed;

        self.rect.x = self.x;
        self.rect.y = self.y;
        
    def blitme(self):
        self.screen.blit(self.image, self.rect);
import pygame
from pygame.sprite import Sprite;
from random import randint;

class Enemy(Sprite):

    def __init__(self, app):
        super().__init__();
        self.screen = app.screen;
        self.settings = app.settings;
        self.direction = 'E';
        self.startx = 0;
        self.starty = 0;
        imageNumber = randint(1, 6);
        self.image = pygame.image.load(self.settings.enemyImages[imageNumber])
        self.rect = self.image.get_rect();
        self.x = float(self.rect.x);
        self.y = float(self.rect.y);
        direction = randint(1,4);
        if direction == 1:
            self.direction = 'N';
        elif direction == 2:
            self.direction = 'E';
        elif direction == 3:
            self.direction = 'S';
        elif direction == 4:
            self.direction == 'W';
        
    def update(self):
        if self.direction == 'N':
            self.y -= self.settings.enemySpeed;
        if self.direction == 'E':
            self.x += self.settings.enemySpeed;
        if self.direction == 'S':
            self.y += self.settings.enemySpeed;
        if self.direction == 'W':
            self.x -= self.settings.enemySpeed;

        self.rect.x = self.x;
        self.rect.y = self.y;
    
    def blitme(self):
        self.screen.blit(self.image, self.rect);
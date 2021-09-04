import pygame
from pygame.sprite import Sprite;
from random import randint;

IMAGE_SIZE = 60;

class Enemy(Sprite):

    def __init__(self, app):
        super().__init__();

        # direction = 1;

        self.screen = app.screen;
        self.screenRect = app.screen.get_rect();
        self.settings = app.settings;
        
        imageNumber = randint(0, len(self.settings.enemyImages) - 1);
        direction = randint(1,4);

        self.direction = 4;
        self.image = pygame.image.load(self.settings.enemyImages[imageNumber])
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
            self.y -= self.settings.enemySpeed;
        if self.direction == 'E':
            self.x += self.settings.enemySpeed;
        if self.direction == 'S':
            self.y += self.settings.enemySpeed;
        if self.direction == 'W':
            self.x -= self.settings.enemySpeed;

        self.rect.x = self.x;
        self.rect.y = self.y;
    
    def collided(self, otherRect):
        return self.rect.colliderect(otherRect);
        
    def blitme(self):
        self.screen.blit(self.image, self.rect);
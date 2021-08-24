import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
    ''' Manages Bullets Fired From The Ship '''
    def __init__(self, game):
        ''' Create A Bullet Object At The Ships Current Position '''
        super().__init__()
        self.screen = game.screen;
        self.settings = game.settings;
        self.color = self.settings.bulletColor;
        # Create A Bullet rect at (0,0) And Then The Set Current Position
        self.rect = pygame.Rect(0,0, self.settings.bulletWidth, self.settings.bulletHeight);
        self.rect.midtop = game.ship.rect.midtop;
        #store The Bullet's Position As A Decimal Value
        self.y = float(self.rect.y);
    
    def update(self):
        ''' Move The Bullet Up The Screen '''
        # Update The Decimal Position Of The Bullet
        self.y -= self.settings.bulletSpeed;
        #updated the Rect Position
        self.rect.y = self.y;

    def drawBullet(self):
        ''' Draw The Bullet To The Screen '''
        pygame.draw.rect(self.screen, self.color, self.rect);
    
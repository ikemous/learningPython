import pygame;
from pygame.sprite import Sprite;

class Bullet:
    ''' Class to handle the bullets '''
    def __init__(self, app):
        ''' Create bullet object at the ships current position '''
        super.__init__();
        self.screen = app.screen();
        self.settings = app.settings;
        self.color = self.settings.bulletColor;

        # Create bullet at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rect.midtop = app.ship.rect.midtop;

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y);
    
    def update(self):
        ''' Draw the bullet to the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect);
import pygame;
from settings import Settings;

class Square:
    ''' Class to help create the bullet '''
    def __init__(self, app, x, y):
        ''' Create the rect instance for the bullet '''
        self.settings = Settings();
        self.screen = app.screen;
        self.rect = pygame.Rect(x, y, self.settings.bulletWidth, self.settings.bulletHeight);
        self.color = self.settings.bulletColor;
        self.speed = self.settings.bulletSpeed;
    
    def draw(self):
        ''' Draw the rect onto the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect);
            
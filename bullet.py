import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
    ''' Class to handle the bullets '''

    def __init__(self, app, slope):
        ''' Create bullet object at the ships current position '''
        super().__init__();
        self.screen = app.screen;
        self.settings = app.settings;
        self.color = self.settings.bulletColor;

        # Create bullet at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bulletWidth, self.settings.bulletHeight)
        self.rect.midtop = app.player.rect.center;

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y);
        self.x = float(self.rect.x);

        self.slope = slope;
        
    
    def update(self):
        ''' Move the bullet ''' 
        self.x += self.slope;
        self.rect.x = self.x;
        self.y -= self.slope;
        self.rect.y = self.y;
        # self.y -= self.slope;
        # self.x += self.slope;
        # self.rect.center = (self.rect.x + self.slope, self.rect.y + self.slope)
        # self.rect.x = self.x;
        # self.rect.y = self.y;
        pass;

    def drawBullet(self):
        ''' Draw the bullet to the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect);
        # endPos = pygame.mouse.get_pos()
        # pygame.draw.line(self.screen, self.color, (self.rect.x, self.rect.y), endPos, width=20)
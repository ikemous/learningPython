import pygame;
from pygame.sprite import Sprite;

class Alien(Sprite):
    ''' A Class To Represent A Single Alien In The Fleet '''
    def __init__(self, game):
        ''' Initialize The Alien And Set Its Starting Position '''
        super().__init__()
        self.settings = game.settings;
        self.screen = game.screen;
        # Load The Alien And Set Its Starting Rect Attribute
        self.image = pygame.image.load('images/002-snake.png');
        self.rect = self.image.get_rect();
        # Start Each New Alien Near The Top Left Of The Screen
        self.rect.x = self.rect.width;
        self.rect.y = self.rect.height;
        # Store The Alien's Exact Horizontal Position
        self.x = float(self.rect.x);

    def checkEdges(self):
        ''' Return True If Alien Is At Edge Of The Screen '''
        screenRect = self.screen.get_rect();
        if (self.rect.right >= screenRect.right or self.rect.left <= 0):
            return True;

    def update(self):
        ''' Move The Alien To The Right or Left '''
        self.x += (self.settings.alienSpeed * self.settings.fleetDirection);
        self.rect.x = self.x;


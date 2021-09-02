import pygame;
from math import atan2, pi, cos, sin;
from pygame.sprite import Sprite;
from square import Square;

class Bullet(Square, Sprite):
    ''' Class to handle the bullets '''

    def __init__(self, app, x, y, targetx, targety):
        ''' Create bullet object at the ships current position '''
        # Call inheritance function(s)
        super().__init__(app, x, y);
        Sprite.__init__(self);

        # Calculate the angle between the player and mouse point
        angle = atan2(targety - y, targetx - x);
        
        # Starting x and y positions
        self.x = x;
        self.y = y;

        # Calculate the next point positions
        self.dx = cos(angle) * self.speed;
        self.dy = sin(angle) * self.speed;

    def update(self):
        ''' update the x and y positions to move the bullet '''
        # Calculate the new x and y positions 
        self.x = self.rect.x + self.dx;
        self.y = self.rect.y + self.dy;
        # Set the new x and y positions for the bullet
        self.rect.x = int(self.x);
        self.rect.y = int(self.y);
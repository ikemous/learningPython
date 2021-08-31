import pygame;
from math import sqrt, acos, degrees, hypot, atan2;
from settings import Settings;

class Player:
    ''' A Class To Manage The Player '''

    def __init__(self, app):
        ''' Initialize the player and its starting position '''
        self.screen = app.screen;
        self.screenRect = app.screen.get_rect();
        self.settings = Settings();

        # Load the player image and get its rect
        self.image = pygame.image.load(self.settings.playerImage);
        self.rect = self.image.get_rect();

        # Starting position of the player
        self.rect.midbottom = self.screenRect.midbottom;
        self.x = float(self.rect.x);
        self.y = float(self.rect.y);
        self.currentMousePos = (self.screenRect.centerx, 0);
        self.rotateAngle = 0;

        # Movement Flags
        self.movingRight = False;
        self.movingLeft = False;
        self.movingUp = False;
        self.movingDown = False;

    def updateRotateAngle(self):
        ''' Calculate rotation from old and new mouse posisitons '''
        # playerPos = (self.rect.x + 30, self.rect.y + 30);
        playerPos = (self.rect.centerx + 30, self.rect.centery - 30);
        self.currentMousePos = pygame.mouse.get_pos();
        angle = atan2(playerPos[0] - self.currentMousePos[0], playerPos[1] - self.currentMousePos[1]);
        self.rotateAngle = degrees(angle);

    def updateMovement(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.x += self.settings.playerSpeed;
        elif self.movingLeft and self.rect.left > 0:
            self.x -= self.settings.playerSpeed;
        elif self.movingUp and self.rect.top > 0:
            self.y -= self.settings.playerSpeed;
        elif self.movingDown and self.rect.bottom < self.screenRect.bottom:
            self.y += self.settings.playerSpeed;
        # Update the players x and y position
        self.rect.x = self.x;
        self.rect.y = self.y;

    def update(self):
        ''' Update the players position based on the movement flag '''
        self.updateMovement();
        self.updateRotateAngle();

    def blitme(self):
        ''' Draw the player at the current position '''
        self.screen.blit(pygame.transform.rotate(self.image, self.rotateAngle), self.rect);
import pygame;
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

        # Movement Flags
        self.movingRight = False;
        self.movingLeft = False;
        self.movingUp = False;
        self.movingDown = False;

    def update(self):
        ''' Update the players position based on the movement flag '''
        if self.movingRight:
            self.rect.x += self.settings.playerSpeed;
        elif self.movingLeft:
            self.rect.x -= self.settings.playerSpeed;
        elif self.movingUp:
            self.rect.y -= self.settings.playerSpeed;
        elif self.movingDown:
            self.rect.y += self.settings.playerSpeed;

    def blitme(self):
        ''' Draw the player at the current position '''
        self.screen.blit(self.image, self.rect);
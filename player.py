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

    def blitme(self):
        ''' Draw the player at the current position '''
        self.screen.blit(self.image, self.rect);
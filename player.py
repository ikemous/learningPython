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
        self.x = float(self.rect.x);
        self.y = float(self.rect.y);
        self.rotateAngle = 0;

        # Movement Flags
        self.movingRight = False;
        self.movingLeft = False;
        self.movingUp = False;
        self.movingDown = False;
    
    def turnPlayer(self):
        mousePosition = pygame.mouse.get_pos();
        print(mousePosition, (self.rect.x, self.rect.y))

    def update(self):
        ''' Update the players position based on the movement flag '''
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
        self.turnPlayer();
        self.image = pygame.transform.rotate(self.image, 90);

    def blitme(self):
        ''' Draw the player at the current position '''
        self.screen.blit(self.image, self.rect);
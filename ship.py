import pygame;

class Ship:
    ''' A Class To Manage The Ship '''
    def __init__(self, game):
        ''' Initialize The Ship And Set It's Starting Position '''
        self.screen = game.screen;
        self.screenRect = game.screen.get_rect();
        self.settings = game.settings;
        #load The Ship Image And Get Its Rect
        self.image = pygame.image.load(self.settings.shipImage);
        self.rect = self.image.get_rect();
        # Right Movement Flag
        self.movingRight = False;
        # Left Movement Flag
        self.movingLeft = False;
        # Up Movement Flag
        self.movingUp = False;
        # Down Movement Flag
        self.movingDown = False;
        self.x = float(self.rect.x);
        self.y = float(self.settings.screenHeight - 90);
        # Start Each New Ship At The Bottom Center Of The Screen
        self.rect.midbottom = self.screenRect.midbottom;

    def blitme(self):
        ''' Draw The Ship At The Bottom Center Of The Screen '''
        self.screen.blit(self.image, self.rect);
        
    def update(self):
        ''' Update The Ship's Position Based On The Movement Flag '''
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.x += self.settings.shipSpeed;
        if self.movingLeft and self.rect.left > 0:
            self.x -= self.settings.shipSpeed;
        if self.movingUp and self.rect.top > 0:
            self.y -= self.settings.shipSpeed;
        if self.movingDown and self.rect.top < self.settings.screenHeight - 90:
            self.y += self.settings.shipSpeed;
        # Update Rect Object from self.x
        self.rect.x = self.x;
        self.rect.y = self.y;

    def centerShip(self):
        ''' Center The Ship On The Screen '''
        self.rect.midbottom = self.screenRect.midbottom;
        self.x = float(self.rect.x);
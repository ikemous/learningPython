import sys;
import pygame;
import ctypes
from settings import Settings;
from bullet import Bullet;
from player import Player;

class Application:
    ''' Over class to manage game assets and behaviour '''

    def __init__(self):
        ''' initialize the gmae, and create game resources '''
        pygame.init();
        self.settings = Settings();
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight));
        self.icon = pygame.image.load(self.settings.appIcon);
        pygame.display.set_icon(self.icon);
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN);
        pygame.display.set_caption(self.settings.caption);
        self.player = Player(self);
        self.bullets = pygame.sprite.Group();

    def fireBullet(self):
        ''' Create a new bullet and add it to the bullets group '''
        newBullet = Bullet(self);
        self.bullets.add(newBullet);

    def checkKeyDown(self, event):
        ''' Respond To Key presses'''
        if event.key == pygame.K_a:
            self.player.movingLeft = True;
        elif event.key == pygame.K_d:
            self.player.movingRight = True;
        elif event.key == pygame.K_w:
            self.player.movingUp = True;
        elif event.key == pygame.K_s:
            self.player.movingDown = True;

    def checkKeyUp(self, event):
        ''' Respond To Key releases '''
        if event.key == pygame.K_a:
            self.player.movingLeft = False;
        elif event.key == pygame.K_d:
            self.player.movingRight = False;
        elif event.key == pygame.K_w:
            self.player.movingUp = False;
        elif event.key == pygame.K_s:
            self.player.movingDown = False;

    def mouseDown(self, event):
        if event.button == 1:
            self.fireBullet();
            print("Click", self.bullets);

    def checkEvents(self):
        ''' Respond To Keypresses and mouse events '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                self.checkKeyDown(event);
            elif event.type == pygame.KEYUP:
                self.checkKeyUp(event);
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown(event);
                    
    
    def drawBullets(self):
        for bullet in self.bullets.sprites():
            bullet.drawBullet();
            
    def updateScreen(self):
        self.screen.fill(self.settings.backgroundColor);
        self.player.blitme();
        for bullet in self.bullets.sprites():
            bullet.drawBullet();
        pygame.display.flip();

    def runGame(self):
        ''' Star the main loop for the game '''
        while True:
            self.checkEvents();      
            self.player.update(); 
            self.bullets.update();
            self.updateScreen();

if __name__ == '__main__':
    # Lines of code to allow the icon to be in the taskbar
    myappid = u'mycompany.myproduct.subproduct.version'; # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid);

    # Make a game instance and run the game
    app = Application();
    app.runGame();
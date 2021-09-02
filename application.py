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
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN);
        self.icon = pygame.image.load(self.settings.appIcon);
        pygame.display.set_icon(self.icon);
        pygame.display.set_caption(self.settings.caption);
        self.player = Player(self);
        self.bullets = pygame.sprite.Group();

    def fireBullet(self):
        ''' Create a new bullet and add it to the bullets group '''
        x,y = pygame.mouse.get_pos();
        newBullet = Bullet(self, self.player.rect.x + 30, self.player.rect.y + 30, x, y);
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
        ''' Respond to actions on the mouse press '''
        if event.button == 1:
            self.fireBullet();

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
        ''' Go Through Each Bullet and draw the sprites '''
        for bullet in self.bullets.sprites():
            bullet.draw();
    
    def removeBullets(self):
        ''' Remove Any Bullets from its sprite group '''
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0 or bullet.rect.bottom >= self.settings.screenHeight 
                    or bullet.rect.left <= 0 or bullet.rect.right >= self.settings.screenWidth):
                self.bullets.remove(bullet);  

    def updateScreen(self):
        ''' Update the screen and the items it contains '''
        self.screen.fill(self.settings.backgroundColor);
        self.player.blitme();
        self.drawBullets();
        pygame.display.flip();

    def runGame(self):
        ''' Star the main loop for the game '''
        while True:
            self.checkEvents();      
            self.player.update(); 
            self.bullets.update();
            self.updateScreen();
            self.removeBullets();
            


if __name__ == '__main__':
    # Lines of code to allow the icon to be in the taskbar
    myappid = u'ikemous.games.mygameapp.1'; # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid);

    # Make a game instance and run the game
    app = Application();
    app.runGame();
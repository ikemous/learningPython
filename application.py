import sys;
import pygame;
import ctypes
from settings import Settings;
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

    def checkEvents(self):
        ''' Respond To Keypresses and mouse events '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            
    def updateScreen(self):
        self.screen.fill(self.settings.backgroundColor);
        self.player.blitme();
        pygame.display.flip();

    def runGame(self):
        ''' Star the main loop for the game '''
        while True:
            self.checkEvents();       
            self.updateScreen();

if __name__ == '__main__':
    # Lines of code to allow the icon to be in the taskbar
    myappid = u'mycompany.myproduct.subproduct.version'; # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid);

    # Make a game instance and run the game
    app = Application();
    app.runGame();
import sys;
import pygame;

class Application:
    ''' Over class to manage game assets and behaviour '''

    def __init__(self):
        ''' initialize the gmae, and create game resources '''
        pygame.init();
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN);
        pygame.display.set_caption("");

    def runGame(self):
        ''' Star the main loop for the game '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit();
                
                pygame.display.flip();

if __name__ == '__main__':
    # Make a game instance and run the game
    app = Application();
    app.runGame();
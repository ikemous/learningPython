import sys;
import pygame;
from settings import Settings;
from ship import Ship;
from bullet import Bullet;
from alien import Alien;

class AlienInvasion:
    ''' Class to run the window of the game '''
    def __init__(self):
        ''' Initialize the game and create game resources '''
        pygame.init();
        # Create Settings Class
        self.settings = Settings();
        # Set screen display
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN);
        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight));
        self.settings.screenWidth = self.screen.get_rect().width;
        self.settings.screenHeight = self.screen.get_rect().height;
        # iconImage = pygame.image.load("images/snake.jpg");
        # pygame.display.set_icon(iconImage);
        # Set Game Title
        pygame.display.set_caption("Alien Invasion");
        self.ship = Ship(self);
        self.bullets = pygame.sprite.Group();
        self.aliens = pygame.sprite.Group();

        self.createFleet();

    def run_game(self):
        ''' Start the loop for the game '''
        while True:
            # Watch for keyboard and mouse events
            self.check_events();
            self.ship.update();
            self.bullets.update();
            for bullet in self.bullets.copy():
                if (bullet.rect.bottom <= 0):
                    self.bullets.remove(bullet);
            # Fill The Background Color Of The Screen
            self.updateScreen();

    def check_events(self):
        ''' Respond To Keypresses And Mouse Events '''
        for event in pygame.event.get():
            # Check if event quits the game
            if (event.type == pygame.QUIT):
                sys.exit();
            elif (event.type == pygame.KEYDOWN):
                self.checkKeyDownEvents(event);
            elif (event.type == pygame.KEYUP):
                self.checkKeyUpEvents(event);

    def updateScreen(self):
        ''' Update Images On The Screen, And Flip To The New Screen. '''
        self.screen.fill(self.settings.bgColor);
        self.ship.blitme();
        for bullet in self.bullets.sprites():
            bullet.drawBullet();
        self.aliens.draw(self.screen);
        # Make the most revently drawn screen visible
        pygame.display.flip();

    def checkKeyDownEvents(self, event):
        ''' Respond To Keypressess '''
        if (event.key == pygame.K_RIGHT):
            # Move The Ship To The Right
            self.ship.movingRight = True;
        elif (event.key == pygame.K_LEFT):
            self.ship.movingLeft = True;
        elif (event.key == pygame.K_UP):
            self.ship.movingUp = True;
        elif (event.key == pygame.K_DOWN):
            self.ship.movingDown = True;
        elif (event.key == pygame.K_SPACE):
            self.fireBullet();
        elif (event.key == pygame.K_q):
            sys.exit();

    def checkKeyUpEvents(self, event):
        if (event.key == pygame.K_RIGHT):
            self.ship.movingRight = False;
        elif (event.key == pygame.K_LEFT):
            self.ship.movingLeft = False;
        elif (event.key == pygame.K_UP):
            self.ship.movingUp = False;
        elif (event.key == pygame.K_DOWN):
            self.ship.movingDown = False;

    def fireBullet(self):
        ''' Create A new Bullet And Add It To The Bullets Group '''
        newBullet = Bullet(self);
        self.bullets.add(newBullet);

    def createFleet(self):
        ''' Create The Fleet Of Aliens '''
        # Make An Alien
        alien = Alien(self);
        alienWidth, alienHeight = alien.rect.size;
        availableSpaceX = self.settings.screenWidth - (2 * alienWidth);
        numberAliensX = availableSpaceX // (2 * alienWidth);
        #Determine  The Number Of Rows Of Aliens That Fit On The Screen
        shipHeight = self.ship.rect.height;
        availableSpaceY = (self.settings.screenHeight - (3 * alienHeight) - shipHeight);
        numberRows = availableSpaceY // (2 * alienHeight);
        # Create the fleet Of Aliens
        for rowNumber in range(numberRows):
            for alienNumber in range(numberAliensX):
                self.createAlien(alienNumber, rowNumber);

    def createAlien(self, alienNumber, rowNumber):
        ''' Create An Alien And Place It In The Row '''
        alien = Alien(self);
        alienWidth, alienHeight = alien.rect.size;
        alien.x = alienWidth + 2 * alienWidth * alienNumber;
        alien.rect.x = alien.x;
        alien.rect.y= alien.rect.height + 2 * alien.rect.height * rowNumber;
        self.aliens.add(alien);

if __name__ == "__main__":
    # Make the game instance
    ai = AlienInvasion();
    # Run the game
    ai.run_game();
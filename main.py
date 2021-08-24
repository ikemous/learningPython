import sys;
from time import sleep;
import pygame;
from settings import Settings;
from ship import Ship;
from bullet import Bullet;
from alien import Alien;
from gameStats import GameStats;

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
        self.stats = GameStats(self);
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
            self.updateBullets();
            self.updateAliens();
            # Fill The Background Color Of The Screen
            self.updateScreen();

    def updateBullets(self):
        ''' Update Position Of Bullets And Get Rid Of Old Bullets '''
        self.bullets.update();
        # Remove Bullets That Disappeared
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0):
                self.bullets.remove(bullet);
        self.checkBulletAlienCollisions();

    def checkBulletAlienCollisions(self):
        ''' Respond To Bullet-Alien Collisions '''
        # Check For Any Bullets That Hit Aliens
        # If Collided Remove The Bullet And The Alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True);
        if not self.aliens:
            self.bullets.empty();
            self.createFleet();

    def checkFleetEdges(self):
        ''' Respond Appropriately If Any Aliens Have Reached An Edge '''
        for alien in self.aliens.sprites():
            if alien.checkEdges():
                self.changeFleetDirection();
                break;
    
    def changeFleetDirection(self):
        ''' Drop The Entire Fleet And change The Fleet's Direction '''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleetDropSpeed;
        self.settings.fleetDirection *= -1;

    def updateAliens(self):
        ''' 
            Check If The Fleet Is At An Edge
            Then Update The Positions Of All Aliens In The Fleet
        '''
        self.checkFleetEdges();
        self.aliens.update();
        # Look for alien-ship collistions
        if (pygame.sprite.spritecollideany(self.ship, self.aliens)):
            self.shipHit();
        # Look For Aliens Hittong The Bottom Of The Screen
        self.checkAliensBottom();

    def shipHit(self):
        ''' Respond To The Ship Being Hit By An Alien '''
        # Decrement Ships Left Stat
        self.stats.shipsLeft -= 1;
        # Get Rid Of Any Remaining Aliens And Bullets
        self.aliens.empty();
        self.bullets.empty();
        # Create A New Fleet And Center The Ship
        self.createFleet();
        self.ship.centerShip();
        # Pause
        sleep(0.5);        

    def checkAliensBottom(self):
        ''' Check If Any Alines Have Reached The Bottom Of The Screen '''
        screenRect = self.screen.get_rect();
        for alien in self.aliens.sprites():
            if (alien.rect.bottom >= screenRect.bottom):
                self.shipHit();
                break;

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
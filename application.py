import sys;
import pygame;
import ctypes;
from time import sleep;
from settings import Settings;
from bullet import Bullet;
from player import Player;
from enemy import Enemy;
from minion import Minion;
from gameStats import GameStats;
from button import Button;
from scoreboard import Scoreboard;
from boss import Boss;

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
        self.stats = GameStats(self);
        self.scoreboard = Scoreboard(self);
        self.player = Player(self);
        self.bullets = pygame.sprite.Group();
        self.enemies = pygame.sprite.Group();
        self.minions = pygame.sprite.Group();
        self.updateEnemyCount();
        self.playButton = Button(self, "Play");

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

    def checkPlayButton(self, mousePos):
        buttonClicked = self.playButton.rect.collidepoint(mousePos);
        if buttonClicked and not self.stats.gameActive:
            self.stats.resetStats();
            self.stats.gameActive = True;
            self.enemies.empty();
            self.bullets.empty();
            self.scoreboard.prepScore();
            self.scoreboard.prepPlayers();

    def mouseDown(self, event):
        ''' Respond to actions on the mouse press '''
        if event.button == 1:
            if self.stats.gameActive:
                self.fireBullet();
            else:
                mousePos = pygame.mouse.get_pos();
                self.checkPlayButton(mousePos);

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
    
    def updateEnemyCount(self):
        if len(self.enemies) < 6:
            count = len(self.enemies);
            while count < self.settings.MAX_ENEMIES:
                newEnemy = Enemy(self);
                self.enemies.add(newEnemy);
                count += 1;

    def createMinions(self):
        if len(self.minions) < self.settings.MAX_ENEMIES:
            count = len(self.minions);
            while count < self.settings.MAX_ENEMIES:
                newMinion = Minion(self);
                self.minions.add(newMinion);
                count += 1;

    def drawMinions(self):
        for minion in self.minions:
            minion.blitme();

    def checkMinionOutOfBounds(self):
        for minion in self.minions.copy():
            if (minion.rect.bottom <= -40 or minion.rect.bottom >= self.settings.screenHeight + 40
                    or minion.rect.left <= -40 or minion.rect.right >= self.settings.screenWidth + 40):
                self.minions.remove(minion);

    def checkBulletMinionCollisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.minions, True, False);
        if collisions:
            for minionGroup in collisions.values():
                for minion in minionGroup:
                    minion.health -= 1;
                    if minion.health <= 0:
                        self.stats.score += minion.points;
                        self.minions.remove(minion);
                        self.stats.killCount += 1;
                        self.scoreboard.prepScore();

    def checkPlayerMinionCollisions(self):
        if pygame.sprite.spritecollideany(self.player, self.minions):
            self.playerHit();

    def playerHit(self):
        if self.stats.lives > 0:
            self.stats.lives -= 1;
            self.scoreboard.prepPlayers();
            self.minions.empty();
            self.bullets.empty();
            self.player.centerPlayer();
            sleep(1);
        else:
            self.minions.empty();
            self.bullets.empty();
            self.stats.gameActive = False;

    def updateScreen(self):
        ''' Update the screen and the items it contains '''
        self.screen.fill(self.settings.backgroundColor);
        self.player.blitme();
        self.minions.update();
        self.drawMinions();
        self.drawBullets();
        self.scoreboard.show();
        if not self.stats.gameActive:
            self.playButton.draw();
        pygame.display.flip();

    def runGame(self):
        ''' Star the main loop for the game '''
        while True:
            self.checkEvents();
            if self.stats.gameActive:
                self.createMinions();
                self.bullets.update();
                self.checkMinionOutOfBounds();
                self.checkBulletMinionCollisions()
                self.removeBullets();
                self.checkPlayerMinionCollisions();
            self.player.update();
            self.updateScreen();

if __name__ == '__main__':
    # Lines of code to allow the icon to be in the taskbar
    myappid = u'ikemous.games.mygameapp.1'; # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid);

    # Make a game instance and run the game
    app = Application();
    app.runGame();
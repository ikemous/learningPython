import sys;
import pygame;
import ctypes;
import random;
from threading import Timer;
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
        # Initiate pygame
        pygame.init();

        # Grab Settings
        self.settings = Settings();

        # Set game screen componenets
        # self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight));
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN);
        self.settings.screenWidth = self.screen.get_rect().width;
        self.settings.screenHeight = self.screen.get_rect().height;
        self.icon = pygame.image.load(self.settings.appIcon);
        pygame.display.set_icon(self.icon);
        pygame.display.set_caption(self.settings.caption);

        # initiate Stas/Scoreboard
        self.stats = GameStats(self);
        self.scoreboard = Scoreboard(self);

        # Create The Player
        self.player = Player(self);

        # Create Other Sprite Groups(Enemies, Boss, Bullets)
        self.boss = Boss(self);
        self.bullets = pygame.sprite.Group();
        self.enemies = pygame.sprite.Group();
        self.minions = pygame.sprite.Group();

        # Create Buttons
        centerScreen = self.screen.get_rect().center;
        
        self.playButton = Button(self, "Play", center=centerScreen);
        self.quitButton = Button(self, "Quit", width=100, center=(70, 40));
        
        # Draw Buttons
        self.drawMainMenu();

        # Create timer variable for future use
        self.timer = None;

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
        elif event.key == pygame.K_ESCAPE:
            self.stats.gameActive = not self.stats.gameActive;

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

    def startGame(self):
        self.stats.gameActive = True;
        self.stats.gameStarted = True;

    def exitGame(self):
        if self.timer != None and self.timer._started:
            self.cancelTimer();
        self.enemies.empty();
        self.bullets.empty();
        sys.exit();

    def checkPlayButton(self, mousePos):
        buttonClicked = self.playButton.rect.collidepoint(mousePos);
        if buttonClicked and not self.stats.gameActive:
            self.stats.gameActive = True;
            if not self.stats.gameStarted:
                self.stats.resetStats();
                self.enemies.empty();
                self.bullets.empty();
                self.scoreboard.prepScore();
                self.scoreboard.prepPlayers();
                self.stats.gameStarted = True;
                self.createTimer();

    def checkQuitButton(self, mousePos):
        buttonClicked = self.quitButton.rect.collidepoint(mousePos);
        if buttonClicked:
            self.exitGame();

    def mouseDown(self, event):
        ''' Respond to actions on the mouse press '''
        if event.button == 1:
            if self.stats.gameActive:
                self.fireBullet();
            else:
                mousePos = pygame.mouse.get_pos();
                self.checkPlayButton(mousePos);
                self.checkQuitButton(mousePos);

    def checkEvents(self):
        ''' Respond To Keypresses and mouse events '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exitGame();
            elif event.type == pygame.KEYDOWN:
                self.checkKeyDown(event);
            elif event.type == pygame.KEYUP:
                self.checkKeyUp(event);
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown(event);
    
    def fireBullet(self):
        ''' Create a new bullet and add it to the bullets group '''
        x,y = pygame.mouse.get_pos();
        newBullet = Bullet(self, self.player.rect.x + 30, self.player.rect.y + 30, x, y);
        self.bullets.add(newBullet);

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

    def checkBulletBossCollisions(self):
        collision = pygame.sprite.spritecollideany(self.boss, self.bullets);
        if collision:
            self.bullets.remove(collision);
            self.boss.health -= 1;
            if self.boss.health <= 0:
                self.stats.bossSpawned = False;
                self.stats.score += self.boss.points;
                self.stats.killCount += 1;
                self.boss = None;
                self.scoreboard.prepScore();       
                self.startNextStage();         

    def checkPlayerMinionCollisions(self):
        if pygame.sprite.spritecollideany(self.player, self.minions):
            self.playerHit();
        
    def checkPlayerBossCollision(self):
        if pygame.sprite.collide_rect(self.player, self.boss):
            self.playerHit();

    def checkBossOutOfBounds(self):
        if (self.boss.rect.bottom <= -60 or self.boss.rect.bottom >= self.settings.screenHeight + 60
                    or self.boss.rect.left <= -60 or self.boss.rect.right >= self.settings.screenWidth + 60):
            self.resetBoss();

    def resetBoss(self):
        boss = Boss(self);
        boss.health = self.boss.health;
        self.boss = boss;

    def spawnBoss(self):
        self.stats.bossSpawned = True;
        self.boss = Boss(self);

    def cancelTimer(self):
        self.timer.cancel();
        self.timer = None;
    
    def createTimer(self):
        self.timer = Timer(self.stats.stageTimer, self.spawnBoss);
        self.timer.start();

    def startNextStage(self):
        self.stats.stage += 1;
        self.boss = None;
        self.boss = Boss(self);
        self.cancelTimer();
        self.createTimer();
        self.minions.empty();
        sleep(1);

    def playerHit(self):
        if self.stats.lives > 0:
            self.stats.lives -= 1;
            self.scoreboard.prepPlayers();
            self.resetBoss();
            self.minions.empty();
            self.bullets.empty();
            self.player.centerPlayer();
            sleep(1);
        else:
            self.minions.empty();
            self.bullets.empty();
            self.resetBoss();
            self.stats.bossSpawned = False;
            self.stats.gameActive = False;
            if self.timer._started:
                self.cancelTimer();

    def drawMainMenu(self):
        self.playButton.draw();
        self.quitButton.draw();
        pass;
    
    def updateGame(self):
        self.createMinions();
        self.bullets.update();
        self.checkMinionOutOfBounds();
        self.checkBulletMinionCollisions();
        self.removeBullets();
        self.checkPlayerMinionCollisions();
        if self.stats.bossSpawned:
            self.boss.update();
            self.checkBossOutOfBounds();
            self.checkBulletBossCollisions();
            self.checkPlayerBossCollision();

    def updateScreen(self):
        ''' Update the screen and the items it contains '''
        self.screen.fill(self.settings.backgroundColor);
        if not self.stats.gameActive:
            self.drawMainMenu();
        else:
            self.scoreboard.show();
            self.player.blitme();
            self.minions.update();
            self.drawMinions();
            self.drawBullets();
            if self.stats.bossSpawned:
                self.boss.blitme();
        pygame.display.flip();

    def runGame(self):
        ''' Star the main loop for the game '''
        while True:
            # Check For Any Key Press Events
            self.checkEvents();
            # Check If The Game Is Active
            if self.stats.gameActive and self.stats.gameStarted:
                # Update The Game
                self.updateGame();
            # # Update The Player
            self.player.update();
            # Update The Screen
            self.updateScreen();

if __name__ == '__main__':
    # Lines of code to allow the icon to be in the taskbar
    myappid = u'ikemous.games.mygameapp.1'; # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid);

    # Make a game instance and run the game
    app = Application();
    app.runGame();
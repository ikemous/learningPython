import pygame.font;
from pygame.sprite import Group;
from player import Player;

class Scoreboard:

    def __init__(self, app):
        self.app = app;
        self.screen = app.screen;
        self.screenRect = self.screen.get_rect();
        self.settings = app.settings;
        self.stats = app.stats;

        self.textColor = (30, 30, 30);
        self.font = pygame.font.SysFont(None, 48);

        self.prepScore();
        self.prepPlayers();

    def prepScore(self):
        roundedScore = round(self.stats.score, -1);
        scoreString =  "{:,}".format(roundedScore);
        self.scoreImage = self.font.render(scoreString, True, self.textColor, self.settings.backgroundColor);
        self.scoreRect = self.scoreImage.get_rect();
        self.scoreRect.right = self.screenRect.right - 20;
        self.scoreRect.top = 20;
    
    def prepPlayers(self):
        self.players = Group();
        for playerNumber in range(self.stats.lives):
            player = Player(self.app);
            player.rect.x = 10 + playerNumber * player.rect.width;
            player.rect.y = 10
            self.players.add(player);
    
    def show(self):
        self.screen.blit(self.scoreImage, self.scoreRect);
        self.players.draw(self.screen);
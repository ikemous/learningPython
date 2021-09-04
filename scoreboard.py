import pygame.font;

class Scoreboard:

    def __init__(self, app):
        self.screen = app.screen;
        self.screenRect = self.screen.get_rect();
        self.settings = app.settings;
        self.stats = app.stats;

        self.textColor = (30, 30, 30);
        self.font = pygame.font.SysFont(None, 48);

        self.prepScore();

    def prepScore(self):
        scoreString = str(self.stats.score);
        self.scoreImage = self.font.render(scoreString, True, self.textColor, self.settings.backgroundColor);
        self.scoreRect = self.scoreImage.get_rect();
        self.scoreRect.right = self.screenRect.right - 20;
        self.scoreRect.top = 20;
    
    def show(self):
        self.screen.blit(self.scoreImage, self.scoreRect);
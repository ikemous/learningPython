class GameStats:

    def __init__(self, app):
        self.settings = app.settings;
        self.resetStats();
        self.gameActive = False;

    def resetStats(self):
        self.lives = self.settings.playerLives;
        self.score = 0;
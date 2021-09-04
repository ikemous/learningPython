class GameStats:

    def __init__(self, app):
        self.settings = app.settings;
        self.resetStats();
        self.gameActive = True;

    def resetStats(self):
        self.lives = self.settings.playerLives;
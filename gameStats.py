class GameStats:

    def __init__(self, app):
        self.settings = app.settings;
        self.resetStats();
        self.gameActive = False;
        self.stage = 1;
        self.bossSpawned = True;

    def resetStats(self):
        self.lives = self.settings.playerLives;
        self.score = 0;
        self.stage = 1;
        self.killCount = 0;
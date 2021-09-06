class GameStats:

    def __init__(self, app):
        self.settings = app.settings;
        self.resetStats();
        self.gameActive = False;
        self.bossSpawned = False;
        self.stageTimer = 90;
        self.stage = 1;

    def resetStats(self):
        self.lives = self.settings.playerLives;
        self.bossSpawned = False;
        self.score = 0;
        self.stage = 1;
        self.killCount = 0;
class GameStats:

    def __init__(self, app):
        self.settings = app.settings;
        self.resetStats();
        self.gameActive = False;
        self.gameStarted = False;
        self.bossSpawned = False;
        self.stage = 1;
        self.stageTimer = self.settings.enemyBosses[str(self.stage)]["timer"];

    def resetStats(self):
        self.lives = self.settings.playerLives;
        self.bossSpawned = False;
        self.score = 0;
        self.stage = 1;
        self.stageTimer = self.settings.enemyBosses[str(self.stage)]["timer"];
        self.killCount = 0;
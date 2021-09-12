import json;

bosses = None;
enemies = None;

with open("bosses.json") as jsonFile:
    bosses = json.load(jsonFile);

with open("enemies.json") as jsonFile:
    enemies = json.load(jsonFile);

class Settings:
    ''' Class To Hold All Settings For The Application '''

    def __init__(self):
        ''' Initialize the settings class'''

        # Window Settings
        self.caption = "Space ship";
        self.screenWidth = 1200;
        self.screenHeight = 800;
        self.backgroundColor = (212, 241, 249);
        self.appIcon = "images\\icon.png";

        # Player Settings
        self.playerImage = "images\\playerImages\\stingray.bmp";
        self.playerSpeed = 1;
        self.playerLives = 3;

        # Bullet Settings
        self.bulletSpeed = 3.0;
        self.bulletWidth = 10;
        self.bulletHeight = 20;
        self.bulletColor = (10, 10, 10);

        # Enemy Settings
        self.enemySpeed = 0.2;
        self.enemyBosses = bosses;
        self.enemyGroups = enemies;
        self.MAX_ENEMIES = 6;
        self.enemyPoints = 10;
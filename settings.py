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
        self.enemyImages = [
            "images\\enemyImages\\rabbit.bmp",
            "images\\enemyImages\\beetle.bmp",
            "images\\enemyImages\\boar.bmp",
            "images\\enemyImages\\walrus.bmp",
        ];
        self.MAX_ENEMIES = 6;
        self.enemyPoints = 10;
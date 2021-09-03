class Settings:
    ''' Class To Hold All Settings For The Application '''

    def __init__(self):
        ''' Initialize the settings class'''
        # Window Settings
        self.caption = "Space ship";
        self.screenWidth = 1200;
        self.screenHeight = 800;
        self.backgroundColor = (100, 50, 10);
        self.appIcon = "images\\icon.png";

        # Player Settings
        self.playerImage = "images\\stingray.bmp";
        self.playerSpeed = 1;

        # Bullet Settings
        self.bulletSpeed = 3.0;
        self.bulletWidth = 10;
        self.bulletHeight = 20;
        self.bulletColor = (10, 10, 10);

        # Enemy Settings
        self.enemySpeed = 0.2;
        self.enemyImages = [
            "images\\walrus.bmp",
            "images\\rabbit.bmp",
            "images\\beetle.bmp",
            "images\\rhino.bmp",
            "images\\squid.bmp",
            "images\\boar.bmp",
            "images\\snake.bmp",
        ];
        self.MAX_ENEMIES = 4;
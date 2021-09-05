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
        self.enemyGroups = {
            1: [
                {
                    "name": "ribbit",
                    "imagePath": "images\\enemy\\frog.bmp",
                    "points": 10,
                    "speed": 0.2,
                    "health": 1,
                },
                {
                    "name": "perry",
                    "imagePath": "images\\enemy\\platypus.bmp",
                    "points": 100,
                    "speed": 0.4,
                    "health": 1,
                },
                {
                    "name": "mumbo",
                    "imagePath": "images\\enemy\penguin.bmp",
                    "points": 25,
                    "speed": 0.1,
                    "health": 1,
                },
                {
                    "name": "wally",
                    "imagePath": "images\\enemy\\walrus.bmp",
                    "points": 75,
                    "speed": 0.1,
                    "health": 1,
                }
            ],
            # 2: [],
            # 3: [],
            # 4: [],
        };
        self.enemyImages = [
            "images\\enemy\\rabbit.bmp",
            "images\\enemy\\beetle.bmp",
            "images\\enemy\\boar.bmp",
            "images\\enemy\\walrus.bmp",
        ];
        self.MAX_ENEMIES = 6;
        self.enemyPoints = 10;
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
        self.enemyBosses = {
            1: {
                "name": "Bruce",
                "imagePath": "images\\boss\\shark.bmp",
                "points": 1000,
                "speed": 0.3,
                "health": 100,
            },
            2: {
                "name": "Big boi 2000",
                "imagePath": "images\\boss\\elephant.bmp",
                "points": 10000,
                "speed": 0.05,
                "health": 250,
            },
            3: {
                "name": "Buffy The Buffalo",
                "imagePath": "images\\boss\\buffalo.bmp",
                "points": 50000,
                "speed": 0.2,
                "health": 500,
            },
        }
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
            2: [
                {
                    "name": "the copycat",
                    "imagePath": "images\\enemy\\parrot.bmp",
                    "points": 110,
                    "speed": 0.35,
                    "health": 2,
                },
                {   
                    "name": "do you feel it now mrCrabs?",
                    "imagePath": "images\\enemy\\crab.bmp",
                    "points": 125,
                    "speed": 0.25,
                    "health": 3,
                },
                {
                    "name": "bully mc bullfinch",
                    "imagePath": "images\\enemy\\bullfinch.bmp",
                    "points": 75,
                    "speed": 0.5,
                    "health": 1,
                },
                {
                    "name": "pinky the flamingo",
                    "imagePath": "images\\enemy\\flamingo.bmp",
                    "points": 200,
                    "speed": 0.15,
                    "health": 8,
                },
            ],
            3: [
                {
                    "name": "charlet the spider",
                    "imagePath": "images\\enemy\\spider.bmp",
                    "points": 20,
                    "speed": 0.45,
                    "health": 1,
                },
                {
                    "name": "not so ladybug",
                    "imagePath": "images\\enemy\\ladybug.bmp",
                    "points": 25,
                    "speed": 0.65,
                    "health": 1,
                },
                {
                    "name": "i can't believe it's not butter",
                    "imagePath": "images\\enemy\\butterfly.bmp",
                    "points": 50,
                    "speed": 0.75,
                    "health": 1,
                },
                {
                    "name": "berry the bee",
                    "imagePath": "images\\enemy\\bee.bmp",
                    "points": 200,
                    "speed": 0.75,
                    "health": 1,
                },
            ],
            # 4: [],
        };
        self.MAX_ENEMIES = 6;
        self.enemyPoints = 10;
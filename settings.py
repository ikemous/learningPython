class Settings:
    ''' Class To Store All Settings For The Game '''
    def __init__(self):
        ''' Initialize The Game's Settings '''
        # Screen Settings
        self.screenWidth = 1200;
        self.screenHeight = 800;
        self.bgColor = (200, 100, 200);
        self.shipSpeed = 1.5;
        self.applicationIcon = "images/beetle.png";

        # Bullet Settings
        self.bulletSpeed = 1.0;
        self.bulletWidth = 3;
        self.bulletHeight = 15;
        self.bulletColor = (60, 60, 60);

        # Ship Settings
        self.shipImage = "images/beetle.png"
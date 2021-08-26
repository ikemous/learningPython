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
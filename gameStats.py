class GameStats:
    ''' Track Statistics For Alien Invasion '''

    def __init__(self, game):
        ''' Initialize Stats '''
        self.settings = game.settings;
        self.resetStats();
    
    def resetStats(self):
        ''' Initialize Statistics That Can Change During The Game '''
        self.shipsLeft = self.settings.shipLimit;
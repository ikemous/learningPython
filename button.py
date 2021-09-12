import pygame.font;

class Button:

    def __init__(
            self, app, msg, width = 200, height = 50, color = (255, 255, 255),
            textColor = (0, 255, 0), center = (300, 300)
        ):

        self.screen = app.screen;
        self.screenRect = self.screen.get_rect();

        self.width, self.height = width, height;
        self.buttonColor = color;
        self.textColor = textColor;
        self.font = pygame.font.SysFont(None, 48);

        self.rect = pygame.Rect(0, 0, self.width, self.height);
        self.rect.center = center;

        self.prepMsg(msg);

    def prepMsg(self, msg):
        self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor);
        self.msgImageRect = self.msgImage.get_rect();
        self.msgImageRect.center = self.rect.center;

    
    def draw(self):
        self.screen.fill(self.buttonColor, self.rect);
        self.screen.blit(self.msgImage, self.msgImageRect);
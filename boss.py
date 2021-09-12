import pygame;
from enemy import Enemy;

class Boss(Enemy):
    def __init__(self, app):
        super().__init__(app);
        
        stage = str(app.stats.stage);
        bossSettings = self.settings.enemyBosses[stage];
        self.points = bossSettings["points"];
        self.health = bossSettings["health"];
        self.healthBarLength = self.rect.width;
        self.healthRatio = self.health / self.healthBarLength;
        self.speed = bossSettings["speed"];
        imagePath = bossSettings["imagePath"];
        self.image = pygame.image.load(imagePath);
        self.rect = self.image.get_rect();

    def blitme(self):
        self.screen.blit(self.image, self.rect);
        pygame.draw.rect(self.screen, (255, 0, 0), (self.rect.x, self.rect.y + 65, self.health/self.healthRatio, 10));
        pygame.draw.rect(self.screen, (255, 255, 255), (self.rect.x, self.rect.y + 65, self.healthBarLength, 10), 4);
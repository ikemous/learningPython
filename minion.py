import pygame;
from enemy import Enemy;
from random import randint;

class Minion(Enemy):

    def __init__(self, app):
        super().__init__(app);

        stage = app.stats.stage;
        enemyNumber = randint(0, len(self.settings.enemyGroups[stage]) - 1);
        enemySettings = self.settings.enemyGroups[stage][enemyNumber];
        self.points = enemySettings["points"];
        self.health = enemySettings["health"];
        self.speed = enemySettings["speed"];
        imagePath = enemySettings["imagePath"];
        self.image = pygame.image.load(imagePath);
        self.rect = self.image.get_rect();
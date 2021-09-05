import pygame;
from enemy import Enemy;

class Boss(Enemy):
    def __init__(self, app):
        super().__init__(app);

    def checkCollision(self, otherRect):
        pass;
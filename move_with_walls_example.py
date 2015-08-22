#!/usr/bin/env python

import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()
        
        self.image = pygame.Surface([15,15])
        self.image.fill(WHITE)
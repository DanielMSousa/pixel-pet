#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:33:14 2021

@author: daniel
"""

#import os

import pet

import pygame
from pygame.locals import *

from sys import exit

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pixel pet')
clock = pygame.time.Clock()

#how many times bigger the sprite of the pet should be
p = 8

my_pet = pet.Pet('Julio', specie='ghost', health=20)

class PetSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load(f'pets/{my_pet.specie}/Tamagotchi-happy.png'))
        self.sprites.append(pygame.image.load(f'pets/{my_pet.specie}/Tamagotchi-idle.png'))
        self.sprites.append(pygame.image.load(f'pets/{my_pet.specie}/Tamagotchi-unhappy.png'))
        self.sprites.append(pygame.image.load(f'pets/{my_pet.specie}/Tamagotchi-sick.png'))
        self.sprites.append(pygame.image.load(f'pets/{my_pet.specie}/Tamagotchi-dead.png'))
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (p * 32, p * 32))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 320 - 4 * 32, 240 - 4 * 32
        
        self.sprite_list = {
            'happy': 0,
            'idle': 1,
            'unhappy': 2,
            'sick': 3,
            'dead': 4
        }
    
    def update(self):
        self.image = self.sprites[self.sprite_list[my_pet.mood]]
        self.image = pygame.transform.scale(self.image, (p * 32, p * 32))

all_sprites = pygame.sprite.Group()
pet_sprite = PetSprite()
all_sprites.add(pet_sprite)

while True:
    screen.fill((5, 156, 213))
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    my_pet.update()
    
    all_sprites.draw(screen)
    all_sprites.update()
    
    pygame.display.update()
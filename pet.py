#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 18:08:57 2021

@author: daniel
"""

class Pet:
    def __init__(self, name, specie, food=100, health=100, sleep=100, happiness=100, alive=True):
        # this one starts the pet based in the last state of it and the last time
        # the pet was feed, slept, etc...~
        self.name = name
        self.specie = specie
        self.food = food
        self.health = health
        self.sleep = sleep
        self.happiness = happiness
        self.alive = alive
        self.counter = 0
        self.mood = 'happy'
        self.sleeping = False
        
    def render(self):
        #renders the pet based in his mood
        pass
    
    def checkmood(self):
        if not(self.sleeping):
            if (self.health <= 40):
                self.mood = 'sick'
            elif(self.food >= 75):
                self.mood =  'happy'
            elif (self.food < 75 and self.food >= 50):
                self.mood = 'idle'
            else:
                self.mood = 'unhappy'
        else:
            self.mood = 'sleeping'
            
        return self.mood
    
    def checkalive(self):
        return not(self.sleep == 0 and self.food == 0)
    #and self.health == 0 and self.happiness == 0
    
    def update(self):
        #this function will try to predict how the pet should be based in the last
        #time the player took care of it
        #If there's more than 2 without feeding you pet it'll die
        if (self.checkalive()):
            self.mood = self.checkmood()
            self.counter += 1
            if(self.counter == 10):
                self.counter = 0
                self.food -= 1
                self.sleep -= 1
                print(self.food, self.sleep)
                print(self.checkmood())
        else:
            self.mood = 'dead'
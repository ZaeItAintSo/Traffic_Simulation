"""
Zae Moore
10/14/2021
Model traffic jams
"""
import pygame
import numpy as np

class car:
    def __init__(self, aMass, aLength, aWidth, aTheta, aMaxV, aVel, aMaxA, aAcc, aReact, aColor, aScreen):
        self.mass = aMass #kg
        self.length = aLength #m
        self.width = aWidth #m
        self.theta = aTheta #angle, degrees
        self.maxv = aMaxV #m/s
        self.vel = aVel #m/s
        self.maxa = aMaxA #m/s^2
        self.acc = aAcc #m/s^2
        self.react = aReact #s
        self.color = aColor
        self.screen = aScreen
        self.radius = 250
        self.screen_width = 750
        self.screen_height = 750
    def getAcc(self):
        return self.acc
    def getVel(self):
        return self.vel
    def getPos(self):
        return self.theta
    def getMaxA(self):
        return self.maxa
    def getMaxV(self):
        return self.maxv
    def setAcc(self, aAcc):
        self.acc = aAcc/self.radius
    def setVel(self, aVel):
        self.vel = aVel/self.radius
    def setPos(self, aTheta):
        self.theta = aTheta
    def updateAcc(self, aAcc):
        self.acc = aAcc/self.radius
    def updateVel(self):
        self.vel += self.acc*self.react #Angular v
    def updatePos(self):
        self.theta += self.vel*self.react%360 #Theta
        #Modulo 360!!! Then you dont have to worry about how many times it's gone around the circle, it just gives an angle between 0 and 360deg
    def draw_car(self):
        self.x = np.cos(self.theta)*self.radius + self.screen_width/2
        self.y = np.sin(self.theta)*self.radius + self.screen_height/2
        self.size = self.length*self.width
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
    

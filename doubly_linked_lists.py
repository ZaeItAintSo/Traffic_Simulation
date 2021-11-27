"""
Zae Moore
10/14/2021
Model traffic jams
"""
import highwayobjects as objC
import numpy as np
import pygame

"""
Checks:
check if there's a crash
distance in between you and next car in front and behind
double linked list?
Have pygame print numbers in the corner like number of cars, average speed of cars, average distance between cars, etc.
"""
##################################################################
#Highway Code
##################################################################
# Setting basic variables
running = True

background_color = "black"

track_radius = 250 # Radius to the center of the track

# Screen size generated with pygame
screen_width = 750
screen_height = 750
(width, height) = (screen_width, screen_height)

# Setting up the pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Simulation")
screen.fill(background_color)

def draw_track():
    pygame.draw.circle(screen, "gray", (screen_width/2, screen_height/2), 300)
    pygame.draw.circle(screen, "black", (screen_width/2, screen_height/2), 200)

class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
            return
         
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.count += 1

    def getNext(self, index):
        start = self.head
        thing = start
        for i in range(index):
            thing = thing.next
        return thing

# Create a new Doubly Linked List
carList = doublyLinkedList()
carList.append(objC.car(2000, 5, 2, 0, 60, 0, 2, 0, 0.3, "red", screen))
carList.append(objC.car(2300, 5, 2, 90, 70, 0, 3, 0, 0.3, "blue", screen))
carList.append(objC.car(2300, 5, 2, 180, 80, 0, 5, 0, 0.3, "green", screen))

#Loop through objects
while running:
    for event in pygame.event.get():
        # Allows the code to be quit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            screen.fill(background_color)
            draw_track()

            current = carList.head
            #currentCar = carList.head.item

            for i in range(carList.count):
                currentCar = current.item

                if currentCar.getVel() > currentCar.getMaxV():
                    currentCar.updateAcc(-currentCar.getMaxA())
                if currentCar.getVel() == currentCar.getMaxV():
                    currentCar.updateAcc(0)
                if currentCar.getVel() < currentCar.getMaxV():
                    currentCar.updateAcc(currentCar.getMaxA())
                currentCar.updateVel()
                currentCar.updatePos()
                currentCar.draw_car()
                
                current = carList.getNext(i+1)
                #Need to have the currentCar compare its location to prev and next cars

            pygame.display.flip()

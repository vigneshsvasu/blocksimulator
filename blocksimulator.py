## Should have run:
# !pip install pygame
# !pip install pymunk
import random
import time
import pygame
import numpy
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
# Some general variables -- you don't need to change any of these
N_BLOCKS = 6 # How many blocks will fall?
BLOCK_SIZE = 20 # How big are the blocks?
deltaY = 35 # How far spaced out vertically are they?
xSD = 30.0 # What is the SD for their x-locations?
FPS = 30. # how many frames per second do we run?
BLOCK_MASS = 1.0
BLOCK_FRICTION = 1.0
FLOOR = 100
RUN_TIME = 20.0 # Time in seconds that we will run a simulation for -- this was increased to be
sure we run for long enough across platforms
STEPS_PER_FRAME = 5.0 # Do not change this
WIDTH = 600 # Screen dimensions -- don't change
HEIGHT = 600
class BlockTower:
# Implement a class to show/simulate blocks falling via pymunk
# Note: this code has been modified from the pymunk pyramid demo
    def __init__(self, positions):
# The intializer takes a list of x-positions for blocks; their height is set
# by the code here.
        assert(len(positions)==N_BLOCKS) # can't give more than N_BLOCKS since we need to draw them
        self.positions = positions # store the positions of our blocks
# Set up some pygame stuff
        self.running = True
        self.physics_running = False
        self.start_time = 0
        self.drawing = True
        self.w, self.h = WIDTH,HEIGHT
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
### Init pymunk and create space
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.space.sleep_time_threshold = 0.3
        self.floor = pymunk.Segment(self.space.static_body, (0, FLOOR), (self.w,FLOOR), 1.0)
        self.floor.friction = 1.0
        self.space.add(self.floor)
# Draw each block and add it to the physics
        for i in range(N_BLOCKS):
            points = [(-BLOCK_SIZE, -BLOCK_SIZE), (-BLOCK_SIZE, BLOCK_SIZE),
(BLOCK_SIZE,BLOCK_SIZE), (BLOCK_SIZE, -BLOCK_SIZE)]
            moment = pymunk.moment_for_poly(BLOCK_MASS, points, (0,0))
            body = pymunk.Body(BLOCK_MASS, moment)
            xpos = self.positions[i]
            ypos = FLOOR + (2*i+1) * deltaY
            body.position = Vec2d(xpos,ypos)
            shape = pymunk.Poly(body, points)

            if(i == N_BLOCKS-1): # color the top
                shape.color = (1,0,0,1)
                self.target_block = shape # store the top one we are tracking
                shape.friction = 1
                self.space.add(body,shape)
### draw options for drawing
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
def change_x_y(self, new_x):
# This is what you should call instead of initializing new objects
# this resets the y-positions and puts the blocks at the specified x positions
    self.space.remove(self.space.bodies)
    self.__init__(new_x)

def is_black_block_on_floor(self):
# Returns true or false depending on whether the black block is on the bottom
    col = self.target_block.shapes_collide(self.floor) # this resturns a ContactPointSet
    return len(col.points) > 0
def simulate(self):
# Just run a simulation, returning whether after 10s the black block hits the floor
    for s in range(int(FPS*5*RUN_TIME)): # run for 10s
        self.space.step(1.0 / FPS / STEPS_PER_FRAME) # run this many steps
    return self.is_black_block_on_floor()

def draw(self, file="screenshot.jpg"):
### This gets called to draw the scene
### Clear the screen
    self.screen.fill(THECOLORS["white"])
### Draw space with our given options
    self.space.debug_draw(self.draw_options)
## Save to a file
    pygame.image.save(self.screen, file)

if __name__ == "__main__":
# Set up a null pygame video driver

import os
os.environ['SDL_VIDEODRIVER']='dummy'
from IPython.display import Image # required for showing the image
positions = [numpy.random.normal(WIDTH/2, xSD) for _ in range(N_BLOCKS)]
# set up a block tower
demo2 = BlockTower(positions) # make a block tower
demo2.draw() # draw it -- this saves it as a file called screenshot.jpg, defaultly
# show the image
display(Image(filename='screenshot.jpg') )
# gather input (should be yes/no)
guess = input()
# print the simulation result
print(demo2.simulate())
import csv
# Opening the file in write mode; test_df2.csv is the file we are creating
with open('predictions.csv', mode='w') as csvfile:
wr = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
wr.writerows([["1", "2", "3", "4", "5", "6", "pred-truth","guess"]])
list = []
for i in range(0, 200):
    row = []
    row.append([numpy.random.normal(WIDTH/2, xSD) for _ in range(N_BLOCKS)])
    obj = BlockTower(row[0])
    print("type y/n")
    guess = input()
    a = obj.simulate()
    print(a)
    print("1 run over")
    row[0].append(a)
    row[0].append(guess)
    print(row)
    with open('predictions.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerows(row)
    list.append(row)
    print(list)

import pandas as pd
pred = pd.read_csv("predictions.csv")
Pred.iloc[[0]]
pred.iloc[0, 1]
pred.iloc[0, 0:6]
pred.iloc[0, 6]
Pred.dtypes
pred.astype('str')
#Adding randomness in the positions
for i in range(0, 1):
    for j in range(0, 10):
            position = pred.iloc[0, 0:6] + [numpy.random.normal(0, 10) for _ in range(6)]
            print([position])
            a = BlockTower(position).simulate()
            print(a)

modelprob = [] #200 model averages
rightprediction = 0
for i in range(0, 200):
    for j in range(0, 100): #play 200 times/starting points
        position = pred.iloc[0, 0:6] + [numpy.random.normal(0, 10) for _ in range(6)]
        print([position])

a = BlockTower(position).simulate() #BlockTower.simulate() - generate predictions from a noisy physics model.
if a == True:
    rightprediction += 1
    modelprob.append(rightprediction/100)
    
ten = []
twenty = []
thirty = []
forty = []
fifty = []
sixty = []
seventy = []
eighty = []
ninety = []
hundred = []

for i in range(len(modelprob)):
    if modelprob[i] > 0 and modelprob[i] < .10:
        ten.append(i)
    elif modelprob[i] > .10 and modelprob[i] < .20:
        twenty.append(i)
    elif modelprob[i] > .20 and modelprob[i] < .30:
        thirty.append(i)
    elif modelprob[i] > .30 and modelprob[i] < .40:
        forty.append(i)
    elif modelprob[i] > .40 and modelprob[i] < .50:
        fifty.append(i)
    elif modelprob[i] > .50 and modelprob[i] < .60:
        sixty.append(i)
    elif modelprob[i] > .60 and modelprob[i] < .70:
        seventy.append(i)
    elif modelprob[i] > .70 and modelprob[i] < .80:
        eighty.append(i)
    elif modelprob[i] > .80 and modelprob[i] < .90:
        ninety.append(i)
    else:
        hundred.append(i)

accurate = 0
ourprediction = prediction(i) #pulling our prediction from csv file
for i in range(len(ten)):
    if ourprediction == ten[i]:
        accurate +=1
        i += 1
        tensaccuracy = accurate/len(ten)


with open("extra_credit.csv", "w") as csvfile:
wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
wr.writerows([["1","2","3","4","5","6","pred-truth"]])

for i in range(0, 200):
    lst = []
    lst.append([numpy.random.normal(WIDTH/2, xSD) for _ in range(N_BLOCKS)])
    obj = BlockTower(row[0])
    a = obj.simulate()
    lst[0].append(a)

with open('extra_credit.csv', 'a', newline='') as csvfile:
writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
writer.writerows(lst)

def probability(data, index):
    hits = 0
    for i in range(0, 100):
        position = data.iloc[index][0:6] + [numpy.random.normal(0, 10) for each in range(6)]
        b = BlockTower(position).simulate()
        if b:
            hits +=1
            probability = hits/100
    return probability

def updatecsv():
    probabilities = []
for i in range(0,200):
    prob = probability(EC, i)
    probabilities.append(prob)
    print(probabilities)
files = 'extra_credit.csv'
dataf = pd.read_csv(files)
dataf = dataf.convert_objects(convert_numeric=True)
dataf.insert(7, 'probability', probabilities)
dataf.to_csv(files)
updatecsv()
extra = pd.read_csv("extra_credit.csv")
extra.iloc[0]
g_rows = []

for i in range(0, 200):
    prob = extra.iloc[i][8]

if 0.45 <= prob <= 0.55:
    g_rows.append(i)
    print(g_rows)
extra.iloc[0][0:7]

for each in range(len(g_rows)):
    pos = list(extra.iloc[each][1:7])
    obj = BlockTower(pos)
    a = obj.run_person()
    print(a)

#!/usr/bin/env python3
import pymunkoptions
pymunkoptions.options["debug"] = False
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import pygame_util
import pymunk.util
from pymunk import Vec2d
from math import *
from walker import walker

class simulation():
    def __init__(self, scr_w=600, scr_h=600, angle=pi / 27, gravity=200, show=True):

        # Window size
        self.scr_w = scr_w
        self.scr_h = scr_h

        # Graphics initialization (if show)
        self.show = show
        if self.show:
            pygame.init()
            self.screen = pygame.display.set_mode((self.scr_w, self.scr_h))
            self.clock = pygame.time.Clock()

        # Create the space
        self.space = pymunk.Space()
        self.space.gravity = (0, -gravity)

        # Create the floor
        self._create_floor(angle)

    def _create_floor(self, angle):

        # Create the floor
        body = pymunk.Body()
        body.position = self.scr_w / 2, self.scr_h / 4
        v = [(-self.scr_w, -(self.scr_h / 2) * sin(angle)),
             (self.scr_w, (self.scr_h / 2) * sin(angle)),
             (self.scr_w, -self.scr_h / 2),
             (-self.scr_w, -self.scr_h / 2)]
        floor = pymunk.Poly(body, v)
        floor.friction = 1.0
        floor.elasticity = 0.4
        self.space.add(floor)

    def step(self, delta):

        # Simulation step
        self.space.step(delta)

        # Draw stuff (if show)
        if self.show:
            self.screen.fill(THECOLORS['black'])
            pygame_util.draw_space(self.screen, self.space)
            pygame.display.flip()
            self.clock.tick(1 / delta)

    def start(self, chromosome):

        score = 0;

        #Create the walker
        robot = walker(self.space, [chromosome[0], chromosome[1]], chromosome[2], chromosome[3], chromosome[4], chromosome[5], chromosome[6], chromosome[7], chromosome[8])

        iteration = 0

        while True:

            #Perform one step
            self.step(0.02)

            #When the walker reaches its end
            if (robot.rul.body.kinetic_energy + robot.lul.body.kinetic_energy) < 20 or iteration > 5000:

                return (600 - robot.lul.body.position[0])

            iteration = iteration + 1
        #    lastPosition = robot.lul.body.position[0]

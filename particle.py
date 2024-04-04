import pygame
import numpy as np
from globals import *
from collections import deque


class Particle:
    def __init__ (self, mass, x_position, y_position, x_velocity, y_velocity, color, radio=None):
        self.mass = mass
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.color = color
        self.trail = deque(maxlen=1500)  # Crear un deque con una longitud máxima de 100 elementos
        if radio == None:
            self.radio = self.mass / 10
            #self.trail = []
        else:
            self.radio = radio

    
    def draw_particle(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_position, self.y_position), self.radio)

    def update_position(self, center_of_mass_x, center_of_mass_y):
        self.x_position = self.x_position + self.x_velocity -center_of_mass_x + window_width/2
        self.y_position = self.y_position + self.y_velocity -center_of_mass_y + window_height/2

    def check_border(self):
        if self.x_position >= window_width - self.radio or self.x_position <= self.radio:
            self.x_velocity = - self.x_velocity
        elif self.y_position >= window_height - self.radio or self.y_position <= self.radio:
            self.y_velocity = - self.y_velocity

    def update_velocity(self, delta_t, other_particle):


        x_distance = self.x_position - other_particle.x_position
        y_distance = self.y_position - other_particle.y_position
        distance = np.sqrt((x_distance)**2 + (y_distance)**2)

        acceleration = G * other_particle.mass / distance**2

        sine = (other_particle.y_position - self.y_position) / distance
        cosine = (other_particle.x_position - self.x_position) / distance

        self.x_velocity = self.x_velocity + acceleration * cosine * delta_t
        self.y_velocity = self.y_velocity + acceleration * sine * delta_t
            

    
    def draw_trail(self, screen):
        self.trail.append([self.x_position, self.y_position])
        for row in self.trail:
            pygame.draw.circle(screen, self.color, (row[0], row[1]), 1)



        
    

        
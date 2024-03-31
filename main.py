import numpy as np
import pygame
from globals import *
from particle import *


width, height = 800, 800 # Number of pixels of the game window
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)


pygame.init()

run = True
clock = pygame.time.Clock() # For controlling the fps
screen = pygame.display.set_mode((width, height))

n = 3
particle_0 = Particle(300, width/2, height/2, 0, 0, WHITE, 20)
particle_1 = Particle(5, width/2 - 1 * width / 3, height/2 + 100, 0, 1, RED, 10)
particle_2 = Particle(20, width/2 + 1 * width / 3, height/2 + 1*height/3, 1, -1, BLUE, 10)

particles_vector = []
for i in range(n):
    nombre_partícula = f'particle_{i}'
    particles_vector.append(globals()[nombre_partícula])

while run:
    clock.tick(100)
    pygame.display.set_caption("Simulation - FPS: {}".format(int(clock.get_fps())))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            '''
            Quit the game.
            '''
            run = False


    for particle1 in particles_vector:
        particle1.draw_particle(screen)
        particle1.update_position()
        particle1.draw_trail(screen)
        particle1.check_border()

        for particle2 in particles_vector:
            if particle1 != particle2:
                particle1.update_velocity(clock.get_fps(), particle2)
        

    """ particle_0.draw_particle(screen)
    particle_1.draw_particle(screen)
    particle_2.draw_particle(screen)

    #particle_a.update_position()
    particle_1.update_position()

    particle_0.update_velocity(clock.get_fps(), particle_1)
    particle_1.update_velocity(clock.get_fps(), particle_0)
    
    particle_1.draw_trail(screen)
     """


    # Update screen
    pygame.display.flip()

    # Clean screen
    screen.fill(BLACK)

pygame.quit()
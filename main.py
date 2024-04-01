import numpy as np
import pygame
from globals import *
from particle import *
from update_window import *


pygame.init()

run = True
clock = pygame.time.Clock() # For controlling the fps
screen = pygame.display.set_mode((width, height))

n = 2
particle_0 = Particle(50, 20, 20, 0, 0.5, WHITE)
particle_1 = Particle(100, 120, 120, 0.5, 0, RED)
#particle_2 = Particle(70, 500, 350, -2, 0, BLUE)
#particle_3 = Particle(150, 260, 600, 1, 3, GREEN)



particles_vector = []
for i in range(n):
    nombre_partícula = f'particle_{i}'
    particles_vector.append(globals()[nombre_partícula])

while run:
    clock.tick(60)
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
                particle1.update_velocity(1/100, particle2)
        


    # Update screen
    pygame.display.flip()

    # Clean screen
    screen.fill(BLACK)

pygame.quit()
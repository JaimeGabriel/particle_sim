import numpy as np
import pygame
from globals import *
from particle import *



pygame.init()

run = True
clock = pygame.time.Clock() # For controlling the fps
screen = pygame.display.set_mode((window_width, window_height))

n = 3 # Number of particles
particle_0 = Particle(70, 20, 20, 0, 0.05, WHITE)
particle_1 = Particle(70, 120, 200, 0.05, 0, RED)
particle_2 = Particle(30, 550, 350, 0, 0, BLUE)
#particle_3 = Particle(10, 260, 600, 0, 0.2, GREEN)

particles_vector = []
for i in range(n):
    nombre_partícula = f'particle_{i}'
    particles_vector.append(globals()[nombre_partícula])
   


while run:
    clock.tick(600)
    pygame.display.set_caption("Simulation - FPS: {}".format(int(clock.get_fps())))
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            '''
            Quit the game.
            '''
            run = False

    # Aux variables
    mass_times_x = 0
    mass_times_y = 0
    total_mass = 0

    for particle1 in particles_vector:
        mass_times_x += particle1.mass * particle1.x_position
        mass_times_y += particle1.mass * particle1.y_position
        total_mass += particle1.mass


    center_of_mass_x = mass_times_x / total_mass
    center_of_mass_y = mass_times_y / total_mass
    #center_of_mass = Particle(50, center_of_mass_x, center_of_mass_y, 0, 0, GREEN)
    #center_of_mass.draw_particle(screen)

    for particle1 in particles_vector:

        particle1.draw_particle(screen)
        particle1.update_position(center_of_mass_x, center_of_mass_y)
        particle1.draw_trail(screen)
        particle1.check_border()

        for particle2 in particles_vector:
            if particle1 != particle2:
                particle1.update_velocity(1/30, particle2)


    # Update screen
    pygame.display.flip()


    # Clean screen
    screen.fill(BLACK)



    
pygame.quit()
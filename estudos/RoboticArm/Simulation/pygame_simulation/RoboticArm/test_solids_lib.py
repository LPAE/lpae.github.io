import pygame
from pygame.locals import *

from Solids import *

from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(50, (display[0]/display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)

    cube_1 = Cube(color=(1, 0, 0))
    cube_2 = Cube(color=(0, 1, 0))
    cube_3 = Cube(color=(0, 0, 1))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        cube_1.draw()
        cube_1.axis = [1, 1, 1]
        cube_1.theta_degree += 10

        cube_2.draw()
        cube_2.axis = [0, 1, 0]
        cube_2.theta_degree += 10

        cube_3.draw()
        cube_3.axis = [0, -1, -1]
        cube_3.theta_degree += 10

        pygame.display.flip()

        pygame.time.wait(1)


main()
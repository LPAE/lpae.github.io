import pygame
import numpy as np
from Parts import MasterPart, SlavePart
import time
import threading
import os
import sys


class PgScreen:
    def __init__(self,
                 screen_size=(800, 600),
                 clock_rate=30,
                 pixel_meter=100):

        self.screen_size = screen_size
        self.clock_rate = clock_rate
        self.pixel_meter = pixel_meter

        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        self.main_state = 'start_state'
        self.close_app = False
        self.clock = pygame.time.Clock()

        self.part_list = []

        self.part_list.append(MasterPart(None,
                                         screen_size,
                                         None,
                                         'master',
                                         init_ref=[400, 300, 0],
                                         init_theta=0,
                                         init_phi=np.pi/5,
                                         init_R=150))

        self.part_list.append(SlavePart(self.part_list[-1],
                                        None,
                                        screen_size,
                                        None,
                                        'slave',
                                        init_phi=2*np.pi/3,
                                        init_R=200))

        self.part_list.append(SlavePart(self.part_list[-1],
                                        None,
                                        screen_size,
                                        None,
                                        'slave',
                                        init_phi=np.pi/2,
                                        init_R=50))

        main_thread = threading.Thread(target=self.main_loop)
        main_thread.start()

    def check_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_app = True

        if self.main_state == 'start_state':
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                self.main_state = 'run_state'

        elif self.main_state == 'run_state':
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                self.part_list[1].master.phi -= 0.1
                self.part_list[1].update_ref()
                self.part_list[2].update_ref()
            if pressed[pygame.K_DOWN]:
                self.part_list[1].master.phi += 0.1
                self.part_list[1].update_ref()
                self.part_list[2].update_ref()
            if pressed[pygame.K_LEFT]:
                self.part_list[1].master.theta -= 0.1
                self.part_list[1].update_ref()
                self.part_list[2].update_ref()
            if pressed[pygame.K_RIGHT]:
                self.part_list[1].master.theta += 0.1
                self.part_list[1].update_ref()
                self.part_list[2].update_ref()
            if pressed[pygame.K_w]:
                self.part_list[1].phi -= 0.1
                self.part_list[2].update_ref()
            if pressed[pygame.K_s]:
                self.part_list[1].phi += 0.1
                self.part_list[2].update_ref()

        elif self.main_state == 'restart_state':
            os.execl(sys.executable, sys.executable, *sys.argv)

    def main_loop(self):
        while not self.close_app:
            self.check_key_events()
            if self.main_state == 'run_state':
                pass

            self.screen_update()
            time.sleep(1 / self.clock_rate)

    def screen_update(self):
        self.screen.fill((0, 0, 0))

        if self.main_state == 'start_state':
            pass

        elif self.main_state == 'run_state':
            self.screen.fill((0, 0, 0))
            for part in self.part_list:
                # ------------------------------------------------------------------------------------------------------
                pygame.draw.circle(self.screen,
                                   (225, 0, 0),
                                   [part.ref[0]//3, (3*self.screen_size[1])//4 - part.ref[2]//3],
                                   5)

                pygame.draw.aaline(self.screen,
                                   (255, 0, 0),
                                   [part.ref[0]//3, (3*self.screen_size[1])//4 - part.ref[2]//3],
                                   [part.x//3, (3*self.screen_size[1])//4 - part.z//3],
                                   True)
                # ------------------------------------------------------------------------------------------------------
                pygame.draw.circle(self.screen,
                                   (225, 0, 0),
                                   [(self.screen_size[0]+part.ref[1])//3, (3*self.screen_size[1])//4 - part.ref[2]//3],
                                   5)

                pygame.draw.aaline(self.screen,
                                   (255, 0, 0),
                                   [(self.screen_size[0]+part.ref[1])//3, (3*self.screen_size[1])//4 - part.ref[2]//3],
                                   [(self.screen_size[0]+part.y)//3, (3*self.screen_size[1])//4 - part.z//3],
                                   True)
                # ------------------------------------------------------------------------------------------------------
                pygame.draw.circle(self.screen,
                                   (225, 0, 0),
                                   [(self.screen_size[0]+part.ref[0])//2, (3*self.screen_size[1])//4 - part.ref[1]//2],
                                   5)

                pygame.draw.aaline(self.screen,
                                   (255, 0, 0),
                                   [(self.screen_size[0]+part.ref[0])//2, (3*self.screen_size[1])//4 - part.ref[1]//2],
                                   [(self.screen_size[0]+part.x)//2, (3*self.screen_size[1])//4 - part.y//2],
                                   True)
        pygame.display.flip()


# ======================================================================================================================
# screen_1 = PgScreen(screen_size=(1024, 768))
screen_1 = PgScreen(screen_size=(1000, 500))


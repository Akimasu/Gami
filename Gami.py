import pygame
from pygame.locals import *
from pygame import *
import time
import random
import math
# import numpy as np
# import sympy as sy
import sys

# sys.setrecursionlimit(100000)

# Setting
pygame.init()
SCREEN_WIDTH_Complete, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH_Complete, SCREEN_HEIGHT))  # , FULLSCREEN
SCREEN_WIDTH = SCREEN_WIDTH_Complete - 150
SCREEN_WIDTH_Complete = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
pygame.display.set_caption('Extra Gamily')
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


class player:
    def __init__(self, rad):
        self.rad = rad


def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    # return math.hypot(dx, dy)
    if (dx ** 2 + dy ** 2) <= 0:
        return 0
    else:
        return abs(dx ** 2 + dy ** 2) ** (1 / 2)


class enemy:
    def __init__(self, vel_x, vel_y, rad=10):
        self.pox = random.randint(0, 800)
        self.poy = random.randint(0, 600)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.rad = rad
        self.speed = (vel_x ** 2 + vel_y ** 2) ** (1 / 2)

    def run(self):
        self.pox += self.vel_x
        self.poy += self.vel_y

        if self.pox >= 800 or self.pox <= 0:
            self.vel_x = -self.vel_x
        if self.poy >= 600 or self.poy <= 0:
            self.vel_y = -self.vel_y

    def rebound(self, p1x, p1y, x, y, lastx, lasty, counter):
        hx = (x + lastx) / 2
        hy = (y + lasty) / 2
        counter += 1
        if counter <= 700:
            if distance(p1x, p1y, hx, hy) <= p1.rad + self.rad - 5:
                self.rebound(p1x, p1y, x, y, hx, hy, counter)
            elif distance(p1x, p1y, hx, hy) >= p1.rad + self.rad + 5:
                self.rebound(p1x, p1y, hx, hy, lastx, lasty, counter)
            else:
                # p_x, p_y = hx, hy
                ortsvektor_x = p1x - hx
                ortsvektor_y = p1y - hy
                # t = sy.Symbol('t')
                # lot_x = hx+t*(p1x - hx)
                # lot_y = hy+t*(p1y - hy)
                # t_berechnet = sy.solve(sy.Eq((hx+t*(p1x - hx)-lastx)*ortsvektor_x+(hy+t*(p1y - hy)-lasty)*ortsvektor_y, 0))
                if (-p1x * (p1x - hx) + hx * (p1x - hx) - p1y * (p1y - hy) + hy * (p1y - hy)) != 0:
                    t_berechnet = ((p1x ** 2) + p1x * lastx - p1x * hx + lastx * hx + ( p1y ** 2) + p1y * lasty - p1y * hy + lastx * hy) / (-p1x * (p1x - hx) + hx * (p1x - hx) - p1y * (p1y - hy) + hy * (p1y - hy))
                else:
                    t_berechnet = 0
                # t_berechnet = (p_x * ortsvektor_x + p_y * ortsvektor_y - hx * ortsvektor_x - hy *ortsvektor_y)/((p1x - hx) * ortsvektor_x + (p1y - hy) * ortsvektor_y)
                lot_berechnet_x = hx + t_berechnet * ortsvektor_x
                lot_berechnet_y = hy + t_berechnet * ortsvektor_y
                newx = (lot_berechnet_x - lastx) + lot_berechnet_x
                newy = (lot_berechnet_y - lasty) + lot_berechnet_y
                vel_x_part = newx - hx
                vel_y_part = newy - hy
                if abs((vel_x_part ** 2 + vel_y_part ** 2)) <= 0:
                    res_vel = 0
                else:
                    res_vel = abs((vel_x_part ** 2 + vel_y_part ** 2)) ** (1 / 2)
                vel_ratio = res_vel / self.speed
                if vel_ratio != 0:
                    self.vel_x = vel_x_part / vel_ratio
                    self.vel_y = vel_y_part / vel_ratio
                else:
                    self.vel_x = vel_x
                    self.vel_y = vel_y
        else:
            # p_x, p_y = hx, hy
            ortsvektor_x = p1x - hx
            ortsvektor_y = p1y - hy
            # t = sy.Symbol('t')
            # lot_x = hx+t*(p1x - hx)
            # lot_y = hy+t*(p1y - hy)
            # t_berechnet = sy.solve(sy.Eq((hx+t*(p1x - hx)-lastx)*ortsvektor_x+(hy+t*(p1y - hy)-lasty)*ortsvektor_y, 0))
            if (-p1x * (p1x - hx) + hx * (p1x - hx) - p1y * (p1y - hy) + hy * (p1y - hy)) != 0:
                t_berechnet = ((p1x ** 2) + p1x * lastx - p1x * hx + lastx * hx + (
                            p1y ** 2) + p1y * lasty - p1y * hy + lastx * hy) / (
                                          -p1x * (p1x - hx) + hx * (p1x - hx) - p1y * (p1y - hy) + hy * (p1y - hy))
            else:
                t_berechnet = 0
            # t_berechnet = (p_x * ortsvektor_x + p_y * ortsvektor_y - hx * ortsvektor_x - hy *ortsvektor_y)/((p1x - hx) * ortsvektor_x + (p1y - hy) * ortsvektor_y)
            lot_berechnet_x = hx + t_berechnet * ortsvektor_x
            lot_berechnet_y = hy + t_berechnet * ortsvektor_y
            newx = (lot_berechnet_x - lastx) + lot_berechnet_x
            newy = (lot_berechnet_y - lasty) + lot_berechnet_y
            vel_x_part = newx - hx
            vel_y_part = newy - hy
            if abs((vel_x_part ** 2 + vel_y_part ** 2)) <= 0:
                res_vel = 0
            else:
                res_vel = abs((vel_x_part ** 2 + vel_y_part ** 2)) ** (1 / 2)
            vel_ratio = res_vel / self.speed
            if vel_ratio != 0:
                self.vel_x = vel_x_part / vel_ratio
                self.vel_y = vel_y_part / vel_ratio
            else:
                self.vel_x = vel_x
                self.vel_y = vel_y

    def goal(self):
        if 350 <= self.pox <= 450 and self.poy <= 4:
            down = True
            return down
        if 350 <= self.pox <= 450 and self.poy >= 596:
            down = True
            return down
        if 250 <= self.poy <= 350 and self.pox <= 4:
            down = True
            return down
        if 250 <= self.poy <= 350 and self.pox >= 796:
            down = True
            return down

    def draw(self):
        draw.circle(screen, (0, 255, 0,), (int(self.pox), int(self.poy)), self.rad)


list = []
for i in range(0, 10):
    vel_x = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    vel_y = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    speed = abs(vel_x ** 2 + vel_y ** 2) ** (1 / 2)
    list.append(enemy(vel_x, vel_y))

p1 = player(30)


def start():
    gametime = 0

    while True:
        # Set clock and measure time in seconds
        mselapsed = clock.tick(100)  # fps set on 60 frames for secondy
        gametime += mselapsed  # Count While cycles to track time
        time_passed = round(gametime / 1000, 0)  # save time in seconds (millisencondy times 1000)
        screen.fill((0, 0, 0))

        for i in list:
            i.run()
            i.draw()

        p1x, p1y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255, 0, 0), (int(p1x), int(p1y)), int(p1.rad))
        for i in list:  # Check all raspberries
            dist = distance(p1x, p1y, i.pox, i.poy)
            if dist <= p1.rad + 10:
                counter = 1
                i.rebound(p1x, p1y, i.pox, i.poy, i.pox - i.vel_x, i.poy - i.vel_y, counter)
                # p2.x -= math.sin(angle)
                # p2.y += math.cos(angle)

        for i in list:
            if i.goal():
                list.remove(i)
            if not list:
                start()

        pygame.draw.rect(screen, (0, 0, 255), (350, 0, 100, 4))
        pygame.draw.rect(screen, (0, 0, 255), (0, 250, 4, 100))
        pygame.draw.rect(screen, (0, 0, 255), (350, 596, 100, 4))
        pygame.draw.rect(screen, (0, 0, 255), (796, 250, 4, 100))

        pygame.display.update()

        # Quit game if x sign or esc is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()


start()

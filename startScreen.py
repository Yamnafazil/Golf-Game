import pygame
import os
import tkinter as tk
from tkinter import messagebox
import sys

#  here it starts
pygame.init()

# resource allocations like display images and buttons
win = pygame.display.set_mode((1080, 600))
title = pygame.image.load(os.path.join('img', 'title.png'))
back = pygame.image.load(os.path.join('img', 'back.png'))
course = pygame.image.load(os.path.join('img', 'course1.png'))
course1 = pygame.transform.scale(course, (200, 200))

font = pygame.font.SysFont('comicsansms', 24)

buttons = [[1080/2 - course1.get_width()/2, 260, course1.get_width(), course1.get_height(), 'Grassy Land']]
shopButton = []
ballObjects = []
surfaces = []

# this class contains functionality of the ball 
class ball():
    def __init__(self, color, locked, org):
        self.color = color
        self.locked = locked
        self.original = org
        self.price = 10
        self.equipped = False
        self.font = pygame.font.SysFont('comicsansms', 22)

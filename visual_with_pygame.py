# -*- coding: utf-8 -*-
import pygame
from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    QUIT,
)
import algorithms as alg
import math
pygame.init()
#Dimensions and fill color
WIDTH = int(1024 * 1.5)
HEIGHT = 860
FILL_COLOR = pygame.Color("#00cdcd")

# algorithms dict
algorithms = {"Selection Sort": alg.SelectionSort(),
              "Bubble Sort": alg.BubbleSort(), 
              "Insertion Sort": alg.InsertionSort(), 
              "Merge Sort": algorithms.MergeSort(), 
              "Quick Sort": alg.QuickSort(),
              'Heap Sort': alg.HeapSort(),
              'Random': None}
# button variables
b_width = 100
b_height = 30
gap = 10
coordinates = []
b_text = algorithms.keys()
start_pos = (10*gap,HEIGHT - (40+b_height))

#fonts

LETTER_FONT = pygame.font.SysFont('comicsans',20,)
LABEL_FONT = pygame.font.SysFont('comicsans', 40)

FPS = 60
clock = pygame.time.Clock()
running = True

for i,text in enumerate(b_text):
    x = start_pos[0] + gap * 2 + ((b_width  + gap * 2) * (i%len(b_text))) 
    y = start_pos[1] + ((i//len(b_text)) * (gap + b_width * 2))
    coordinates.append((x,y,text))
    
def write_text(*txt,font):
    for text,pos in txt:
        txt = font.render(text,1,(0,0,0))
        screen.blit(txt,pos)
    pygame.display.update()

def draw():
    temp = pygame.draw.rect(screen,(0,0,0),((0,HEIGHT-100),(WIDTH,100)),5)
    screen.fill((170,170,170),rect =temp)
    for coord in coordinates:
        temp = pygame.draw.rect(screen,(0,0,0),((coord[0],coord[1]),(b_width,b_height)),3)
        screen.fill((220,220,220),rect=temp)
        txt = LETTER_FONT.render(coord[2],1,(0,0,0))
        screen.blit(txt,(coord[0]+5,coord[1]+5))
    temp = pygame.draw.rect(screen,(0,0,0),((0,0),(WIDTH,100)),5)
    screen.fill((170,170,170),rect=temp)    
    pygame.display.update()

def check_events(): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == K_ESCAPE:
            pygame.quit()
        elif event.type == K_SPACE:
            alg.Algorithm("")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            for coord in coordinates:
                x,y,txt = coord
                distance = math.sqrt((x+b_width//2-pos[0])**2 + (y+b_height//2-pos[1])**2)
                if distance <= b_width//2:
                    # actual sorting here
                    pass
                    



screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Visualizer 1.0")


while running:
    clock.tick(FPS)
    screen.fill(FILL_COLOR)
    check_events()
    draw()
    write_text(("WELCOME  TO  THE  SORTING  VISUALIZER ",(start_pos[0],20)),("GENERATE  A  NEW  ARRAY  TO  SORT ( PRESS  SPACE )",(start_pos[0],60)),font=LABEL_FONT)
    



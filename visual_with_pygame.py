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
FILL_COLOR = (245,255,250)
RED = (255,99,71)

# algorithms dict
algorithms = {"Selection Sort": alg.SelectionSort(),
              "Bubble Sort": alg.BubbleSort(), 
              "Insertion Sort": alg.InsertionSort(), 
            #  "Merge Sort": algorithms.MergeSort(), 
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

LETTER_FONT = pygame.font.SysFont('comicsans', 20)
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
    

def draw_gui():
    temp = pygame.draw.rect(screen,(0,0,0),((0,HEIGHT-100),(WIDTH,100)),5)
    screen.fill((170,170,170),rect =temp)
    for coord in coordinates:
        temp = pygame.draw.rect(screen,(0,0,0),((coord[0],coord[1]),(b_width,b_height)),3)
        screen.fill((220,220,220),rect=temp)
        txt = LETTER_FONT.render(coord[2],1,(0,0,0))
        screen.blit(txt,(coord[0]+5,coord[1]+5))
    temp = pygame.draw.rect(screen,(0,0,0),((0,0),(WIDTH,100)),5)
    screen.fill((170,170,170),rect=temp)    
    



def draw_array(algorithm,first_swap = None, second_swap = None):
    screen.fill(FILL_COLOR)
    check_events()
    draw_gui()
    check_events()
    write_text(("WELCOME  TO  THE  SORTING  VISUALIZER ",(start_pos[0],20)),
               ("GENERATE  A  NEW  ARRAY  TO  SORT ( PRESS  SPACE )",(start_pos[0],60)),
                font=LABEL_FONT)
    write_text(("ALGORITHM  CURRENTLY  USED: {}",(1200,20)),
                ("TIME :  {}",(1200,60)),font = LETTER_FONT)
    start_x, end_x = start_pos[0], WIDTH - 100
    for i in range(len(algorithm.array)):
        color = RED
        if first_swap == algorithm.array[i]:
            color = (0,255,0)
        elif second_swap == algorithm.array[i]:
            color = (0,0,0)
        pygame.draw.rect(screen,color,((i * (end_x - start_x)/len(algorithm.array) + start_x,HEIGHT-100),(1.5,- algorithm.array[i])))
    pygame.display.update()
    
    
    
def check_events(): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.K_SPACE:
            draw_array(algorithms["Selection Sort"])
       # if event.type == pygame.MOUSEBUTTONDOWN:
        #    pos = pygame.mouse.get_pos()
         #   print(pos)
          #  for coord in coordinates:
           #     x,y,txt = coord
            #    distance = math.sqrt((x+b_width//2-pos[0])**2 + (y+b_height//2-pos[1])**2)
             #   if distance <= b_width//2:
              #     print(txt)
               #    algorithms[txt].run()
                   
                   
                   
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Visualizer 1.0")


while running:
    clock.tick(FPS)
   # screen.fill(FILL_COLOR)
    check_events()
   # draw_gui()
    write_text(("WELCOME  TO  THE  SORTING  VISUALIZER ",(start_pos[0],20)),
               ("GENERATE  A  NEW  ARRAY  TO  SORT ( PRESS  SPACE )",(start_pos[0],60)),
                font=LABEL_FONT)
    write_text(("ALGORITHM  CURRENTLY  USED: {}",(1200,20)),
                ("TIME :  {}",(1200,60)),font = LETTER_FONT)
    draw_array(algorithms["Bubble Sort"])
    alg.SelectionSort().run()
    pygame.display.update()
    
    



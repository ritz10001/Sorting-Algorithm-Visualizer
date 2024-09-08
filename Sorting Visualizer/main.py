import pygame
import random
from list_utils import ListUtils
from draw_utils import DrawUtils
from sort import Sort
import math
pygame.init() 

class Draw:
    #instance variables
    pad_x = 100
    pad_y = 150
    # grey_shades = [(128,128,128), (160,160,160), (192,192,192)]
    grey_shades = [(200,0,0), (0,200,0), (0,0,200)]
    text_font = pygame.font.SysFont('comicsans', 20)
    title_font = pygame.font.SysFont('comicsans', 30)

    def __init__(self, width, height, array):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_array_config(array)
        self.sorting_algo_name = "Bubble Sort"


    def set_array_config(self, arr):
        self.arr = arr
        self.maxima = max(arr)
        self.minima = min(arr)

        self.rect_width = int((self.width - self.pad_x) / len(arr))
        self.rect_height = math.floor((self.height - self.pad_y) / (self.maxima - self.minima)) #this is like a scale 
        self.start_x = int(self.pad_x / 2)
    
    def setAlgorithm(self, sorting_algo_name):
        self.sorting_algo_name = sorting_algo_name

    def getAlgorithm(self):
        return self.sorting_algo_name


def main():
    run = True
    clk = pygame.time.Clock()

    nums = 50
    min_val = 0
    max_val = 100

    arr = ListUtils.create_array(nums, min_val, max_val)
    draw_instance = Draw(800, 600, arr)
    isSorting = False
    
    sorting_algo = Sort.bubble_sort
    sorting_algo_generator = None

    while run:
        clk.tick(60) #Frame rate

        if isSorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                isSorting = False

        DrawUtils.draw(draw_instance)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    arr = ListUtils.create_array(nums, min_val, max_val)
                    draw_instance.set_array_config(arr)
                elif event.key == pygame.K_SPACE and isSorting == False:
                    isSorting = True
                    sorting_algo_generator = sorting_algo(draw_instance)
                elif event.key == pygame.K_SPACE and isSorting == True:
                    isSorting = False
                elif event.key == pygame.K_b and isSorting == False:
                    sorting_algo = Sort.bubble_sort
                    draw_instance.setAlgorithm("Bubble Sort")
                elif event.key == pygame.K_i and isSorting == False:
                    sorting_algo = Sort.insertion_sort
                    draw_instance.setAlgorithm("Insertion Sort")
                elif event.key == pygame.K_s and isSorting == False:
                    sorting_algo = Sort.selection_sort
                    draw_instance.setAlgorithm("Selection Sort")
                elif event.key == pygame.K_p and isSorting == False:
                    sorting_algo = Sort.bogo_sort
                    draw_instance.setAlgorithm("Bogo/Perm Sort")
                
    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random
from list_utils import ListUtils
from draw_utils import DrawUtils

pygame.init() 

class Draw:
    #instance variables
    pad_x = 100
    pad_y = 150
    grey_shades = [(128,128,128), (160,160,160), (192,192,192)]
    text_font = pygame.font.SysFont('comicsans', 20)
    title_font = pygame.font.SysFont('comicsans', 30)

    def __init__(self, width, height, array):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_array_config(array)


    def set_array_config(self, arr):
        self.arr = arr
        self.maxima = max(arr)
        self.minima = min(arr)

        self.rect_width = int((self.width - self.pad_x) / len(arr))
        self.rect_height = int((self.height - self.pad_y) / (self.maxima - self.minima)) #this is like a scale 
        self.start_x = int(self.pad_x / 2)


def main():
    run = True
    clk = pygame.time.Clock()

    nums = 50
    min_val = 0
    max_val = 100

    arr = ListUtils.create_array(nums, min_val, max_val)
    draw_instance = Draw(800, 600, arr)
    isSorting = False

    while run:
        clk.tick(60) #Frame rate

        DrawUtils.draw(DrawUtils, draw_instance)

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


    pygame.quit()

if __name__ == "__main__":
    main()






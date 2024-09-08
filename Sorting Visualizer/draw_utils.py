import pygame

class DrawUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def draw(self, draw_instance):
        draw_instance.window.fill((255,255,255))

        algo_render = draw_instance.title_font.render("{}".format("Bubble Sort"), 1, (0,255,0))
        draw_instance.window.blit(algo_render, (draw_instance.width / 2 - algo_render.get_width() / 2, 5))

        title_render = draw_instance.title_font.render("Space - Start Sorting | Bksp - Reset", 1, (255,0,0))
        draw_instance.window.blit(title_render, (draw_instance.width / 2 - title_render.get_width() / 2, 45))

        sort_render = draw_instance.text_font.render("Sort", 1, (0,0,0))
        draw_instance.window.blit(sort_render, (draw_instance.width / 2 - sort_render.get_width() / 2, 90))

        self.draw_list(draw_instance)
        pygame.display.update()

    @staticmethod
    def draw_list(draw_instance, color_posn = {}, clear = False):
        arr = draw_instance.arr

        if clear:
            clear_rect = (int(draw_instance.pad_x/2), draw_instance.pad_y, draw_instance.width - draw_instance.pad_x, draw_instance.height - draw_instance.pad_y)
            pygame.draw.rect(draw_instance.window, (255,255,255), clear_rect)

        for i, num in enumerate(arr):
            x = draw_instance.start_x + i * draw_instance.rect_width
            y = draw_instance.height - (num - draw_instance.minima) * draw_instance.rect_height
            
            color = draw_instance.grey_shades[i % 3]

            if i in color_posn:
                color = color_posn[i]

            pygame.draw.rect(draw_instance.window, color, (x, y, draw_instance.rect_width, draw_instance.height))
        
        if clear:
            pygame.display.update()

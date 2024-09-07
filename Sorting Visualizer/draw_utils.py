import pygame

class DrawUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def draw(self, draw_instance):
        draw_instance.window.fill((255,255,255))

        title_render = draw_instance.title_font.render("Space - Start Sorting | Bksp - Reset", 1, (0,0,0))
        draw_instance.window.blit(title_render, (draw_instance.width / 2 - title_render.get_width() / 2, 5))

        sort_render = draw_instance.text_font.render("Sort", 1, (0,0,0))
        draw_instance.window.blit(sort_render, (draw_instance.width / 2 - sort_render.get_width() / 2, 50))

        self.draw_list(draw_instance)
        pygame.display.update()

    @staticmethod
    def draw_list(draw_instance):
        arr = draw_instance.arr
        for i, num in enumerate(arr):
            x = draw_instance.start_x + i * draw_instance.rect_width
            y = draw_instance.height - (num - draw_instance.minima) * draw_instance.rect_height

            color = draw_instance.grey_shades[i % 3]

            pygame.draw.rect(draw_instance.window, color, (x, y, draw_instance.rect_width, draw_instance.height))

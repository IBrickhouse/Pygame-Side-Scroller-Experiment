import pygame
screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("Side Scroller")

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            exit()
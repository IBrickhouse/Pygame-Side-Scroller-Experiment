import pygame
screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("Side Scroller")

def menu():
    image = pygame.image.load('assets/menu.png')
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(200,228):
                    game()

def game():
    image = pygame.image.load('assets/level1.png')
    image = pygame.transform.scale(image, (640,480))
    bgx = 0

    player = pygame.image.load('assets/boy.png')
    player = pygame.transform.rotozoom(player, 0, 0.2)
    player_y = 325
    gravity = 1
    jumpcount = 0
    jump= 0 
    while True:
        screen.blit(image, (bgx-640, 0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))

        bgx = bgx - 1
        if bgx <= -640:
            bgx = 0

        screen.blit(player, (50, player_y))
        if player_y < 325:
            player_y += gravity

        if jump == 1:
            player_y = player_y - 4
            jumpcount += 1
            if jumpcount > 40:
                 jumpcount = 0
                 jump=0

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                print('jump')
                jump = 1
menu()
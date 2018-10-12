import pygame
# import os

pygame.init()

screen = pygame.display.set_mode((480, 700))

# print(os.path.exists('./images/background.png'))

bg = pygame.image.load("./images/background.png")

screen.blit(bg, (100, 100))



pygame.display.update()

# while True:
#     pass

pygame.quit()
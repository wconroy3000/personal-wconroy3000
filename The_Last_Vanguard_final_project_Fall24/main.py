import pygame
from src.controller import Controller
#import your controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

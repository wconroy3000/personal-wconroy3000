import pygame

class GameOver:
    def __init__(self, x, y):
        '''
        Intializes the data from the gameover screen 
        args:
            x: int - the x value for the game over message to be displayed
            y: int - the y value for the game over message to be dsiplayed
        '''
        self.x = x
        self.y = y
        self.game_over_font = pygame.font.Font(None, 120)
        self.color = (255,255,255)
        
    def draw(self, screen):
        '''Allows the gameover message to be displayed on the screen
        args:
            screen: str - the screen to be displayed on
        '''
        text  = 'Game Over'
        text_surface = self.game_over_font.render(text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))
import pygame

class Level:
    def __init__(self, level, x, y):
        '''
        Intializes the data needed for the level to display properly
        args:
            level: int - the current level
            x: int - the x value of where level is to be displayed
            y: int - the y value of where level is to be displayed
        '''
        self.level = level
        self.x = x
        self.y = y
        self.level_font = pygame.font.Font(None, 50) 
        self.color = (255,255,255)
    
    def increase_level(self):
        '''
        Increases the level by 1
        '''
        self.level += 1
        
        
    def draw(self, screen):
        '''
        Allows the level to be drawn on the display
        args:
            screen: str - the screen the level will be displayed on
        '''
        level_value = f'Level: {self.level}'
        text_surface = self.level_font.render(level_value, True, self.color)
        screen.blit(text_surface, (self.x, self.y))
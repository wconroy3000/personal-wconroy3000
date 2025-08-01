import pygame

class View:
    def __init__(self, screen):
        '''
        Intializes the data needed for View to display information
        args:
            screen: str - brings in the screen from the controller
        '''
        self.screen = screen
        self.background = pygame.image.load("assets/animations/background4.jpg")

    def draw_game(self, player, enemy, level, sprites):
        '''
        Draws the characters and information on the screen
        args:
            player: str - the player class from controller
            enemy: str - the enemy class from the controller
            level: str - the level class from the controller
            sprites: str - the sprites necessary to be displayed
        '''
        self.screen.blit(self.background, (0, 0))
        player.draw_health(self.screen)
        enemy.draw_health(self.screen)
        sprites.draw(self.screen)
        level.draw(self.screen)

    def draw_game_over(self, game_over):
        '''
        Draws the game over on the screen
        args:
            game_over: str - the gameover class from the controller
        '''
        game_over.draw(self.screen)
    
    

    
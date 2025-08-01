from src.player import Player
from src.enemy import Enemy
from src.level import Level
from src.gameover import GameOver
from src.highscore import Highscore
from src.view import View
import pygame

class Controller:
    def __init__(self):
        '''
        Intializes the data needed for the game to open
        '''
        pygame.init()
        pygame.display.set_caption("The Last Vanguard")
        pygame.mixer.init()
        
        self.screen_width = 988
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.highscore = Highscore()
        self.view = View(self.screen)
        
        
        self.player = Player(100, 0)
        self.enemy = Enemy(425,0)
        self.level = Level(1,430,20)
        self.game_over = GameOver(270,140)
        self.respawn_time = None

        self.mysprites = pygame.sprite.Group()
        self.mysprites.add(self.player)
        self.mysprites.add(self.enemy)
        self.is_player_dead = False
        
        

    def mainloop(self):
        '''
        Opens the game and plays out the events for the game
        '''
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:  
                        self.player.set_attack("slash")
                    elif event.key == pygame.K_k:  
                        self.player.set_attack("overhead")
                    elif event.key == pygame.K_l: 
                        self.player.set_attack("upper")
            
            if self.is_player_dead == False:
                self.handle_respawn()
                    
                    

                if self.enemy.is_attacking:
                    now = pygame.time.get_ticks()
                    self.enemy.handle_attack(self.player, now)

                
                self.mysprites.update()
            
            if self.is_player_dead == False:
                self.view.draw_game(self.player, self.enemy, self.level,self.mysprites)
                self.highscore.update_highscore(self.level.level)
            else:
                self.screen.fill((0,0,0))
                self.view.draw_game_over(self.game_over)
            self.level.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)
            
    def handle_respawn(self):
        '''
        Respawns the enemy four seconds after their death and lowers their animation speed and attack timer to make them more difficult
        '''
        now = pygame.time.get_ticks()
        if self.player.hp.current_hp == 0:
            self.is_player_dead = True
        if self.enemy.is_enemy_dead and self.respawn_time is None:
            self.respawn_time = now + 4000
        if self.respawn_time and now >= self.respawn_time:
            self.level.increase_level()
            new_animation_speed = self.enemy.animation_speed
            new_attack_timer_max = self.enemy.attack_timer_max
            self.enemy = Enemy(425, 0)
            self.enemy.respawn(new_animation_speed, new_attack_timer_max)
            self.mysprites.add(self.enemy)
            self.respawn_time = None


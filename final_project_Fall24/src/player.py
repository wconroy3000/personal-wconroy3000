import pygame
import random
from src.hp import Hp

class Player(pygame.sprite.Sprite):
   def __init__(self, x, y):
      """
      Initialize the player with a sprite sheet.
      args:
        x: int - Starting x coordinate
        y: int - Starting y coordinate
        sprite_sheet_file: str - Path to the sprite sheet file
        frame_width: int - Width of a single frame
        frame_height: int - Height of a single frame
        num_frames: int - Total number of frames in the sprite sheet
      """
      super().__init__()
      
      self.sprite_sheets = {
         "idle": pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/IdleBlue.png").convert_alpha(),
         "upper": pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/UpperBlue.png").convert_alpha(),
         "slash": pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/SlashBlue.png").convert_alpha(),
         "overhead": pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/OverheadBlue.png").convert_alpha()
      }
      
      frame_width = 162   
      frame_height = 162
      
      num_frames = {
         "idle" : 10,
         "attack" : 7
      } 
      
      self.animations = {
         "idle": self.load_frames(self.sprite_sheets["idle"], frame_width, frame_height, num_frames["idle"]),
         "upper": self.load_frames(self.sprite_sheets["upper"], frame_width, frame_height, num_frames["attack"]),
         "slash": self.load_frames(self.sprite_sheets["slash"], frame_width, frame_height, num_frames["attack"]),
         "overhead": self.load_frames(self.sprite_sheets["overhead"], frame_width, frame_height, num_frames["attack"])
      }
      
      self.player_sounds = {
         "grunt_1": pygame.mixer.Sound("assets/sounds/01._damage_grunt_male.wav"),
         "grunt_2" : pygame.mixer.Sound("assets/sounds/03._damage_grunt_male.wav"),
         "grunt_3" : pygame.mixer.Sound("assets/sounds/05._damage_grunt_male.wav"),
      }


      self.current_animation = "idle"
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.is_animating = True
      self.animation_speed = 100  
      self.last_updated = pygame.time.get_ticks()
      
      
      self.image = self.frames[self.current_frame]
      self.rect = self.image.get_rect()
      self.rect.topleft = (x, y)
       
      self.can_attack = False
      self.attack_window_end = 0
      self.attacked_this_phase = False
      
      hp_font = pygame.font.Font(None, 36)
      self.hp = Hp(100,20,20,hp_font)
      self.current_attack = None

   def load_frames(self, sprite_sheet, frame_width, frame_height, num_frames):
      """
      Extract frames from the sprite sheet.
      args:
        sprite_sheet: str - The sprite sheet for the animation
        frame_width: int - Width of each frame
        frame_height: int - Height of each frame
        num_frames: int - Number of frames to extract
      return: 
        str: List of frames 
      """
      frames = []
      sheet_width, sheet_height = sprite_sheet.get_size()
      for i in range(num_frames):
         x = (i * frame_width) % sheet_width
         y = (i * frame_width) // sheet_width * frame_height
         frame = sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
         scaled_frame = pygame.transform.scale(frame, (frame_width*3,frame_height*3))
         frames.append(scaled_frame)
      return frames

   def update(self):
      """
      Handle sprite updates
      """
      if self.is_animating:
         now = pygame.time.get_ticks()
         if now - self.last_updated > self.animation_speed:
               self.last_updated = now
               self.current_frame += 1
               
               if self.current_frame >= len(self.frames):
                  if self.current_animation in ["slash", "upper", "overhead"]:
                     self.current_animation = "idle"
                     self.frames = self.animations[self.current_animation]
                     self.current_frame = 0
                  else:
                     self.current_frame = 0
               
               
               self.image = self.frames[self.current_frame]

   def start_animation(self):
      """
      Start playing the animation.
      """
      self.is_animating = True

   def stop_animation(self):
      """
      Stop the animation and reset to the first frame.
      """
      self.is_animating = False
      self.current_frame = 0
      self.image = self.frames[self.current_frame]
         
         
   
   def take_damage(self, damage):
      '''
      The player takes damage
      args: 
        damage: int - how much damage the player takes
      '''
      self.hp.take_damage(damage)
      self.player_sounds[random.choice(["grunt_1","grunt_2","grunt_3"])].play()
      
      
   
   def draw_health(self, screen):
       '''
       Allows the players health to be drawn on the screen
       args:
        screen: str - the screen the health is to be displayed on
       '''
       self.hp.draw(screen)
     
   
   def reset_attack(self):
      '''
      Resets the attack back to no attack and gets the player ready to attack next window
      '''
      self.current_attack = None
      self.attacked_this_phase = False
      
   def counter(self, enemy):
      '''
      Determines if the player will take damage or deal damage against the enemy
      args:
        enemy: str - the enemy class the player interacts with
      ''' 
      if self.current_attack == enemy.current_attack:
         enemy.take_damage(10)
         self.can_attack = False
      else: 
         self.take_damage(10)
      self.reset_attack()
      
   def set_attack(self, attack_type):
      '''
      Determines what attack the player performs based on user input
      args:
        attack_type: str - the attack the player performs
      ''' 
      if not self.can_attack or self.attacked_this_phase:
        return
      self.current_attack = attack_type
      self.current_animation = attack_type
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.start_animation()
      self.attacked_this_phase = True

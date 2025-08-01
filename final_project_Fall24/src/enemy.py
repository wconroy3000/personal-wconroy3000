import pygame
import random
from src.hp import Hp
   
   

class Enemy(pygame.sprite.Sprite):
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
         "idle" : pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/IdleRed.png").convert_alpha(),
         "upper" : pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/UpperRed.png").convert_alpha(),
         "slash" :pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/SlashRed.png").convert_alpha(),
         "overhead" : pygame.image.load("assets/animations/Fantasy_Warrior/Sprites/OverheadRed.png").convert_alpha()
      }
      
      frame_width = 162   
      frame_height = 162  
      
      self.num_frames = {
         "idle" : 10,
         "attack" : 7
      }
      
      self.animations = {
         "idle": self.load_frames(self.sprite_sheets["idle"], frame_width, frame_height, self.num_frames["idle"]),
         "upper": self.load_frames(self.sprite_sheets["upper"], frame_width, frame_height, self.num_frames["attack"]),
         "slash": self.load_frames(self.sprite_sheets["slash"], frame_width, frame_height, self.num_frames["attack"]),
         "overhead": self.load_frames(self.sprite_sheets["overhead"], frame_width, frame_height, self.num_frames["attack"]),
      }
      
      self.enemy_sounds = {
         "success": pygame.mixer.Sound("assets/sounds/242501__gabrielaraujo__powerupsuccess.wav"),
         "sword" : pygame.mixer.Sound("assets/sounds/sword_thunder_sound.wav"),
         "hit" : pygame.mixer.Sound("assets/sounds/Hitmarker_sound.wav")
      }

      self.current_animation = "idle"
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.is_animating = True
      self.animation_speed = 110  
      self.last_updated = pygame.time.get_ticks()


      self.image = self.frames[self.current_frame]
      self.rect = self.image.get_rect()
      self.rect.topleft = (x, y)
      
      self.attack_timer_max = 3000
      self.attack_timer = random.randint(1000,self.attack_timer_max)
      self.last_attack_time = pygame.time.get_ticks()
      
      self.is_attacking = False
      self.attack_start_time = 0
      self.attack_duration = self.animation_speed * self.num_frames["attack"]
      self.dealt_damage = False
      
      hp_font = pygame.font.Font(None, 36)
      self.hp = Hp(100,800,20,hp_font)
      self.current_attack = None
      self.is_enemy_dead = False
      

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
         flipped_frame =  pygame.transform.flip(scaled_frame, True, False)
         frames.append(flipped_frame)
      return frames

   def set_animation(self, animation_name):
    """
    Switch to the specified animation
    args:
        animation_names: str -The name of the animation to be set
    """
    if animation_name in self.animations:
        self.current_animation = animation_name
        self.frames = self.animations[animation_name]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.is_animating = True
        
        if animation_name in ["overhead", "slash", "upper"]:
           self.enemy_sounds["sword"].play()
           self.is_attacking = True
           self.attack_start_time = pygame.time.get_ticks()
           self.current_attack = animation_name

   def update(self):
    """
    Update the current animation and handle random attacks.
    """
    super().update()
    now = pygame.time.get_ticks()
    if self.is_enemy_dead == True:
       if 65 < self.animation_speed:
         self.animation_speed -= 5
       if self.attack_timer_max > 1500:
          self.attack_timer_max -= 100
       self.enemy_sounds["success"].play()  
       self.kill() 
       return
    if self.is_attacking:
       now = pygame.time.get_ticks()
       if now - self.attack_start_time > self.attack_duration:
          self.is_attacking = False
          self.dealt_damage = False
         
   
    if self.is_animating:
      if now - self.last_updated > self.animation_speed:
         self.last_updated = now
         self.current_frame += 1

         if self.current_frame >= len(self.frames):
            if self.current_animation != "idle":
                  self.set_animation("idle")
            else:
                  self.current_frame = 0 
         self.image = self.frames[self.current_frame]

    if now - self.last_attack_time > self.attack_timer:
        self.last_attack_time = now
        self.attack_timer = random.randint(1000, self.attack_timer_max)
        attack = random.choice(["overhead", "slash", "upper"])
        self.set_animation(attack)
   
   def take_damage(self, damage):
      '''
      Allows the enemy to take damage
      args:
        damage: int - the amount of damage the enemy takes
      '''
      self.hp.take_damage(damage)
      self.enemy_sounds["hit"].play()
      if self.hp.current_hp == 0:
         self.is_enemy_dead = True
         self.set_animation(None)
   
   def draw_health(self,screen):
      '''
      Allows the HP to display on screen
      args:
        screen: str - the screen to be displayed on'''
      self.hp.draw(screen)
      
   def respawn(self, animation_speed, attack_timer_max):
     '''
     Decreases the values of the enemy's durations to make the attack harders
     args: 
        animation_speed: int - the new animation speed for after the respawn
        attack_timer_max: int the new max time between attacks for after the respawn
     '''
     self.animation_speed = animation_speed
     self.attack_timer_max = attack_timer_max
     self.attack_duration = self.animation_speed * self.num_frames["attack"]
       
   def handle_attack(self, player, now):
    '''
    Determines if the enemy will recieve damage during the attack window
    args:
        player: str - brings the player class from controller to interact with
        now: - the time the attack started
    '''
    attack_window_start = self.attack_start_time
    attack_window_end = self.attack_start_time + self.attack_duration
    if attack_window_start <= now <= attack_window_end:
        player.can_attack = True
    elif now > attack_window_end and not self.dealt_damage:
        if player.attacked_this_phase:
            player.counter(self)
        else:
            player.take_damage(10)
        self.dealt_damage = True
    else:
        player.can_attack = False
        player.attacked_this_phase = False
        

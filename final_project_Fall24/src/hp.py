class Hp:
    def __init__(self, max_hp, x, y, font):
        '''
        Initializes the data needed for the health 
        args:
            max_hp: int - the max hp for the character
            x: int - the x value for the HP to be displayed
            y: int - the y value for the HP to be displayed
            font: str - the font for the HP to be displayed
        '''
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.x = x
        self.y = y
        self.font = font 
        self.color = (255,255,255)
        
    def take_damage(self, damage):
        '''
        Applies damage to the characters HP
        args:
            damage: int - the amount of damage the character recieves
        '''
        self.current_hp = max(0, self.current_hp - damage)
        
    def draw(self, screen):
        '''
        Allows the HP to be drawn on the screen
        args:
            screen: str - allows the hp to be displayed on the screen
        '''
        hp_value = f'HP: {self.current_hp}/{self.max_hp}'
        text_surface = self.font.render(hp_value, True, self.color)
        screen.blit(text_surface, (self.x, self.y))
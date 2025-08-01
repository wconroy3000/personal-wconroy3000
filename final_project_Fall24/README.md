# The Last Vanguard
## CS110 Final Project  Fall, 2024 

## Team Members

    William Conroy

## Project Description
    The player will control a swordsman who is capable of performing 3 different attack (overhead, slash, uppercut). The player however can only input these attacks after the enemy swordsman randomly performs one. The player is to input whatever attack the enemy performs in order to "counter" the attack and avoid damage. If they counter successfully the enemy will recieve damage, and if they fail the player will take damage. The enemy will survive 10 hits and then the player will move on to the next level where the enemy gets faster. There are an infinite amount of levels, and the player is to survive as many levels as possible. Inputting J will let the player "slash". Inputting "K" will let the player "overhead". Inputting "L" will let the player "uppercut". The players highscore will be saved to a file and update after each game. 

## GUI Design
The game will have two swordsman standing on a platform facing each other. One will be highlighted in blue to inidicate the player and the other will be red to indicate the enemy. The player's HP will be displayed in the top left and the enemy's HP will be displayed in the top right. The current level will be shown in the top of the middle of the screen. 
### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)
![final gui](assets/finalgui2.jpg)

## Program Design

controller
enemy
gameover
highscore
hp
level
player
view


### Features

1. playable character
2. game over screen
3. NPCs
4. Progressive increase in difficulty
5. Health Points
6. Respawning NPCs
7. Audio indicators
8. Levels
9. Saved Highscore 

### Classes

controller: maintains game flow
enemy: controls the enemy class 
gameover: manages the game over message to be displayed
highscore: writes out the highscore to a file
hp: manages the characters health
level: manages the level
player: controls the player class
view: manages what displays


## ATP

    Test Case 1: Player Damage
        - Test Description: Verify that the player will lose HP and play an audio cue indicating this
        - Test Steps:
            1. Start the game
            2. Press nothing
            3. After enemy attack look at HP on the top left corner and verify a change.
            4. after enemy attack verify a grunt sound is played
        - Expected Outcome: The HP value in the top left should decrease by 10 and a grunt should be heard

    Test Case 2: Successful Counter
        - Test Description: Verify that the player will successfully counter an enemy slash
        - Test Steps:
            1. Start the game
            2. Wait for enemy slash
            3. Input "J" once enemy slashes
            4. Verify a "hit" sound is played for the enemy
            5. Verify the player performs a slash
            6. Verify the HP on the top right decreases by 10
        - Expected Outcome: The player should perform a slash attack leading to a hit audio cue and a decrease the enemys HP

    Test Case 3: Player Death
        - Test Description: Verify that when the player dies a game over screen appears
        - Test Steps:
            1. Start the game
            2. Press nothing 
            3. Wait for the player HP to drop to 0
            4. Verify that once this happens the screen goes to black and says "Game Over" while still displaying the level
        - Expected Outcome: The screen will go to black and display game over with the level the player reached

    Test Case 4: Failed Counter
        - Test Description: Verify that the player fails a counter properly 
        - Test Steps:
            1. Start the game
            2. Wait for an enemy overhead or uppercut
            3. Input "J"
            4. Verify a grunt sound is played
            5. Verify the player performs a slash
            6. Verify the players HP decreases by 10
        - Expected Outcome: The player will perform a slash, therefore failing the counter and taking damage

    Test Case 5: Enemy Death
        - Test Description: Verify that the enemy despawns and the level increases
        - Test Steps:
            1. Start the game
            2. Play the game and counter successfully until enemy HP reaches 0
            3. Verify that when the enemy despawns an audio cue prompting the end of the level is played
            4. Verify the enemy despawns for 4 seconds
            5. Verify that when the enemy respawns the level increases by 1
            6. Verify that when the enemy respawns the enemy HP is reset back to 100
        - Expected Outcome: The enemy should despawn and play an audio cue indicating the end of the level, and respawn afte 4 seconds with full health and on the next level. 
# This is a game I created using pygame with example.py as a base.
import pygame
import random

# Initialize the pygame modules to get everything started.
pygame.init() 

# Set the width and height of the screen.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# Create the player, monsters and prize and assign the relevant images. 
player = pygame.image.load("player1.png")
prize = pygame.image.load("prize1.png")
monster1 = pygame.image.load("monster1.png")
monster2 = pygame.image.load("monster2.png")
monster3 = pygame.image.load("monster3.png")

# Get the width and height of the images in order to do boundary detection.
image_height = player.get_height()
image_width = player.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()
monster1_height = monster1.get_height()
monster1_width = monster1.get_width()
monster2_height = monster2.get_height()
monster2_width = monster2.get_width()
monster3_height = monster3.get_height()
monster3_width = monster3.get_width()

# Store the positions of the player. 
player_position_x = 100
player_position_y = 50

# The prize starts off screen and at a random y position.
prize_position_x = screen_width
prize_position_y = random.randint(0, screen_height - prize_height)

# The monsters starts off screen and at random y positions.
monster1_position_x = screen_width
monster1_position_y = random.randint(0, screen_height - monster1_height)
monster2_position_x = screen_width
monster2_position_y = random.randint(0, screen_height - monster2_height)
monster3_position_x = screen_width
monster3_position_y = random.randint(0, screen_height - monster3_height)

# This will be used to check if the up, down, left or right key has been pressed.
key_up = False
key_down = False
key_left = False
key_right = False

# This is the start of the game loop.
while 1: 
    screen.fill(0) 
    # This draws the player image to the screen at the postion specfied.
    screen.blit(player, (int(player_position_x), int(player_position_y)))
    screen.blit(prize, (int(prize_position_x), int(prize_position_y)))
    screen.blit(monster1, (int(monster1_position_x), int(monster1_position_y)))
    screen.blit(monster2, (int(monster2_position_x), int(monster2_position_y)))
    screen.blit(monster3, (int(monster3_position_x), int(monster3_position_y)))
        
    # Updates the screen
    pygame.display.flip()
    
    # This event checks if the user quits the program, then if so it exits the program. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user presses a key down.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up = True               
            if event.key == pygame.K_DOWN:
                key_down = True               
            if event.key == pygame.K_LEFT:
                key_left = True                
            if event.key == pygame.K_RIGHT:
                key_right = True
                
        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up = False               
            if event.key == pygame.K_DOWN:
                key_down = False                
            if event.key == pygame.K_LEFT:
                key_left = False                
            if event.key == pygame.K_RIGHT:
                key_right = False
                
    # If the user presses the up, down, left or right keys, the following happens.
    if key_up == True:
        # Makes sure the user does not move the player above the window.
        if player_position_y > 0 : 
            player_position_y -= 1
    if key_down == True:
        # Makes sure the user does not move the player below the window.
        if player_position_y < screen_height - image_height:
            player_position_y += 1
    if key_left == True:
        # Makes sure the user does not move the player out the left of the window.
        if player_position_x > 0: 
            player_position_x -= 1
    if key_right == True:
        # Makes sure the user does not move the player out the right of the window.
        if player_position_x < screen_width - image_width: 
            player_position_x += 1
            
            
    # Create bounding boxes for all the game elements.  
    player_box = pygame.Rect(player.get_rect())
    player_box.top = int(player_position_y)
    player_box.left = int(player_position_x)

    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = int(prize_position_y)
    prize_box.left = int(prize_position_x)

    monster1_box = pygame.Rect(monster1.get_rect())
    monster1_box.top = int(monster1_position_y)
    monster1_box.left = int(monster1_position_x)

    monster2_box = pygame.Rect(monster2.get_rect())
    monster2_box.top = int(monster2_position_y)
    monster2_box.left = int(monster2_position_x)

    monster3_box = pygame.Rect(monster3.get_rect())
    monster3_box.top = int(monster3_position_y)
    monster3_box.left = int(monster3_position_x)
    

    # If user collides with a monster, the user loses the game - display the text then quits the game and closes window.
    if player_box.colliderect(monster1_box):
        print("You lose!!")
        pygame.quit()
        exit(0)        
    if player_box.colliderect(monster2_box):
        print("You lose!!")
        pygame.quit()
        exit(0)        
    if player_box.colliderect(monster3_box):
        print("You lose!!")
        pygame.quit()
        exit(0)
        
    # If user collides with the prize the user wins the game - display the text then quits the game and closes window.
    if player_box.colliderect(prize_box):
        print("You win!!")
        pygame.quit()
        exit(0)

    # If monster is off the screen the user wins the game - display the text then quits the game and closes window.
    if (monster1_position_x < 0 - monster1_width) and (monster2_position_x < 0 - monster2_width) and (monster3_position_x < 0 - monster3_width):        
        print("You win!")        
        pygame.quit()        
        exit(0)

    # Make enemy move onto the screen at different speeds.    
    monster1_position_x -= 0.4
    monster2_position_x -= 0.3
    monster3_position_x -= 0.5

    # Make prize approach move onto the screen.
    prize_position_x -= 0.2
    
# This is the end of the game loop.

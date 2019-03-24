# Python Game built with Pygame

import pygame

pygame.init() # Initialize pgame

# Set Up Game Screen
screenWidth = 500
screenHeight = 500
screenTitle = 'Crossy Game'
colorWhite = (255,255,255)
colorBlack = (0,0,0)
pygameClock = pygame.time.Clock()
tickRate = 60 # FPS, frames per second
isGameOver = False

# Make Game Screen
gameScreen = pygame.display.set_mode((screenWidth, screenHeight))
gameScreen.fill(colorWhite)
pygame.display.set_caption(screenTitle)

# Game Loop
# Stop game if isGameOver is True
while not isGameOver:

    # Handles and notices events in pygame
    for event in pygame.event.get():
        # Stop game if event is QUIT
        if event.type == pygame.QUIT:
            isGameOver = True
        print(event)
    
    pygame.display.update() # Update screen
    pygameClock.tick(tickRate) # Initializes the clock

# Close game
pygame.quit()
quit()

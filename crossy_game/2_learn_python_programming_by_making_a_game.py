# Python Game built with Pygame
import pygame

# Set Up Game Screen
screenWidth = 500
screenHeight = 750
screenTitle = 'Crossy Game'
colorWhite = (255,255,255)
colorBlack = (0,0,0)

# Set Up Game Loop
pygameClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:

    tickRate = 60 # FPS, frames per second

    def __init__(self, imgPath, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Make Game Screen
        self.gameScreen = pygame.display.set_mode((width, height))
        self.gameScreen.fill(colorWhite)
        pygame.display.set_caption(title)
        # Set Background image
        backgroundImage = pygame.image.load(imgPath)
        self.image = pygame.transform.scale(backgroundImage, (width, height))

    def runGameLoop(self, lvl):
        isGameOver = False
        didWin = False
        yDirection = 0
        xDirection = 0

        # Init Characters, enemies and treasure chest
        playerCharacter = PlayerCharacter('player.png', 225, 700, 50, 50)

        if lvl >= 2:
            enemy0 = NPC('enemy.png', 50, 150, 50, 50, 6 * lvl / 4)
        else:
            enemy0 = NPC('enemy.png', 50, 800, 50, 50, 8)

        if lvl >= 3:
            enemy1 = NPC('enemy.png', 190, 300, 50, 50, 4 * lvl / 2)
        else:
            enemy1 = NPC('enemy.png', 50, 800, 50, 50, 8)

        enemy2 = NPC('enemy.png', 150, 450, 50, 50, 7 * lvl / 5)

        if lvl >= 4:
            enemy3 = NPC('enemy.png', 200, 600, 50, 50, 5 * lvl / 3)
        else:
            enemy3 = NPC('enemy.png', 50, 800, 50, 50, 8)

        treasure = GameObject('treasure.png', 225, 40, 50, 50)

        # Game Loop
        # Stop game if isGameOver is True
        while not isGameOver:

            # Handles and notices events in pygame
            for event in pygame.event.get():
                # Stop game if event is QUIT
                if event.type == pygame.QUIT:
                    isGameOver = True
                # Key pressed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        yDirection = 1
                    elif event.key == pygame.K_DOWN:
                        yDirection = -1
                    elif event.key == pygame.K_RIGHT:
                        xDirection = 1
                    elif event.key == pygame.K_LEFT:
                        xDirection = -1
                # No key pressed
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        yDirection = 0
                        xDirection = 0
                print(event)

            # Redraw white screen and draw backgorund image
            self.gameScreen.fill(colorWhite)
            self.gameScreen.blit(self.image, (0, 0))

            # Update Player position
            playerCharacter.move(yDirection, xDirection, self.height, self.width)
            playerCharacter.draw(self.gameScreen)

            # Move and draw enemies
            enemy0.move(self.width)
            enemy0.draw(self.gameScreen)

            enemy1.move(self.width)
            enemy1.draw(self.gameScreen)

            enemy2.move(self.width)
            enemy2.draw(self.gameScreen)

            enemy3.move(self.width)
            enemy3.draw(self.gameScreen)

            # Draw treasure chest
            treasure.draw(self.gameScreen)

            # End game if either treasure reached or hit by enemy
            enemies = [enemy0, enemy1, enemy2, enemy3]

            # End game if treasure reached
            if playerCharacter.detectCollisions(treasure):
                isGameOver = True
                didWin = True
                text = font.render('Yeay, you won!', True, colorBlack)
                self.gameScreen.blit(text, (50, 225))
                pygame.display.update()
                pygameClock.tick(1)
                break
            # Detect collisions with enemies stores in array enemies
            else:
                for enemy in enemies:
                    if playerCharacter.detectCollisions(enemy):
                        isGameOver = True
                        didWin = False
                        text = font.render('Damn, you lost!', True, colorBlack)
                        self.gameScreen.blit(text, (50, 225))
                        pygame.display.update()
                        pygameClock.tick(1)
                        break

            pygame.display.update() # Update screen
            pygameClock.tick(self.tickRate) # Initializes the clock

        if didWin:
            self.runGameLoop(lvl + 1)
        else:
            return

class GameObject:

    def __init__(self, imgPath, x, y, width, height):
        # Load Image from a file and scale it
        objImg = pygame.image.load(imgPath)
        self.img = pygame.transform.scale(objImg, (width, height))

        self.x = x
        self.y = y

        # Size of the object
        self.width = width
        self.height = height

    # Draw on top of the background
    def draw(self, background):
        background.blit(self.img, (self.x, self.y))

# Character controlled by the player
class PlayerCharacter(GameObject):
    # Tiles moved per second
    speed = 10

    def __init__(self, imgPath, x, y, width, height):
        super().__init__(imgPath, x, y, width, height)

    # Move function
    def move(self, yDirection, xDirection, maxHeight, maxWidth):
        if yDirection > 0:
            self.y -= self.speed
        elif yDirection < 0:
            self.y += self.speed
        elif xDirection > 0:
            self.x += self.speed
        elif xDirection < 0:
            self.x -= self.speed
        # Make Player never move out of the screen
        if self.y >= maxHeight - 50:
            self.y = maxHeight - 50
        if self.x >= maxWidth - 50:
            self.x = maxWidth - 50

    # Detect collisions with enemies
    def detectCollisions(self, otherBody):
        if self.y > otherBody.y + otherBody.height:
            return False
        elif self.y + self.height < otherBody.y:
            return False

        if self.x > otherBody.x + otherBody.width:
            return False
        elif self.x + self.width < otherBody.x:
            return False

        return True

# Enemies class (Non Player Character)
class NPC(GameObject):
    speed = 10

    # Constructor
    def __init__(self, imgPath, x, y, width, height, speed):
        super().__init__(imgPath, x, y, width, height)
        self.speed = speed

    # Move Function to move the NPC
    def move(self, maxWidth):
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x >= maxWidth - 50:
            self.speed = -abs(self.speed)
        self.x += self.speed

    


pygame.init() # Initialize pgame

newGame = Game('background.png', screenTitle, screenWidth, screenHeight)
newGame.runGameLoop(1)

#newGameObject = GameObject('background.png', 500, 500)
#newGameObject.draw()

# Load the PlayEr Image from a file
#playerImg = pygame.image.load('player.png')
#playerImg = pygame.transform.scale(playerImg, (50, 50))



    # Draw Square and Cirlce
    #pygame.draw.rect(gameScreen, colorBlack, [200, 200,100, 100])
    #pygame.draw.circle(gameScreen, colorBlack,(250, 150), 50)

    # Draw the Player image
    #gameScreen.blit(playerImg, (225, 225))
    
    

# Close game
pygame.quit()
quit()

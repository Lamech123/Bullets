import pygame
import random
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
 
# This class represents the block        
class Block(pygame.sprite.Sprite):
     
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
# This class represents the Player        
class Player(pygame.sprite.Sprite):
     
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([20,20])
        self.image.fill(red)
 
        self.rect = self.image.get_rect()
         
# This class represents the bullet        
class Bullet(pygame.sprite.Sprite):
     
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(black)
 
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width,screen_height])
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.RenderPlain()
 
# List of each block in the game
block_list = pygame.sprite.RenderPlain()
 
# List of each bullet
bullet_list = pygame.sprite.RenderPlain()
 
for i in range(50):
    # This represents a block
    block = Block(blue)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
score = 0
player.rect.y=370
 
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
         
        # Move the bullet up 5 pixels
        bullet.rect.y -= 5
         
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
         
        # For each block hit, remove the bollet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print( score )
             
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
         
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Set the player x position to the mouse x position
    player.rect.x=pos[0]
     
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
    # Clear the screen
    screen.fill(white)
         
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
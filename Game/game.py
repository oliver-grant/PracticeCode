import pygame
import random

# Screen size is 64 by 48 blocks
x_blocks = 64
y_blocks = 48
# Block Sizes
x_block_size = 16
y_block_size = 16

screen = pygame.display.set_mode((x_blocks*x_block_size, y_blocks*y_block_size))
pygame.display.set_caption("My Game")

clock=pygame.time.Clock()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

# Draws a 16 by 16 block of wall with x,y as the upper left coord in blocks
def draw_spec(screen, x, y, col):
  pygame.draw.rect(screen, col, (x*x_block_size, y*y_block_size, 1*x_block_size, 1*y_block_size)) 

# Draws a 16 by 16 block of wall with x,y as the upper left coord in blocks
def draw_wall(screen, x, y):
  draw_spec(screen, x, y, WHITE)

def get_new_loc(x, y):
  dirct = random.randint(0,3)
  new_loc = [-1, -1]
  if (dirct == 0):
    new_loc = [x, y+1]
  if (dirct == 1):
    new_loc = [x+1,y]
  if (dirct == 2):
    new_loc = [x, y-1]
  if (dirct == 3):
    new_loc = [x-1, y]
  if (0 <= new_loc[0]) and (new_loc[0] < x_blocks) and (0 <= new_loc[1]) and (new_loc[1] < y_blocks):
    return new_loc
  else:
    return [x,y]

x_start = -1
y_start = -1
blocks  = [[0 for y in range(y_blocks)] for x in range(x_blocks)]  
# Draws a randomized dungeon
def create_dungeon(screen, length):
    #get starting location
    global x_start, y_start, blocks
    if ((x_start == -1) and (y_start == -1)):
        x_start = random.randint(0, x_blocks-1)
        y_start = random.randint(0, y_blocks-1)
    blocks[x_start][y_start] = 2

    #Randomly build dungeon
    size = 0
    x_cur = x_start
    y_cur = y_start
    while (size < length):
       new_loc = get_new_loc(x_cur, y_cur)
       if (new_loc[0] != x_cur) or (new_loc[1] != y_cur):
         x_cur = new_loc[0]
         y_cur = new_loc[1]
         if (blocks[x_cur][y_cur] == 0):
           blocks[x_cur][y_cur] = 1
           size = size + 1
    blocks[x_cur][y_cur] = 2

    
def draw_dungeon(screen):
  for i in range(x_blocks):
     for j in range(y_blocks):
         if(blocks[i][j] == 1):
             draw_wall(screen, i, j)
         if(blocks[i][j] == 2):
             draw_spec(screen, i, j, RED)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, RED, [1 + x, y, 5, 5], 0)
 
    # Legs
    pygame.draw.line(screen, RED, [3 + x, 9 + y], [5 + x, 14 + y], 1)
    pygame.draw.line(screen, RED, [3 + x, 9 + y], [x, 14 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [3 + x, 9 + y], [5 + x, 7 + y], 1)
 
    # Arms
    pygame.draw.line(screen, RED, [3 + x, 4 + y], [5 + x, 9 + y], 1)
    pygame.draw.line(screen, RED, [3 + x, 4 + y], [1 + x, 9 + y], 1)


# -------- Main Program Loop -----------
done = False
i = 0
while not done:
  # --- Game logic should go here
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0  


  # Moving the guy
  x_coord = x_coord + x_speed
  y_coord = y_coord + y_speed
    
  # --- Screen-clearing code goes here
 
  # Here, we clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
 
  # If you want a background image, replace this clear with blit'ing the
  # background image.
  screen.fill(BLACK)
  if (x_start == -1):
    create_dungeon(screen, 500)
  draw_dungeon(screen)
  draw_stick_figure(screen, x_coord, y_coord)
 
  # --- Drawing code should go here
 
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.flip()
 
  # --- Limit to 60 frames per second
  clock.tick(60)


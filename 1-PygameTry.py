''' 

1-PygameTry.py 

Let's try to create someting 


Draft: 

- class Snake 
--  def init 
--  def drawSnake
--  def moveSnake

- class Snack 
--  def init 
--  def drawSnack

def drawWindow

def main

'''


## Import modules
import pygame
import random



# Define some global variables
screen_width = 500
cube_width = 20


## Create the snake class
class Snake(object):

    def __init__(self, body, direction=(0,1)):
        self.body = body
        self.direction = direction

    def drawSnake(self, surface):
        for i in range(len(self.body)):
            if i == 0:
                pygame.draw.rect(surface, (255,255,255),
                                 ( self.body[i][0], self.body[i][1], cube_width, cube_width) )
            else:
                pygame.draw.rect(surface, (0,255,0),
                                 ( self.body[i][0], self.body[i][1], cube_width, cube_width) )

    def moveSnake(self, direction, snack=False): 

        next_block = [ self.body[0][0]+direction[0]*cube_width,
                       self.body[0][1]+direction[1]*cube_width ]

        self.body.insert(0, next_block)
        self.body.pop()


        

## Function to redraw the window
def drawWindow(surface):
    global s
    surface.fill((0,0,0))
    s.drawSnake(surface)
    pygame.display.update()
        

## Create the main function

def main():
    global screen_width, s
    
    # Initialize the pygame module
    pygame.init()
    # Create the background
    background = pygame.display.set_mode((screen_width, screen_width))
    # Create clock 
    clock = pygame.time.Clock()

    s = Snake( [ [50, 50], [70, 50], [90, 50] ] )

    # Main loop:
    running = True
    while( running ):

        clock.tick(10) 
        
        for event in pygame.event.get():

            # Quit #
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                s.direction = (-1, 0) 
            elif keys[pygame.K_RIGHT]:
                s.direction = ( 1, 0) 
            elif keys[pygame.K_UP]:
                s.direction = ( 0,-1) 
            elif keys[pygame.K_DOWN]:
                s.direction = ( 0, 1) 

        s.moveSnake( s.direction ) 
        

        drawWindow(background)



        
## Run the main function
if __name__ == "__main__":
    main()                      # Call the funciton
    

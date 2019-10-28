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


# Define some global variables
screen_width = 500
cube_width = 20


## Create the snake class
class Snake(object):

    def __init__(self, body, direction):
        self.direction_x, self.direction_y = direction
        self.body = body

    def drawSnake(self, surface):
        for i in range(len(self.body)):
            if i == 0:
                pygame.draw.rect(surface, (255,255,255),
                                 ( self.body[i][0], self.body[i][0], cube_width, cube_width))
            else:
                pygame.draw.rect(surface, (0,255,0),
                                 ( self.body[i][0], self.body[i][0], cube_width, cube_width))
            
                



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

    s = Snake( [[50, 50]], (1,0) )

    # Main loop:
    running = True
    while( running ):

        for event in pygame.event.get():


            # Quit #
            if event.type == pygame.QUIT:
                running = False

        drawWindow(background)



        
## Run the main function
if __name__ == "__main__":
    main()                      # Call the funciton
    

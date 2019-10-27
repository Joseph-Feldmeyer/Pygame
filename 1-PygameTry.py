''' 

1-PygameTry.py 

Let's try to create someting 

'''


## Import modules
import pygame


# Define some global variables
screen_width = 500
cube_width = 10 


## Create the cube class
class Cube(object):

    def __init__(self, pos, color):
        self.x_pos, self.y_pos = pos
        self.color = color

    def drawCube(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x_pos, self.y_pos, cube.width, cube.width))



## Function to redraw the window
def drawWindow(surface):
    global screen_width, cube_width, c
    surface.fill((0,0,0))
    c.drawCube(surface)
    pygame.display.update()
        

## Create the main function

def main():

    # Initialize the pygame module
    pygame.init()
    # Create the background
    background = pygame.display.set_mode((500,500))

    c = Cube((50, 50), (0,255,0))

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
    

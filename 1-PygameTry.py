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
        
        if not snack:
            self.body.pop()


class Snack(object):

    def __init__(self, body):
        self.body_x, self.body_y = body

    def drawSnack(self, surface):
        pygame.draw.rect(surface, (255,0,0),
                         ( self.body_x, self.body_y, cube_width, cube_width) ) 




## Function to redraw the window
def drawWindow(surface):
    global s
    surface.fill((0,0,0))
    s.drawSnake(surface)
    snack.drawSnack(surface)
    pygame.display.update()

    
        

## Create the main function

def main():
    global screen_width, s, snack
    
    # Initialize the pygame module
    pygame.init()
    # Create the background
    background = pygame.display.set_mode((screen_width, screen_width))
    # Create clock 
    clock = pygame.time.Clock()

    # Create a snake 
    s = Snake( [ [60, 60], [80, 60], [100, 60] ] )
    # Create a snack
    snack = Snack( [200, 200] )
    
    
    # Main loop:
    running = True
    while( running ):

        clock.tick(10) 
        
        for event in pygame.event.get():

            # Quit #
            if event.type == pygame.QUIT:
                running = False

            # Logic for key presses, and direction change
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                s.direction = (-1, 0) 
            elif keys[pygame.K_RIGHT]:
                s.direction = ( 1, 0) 
            elif keys[pygame.K_UP]:
                s.direction = ( 0,-1) 
            elif keys[pygame.K_DOWN]:
                s.direction = ( 0, 1) 


        # Logic for snack collision
        if (s.body[0][0]+s.direction[0]*cube_width, s.body[0][1]+s.direction[1]*cube_width) == (snack.body_x, snack.body_y):
            s.moveSnake( s.direction, snack = True )

            # Find all empty cells:
            empty_cells = [ [x*cube_width, y*cube_width]
                            for x in range(screen_width//cube_width)
                                for y in range(screen_width//cube_width)  ]
            for body_part in s.body:
                index = empty_cells.index(body_part)
                empty_cells.pop(index)

            # Choose a random empty cell
            snack_x, snack_y = random.choice(empty_cells) 
            # New snack
            snack = Snack( [snack_x, snack_y] )

        else:
            s.moveSnake( s.direction ) 

        # Logic for lose game:
        ## Run into body part
        if s.body[0] in s.body[1:]:
            running = False
        ## Run out of screen
        if s.body[0] not in [ [x*cube_width, y*cube_width]
                              for x in range(screen_width//cube_width)
                              for y in range(screen_width//cube_width)  ]:
            running = False

        drawWindow(background)


    print("Your score is ", len(s.body))



        
## Run the main function
if __name__ == "__main__":
    main()                      # Call the funciton
    

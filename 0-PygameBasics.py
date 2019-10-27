'''

0-PygameBasics.py 

https://dr0id.bitbucket.io/legacy/pygame_tutorials.html
Learn the basics of pygame so that I can start creating what I want. 

'''


## Import libraries
import pygame


## Create your main function
def main():

    # Initialize the pygame module
    pygame.init()

    # Create screen surface
    screen = pygame.display.set_mode((500,500))


    # Define a variable to control the main loop
    running = True

    # Main loop
    while running:

        # Event handling, gets all events from the event queue
        for event in pygame.event.get():

            # Quit the game
            if event.type == pygame.QUIT:
                running = False




                
## Run the funciton if this module is executed as the main script
if __name__ == "__main__":
    main()                      # Call the main funciton



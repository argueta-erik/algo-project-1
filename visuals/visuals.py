# Example file showing a basic pygame "game loop"
import pygame


# Function defining the lines and rulers for reference
def reference_lines():
    # Vertical Lines
    pygame.draw.line(screen, "red", (640, 0), (640, 720), 1)    # 1/4 Line
    pygame.draw.line(screen, "red", (320, 0), (320, 720), 1)    # 1/2 Line
    pygame.draw.line(screen, "red", (960, 0), (960, 720), 1) # 3/4 Line

    # Horizontal Lines
    pygame.draw.line(screen, "blue", (0, 360), (1280, 360), 1)
    pygame.draw.line(screen, "blue", (0, 70+70+(720/2)), (1280, 70+70+(720/2)), 1)
    
# Function defining the Visualization for the algorithms
def canvas_player(x, y):    # x= 660, y=50
    pygame.draw.rect(screen, "black", (x, y, 600, 320), 3)   # Canvas Player
    pygame.draw.rect(screen, "black", (x+275, y+340, 50, 50), 3)    # Play Button
    pygame.draw.rect(screen, "black", (x+340, y+340, 75, 50), 3)   # FFWD Button
    pygame.draw.rect(screen, "black", (x+185, y+340, 75, 50), 3)    # RWND Button

# Function defining the Menu listing
def menu_listing(x, y):     # x=30, y=50
    pygame.draw.circle(screen, "black", (x, y), 15, 3)
    pygame.draw.rect(screen, "black", (x+30, y-25, 200, 50), 3)
    pygame.draw.rect(screen, "black", (x+245, y-25, 125, 50), 3)

    pygame.draw.circle(screen, "black", (x, y+70), 15, 3)
    pygame.draw.rect(screen, "black", (x+30, y+45, 200, 50), 3)
    pygame.draw.rect(screen, "black", (x+245, y+45, 125, 50), 3)

    pygame.draw.circle(screen, "black", (x, y+140), 15, 3)
    pygame.draw.rect(screen, "black", (x+30, y+115, 200, 50), 3)
    pygame.draw.rect(screen, "black", (x+245, y+115, 125, 50), 3)

    pygame.draw.circle(screen, "black", (x, y+210), 15, 3)
    pygame.draw.rect(screen, "black", (x+30, y+185, 200, 50), 3)
    pygame.draw.rect(screen, "black", (x+245, y+185, 125, 50), 3)

    pygame.draw.circle(screen, "black", (x, y+280), 15, 3)
    pygame.draw.rect(screen, "black", (x+30, y+255, 200, 50), 3)
    pygame.draw.rect(screen, "black", (x+245, y+255, 125, 50), 3)

# Function defining window to add Elements to algorithm
def elements():     # x = 30, y = 70+(720/2)
    # Option to set the size of the array
    pygame.draw.circle(screen, "black", (30, 70+(720/2)), 15, 3)
    pygame.draw.rect(screen, "black", (60, 405, 120, 50), 3)
    pygame.draw.rect(screen, "blue", (60+15+120, 405, 50, 50), 3)

    # Option to randomly fill the array
    pygame.draw.circle(screen, "black", (30, 70+70+(720/2)), 15, 3)
    pygame.draw.rect(screen, "black", (60, 70+70+(720/2)-30, 120, 50), 3)
    pygame.draw.circle(screen, "black", (60+15+120+15+15+20, 70+70+(720/2)), 15, 3)
    pygame.draw.rect(screen, "black", (60+15+120+15+15+15+15+20, 70+70+(720/2)-30, 120, 50), 3)

    # Option to fill in the array manually
    pygame.draw.circle(screen, "black", (30, 25+25+25+70+70+(720/2)), 15, 3)
    pygame.draw.rect(screen, "black", (60, 20+25+70+70+(720/2), 320, 50), 3)


    # Submit Button
    pygame.draw.rect(screen, "green", (120, 625, 150, 50), 5)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    
    # Rulers for Reference
    # reference_lines()
    
    # Canvas Player
    canvas_player(640, 180)
    
    # Dedicated to the Algorithm Selection
    menu_listing(30, 50)

    # Displaying Elements
    elements()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
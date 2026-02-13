# Example file showing a basic pygame "game loop"
import pygame


# Function defining the lines and rulers for reference
def reference_lines():
    pygame.draw.line(screen, "red", (640, 0), (640, 720), 1)    # 1/4 Line
    pygame.draw.line(screen, "red", (320, 0), (320, 720), 1)    # 1/2 Line
    pygame.draw.line(screen, "red", (960, 0), (960, 720), 1) # 3/4 Line
    
# Function defining the Visualization for the algorithms
def canvas_player():
    pygame.draw.rect(screen, "black", (660, 50, 600, 320), 3)   # Canvas Player
    pygame.draw.rect(screen, "black", (935, 390, 50, 50), 3)    # Play Button
    pygame.draw.rect(screen, "black", (1000, 390, 75, 50), 3)   # FFWD Button
    pygame.draw.rect(screen, "black", (845, 390, 75, 50), 3)    # RWND Button


# Funciton defining the Menu listing
def menu_listing():
    pygame.draw.circle(screen, "black", (30, 50), 15, 3)
    pygame.draw.rect(screen, "black", (60, 25, 200, 50), 3)

    pygame.draw.circle(screen, "black", (30, 120), 15, 3)
    pygame.draw.rect(screen, "black", (60, 95, 200, 50), 3)

    pygame.draw.circle(screen, "black", (30, 190), 15, 3)
    pygame.draw.rect(screen, "black", (60, 165, 200, 50), 3)

    pygame.draw.circle(screen, "black", (30, 260), 15, 3)
    pygame.draw.rect(screen, "black", (60, 235, 200, 50), 3)

    pygame.draw.circle(screen, "black", (30, 330), 15, 3)
    pygame.draw.rect(screen, "black", (60, 305, 200, 50), 3)

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
    reference_lines()
    # PADDING IS AT 15px

    canvas_player()

    # Dedicated to the Algorithm Selection
    menu_listing()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
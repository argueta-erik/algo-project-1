# Example file showing a basic pygame "game loop"
import pygame

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
    pygame.draw.line(screen, "red", (640, 0), (640, 720), 1)    # 1/4 Line
    pygame.draw.line(screen, "red", (320, 0), (320, 720), 1)    # 1/2 Line
    pygame.draw.line(screen, "red", (960, 0), (960, 720), 1) # 3/4 Line
    
    # Canvas for the Sorting Visualization
    pygame.draw.rect(screen, "black", (660, 50, 600, 320), 3)
    pygame.draw.rect(screen, "black", (935, 390, 50, 50), 3)    # Play Button
    pygame.draw.rect(screen, "black", (1000, 390, 75, 50), 3)    # FFWD Button
    pygame.draw.rect(screen, "black", (845, 390, 75, 50), 3)    # RWND Button

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
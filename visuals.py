# Example file showing a basic pygame "game loop"
import pygame
import pygame_widgets
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox

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
    pygame.draw.circle(screen, "black", (x, y), 15, 3)              # bubble toggle option
    pygame.draw.rect(screen, "black", (x+30, y-25, 200, 50), 3)     # text box "Bubble Sort"
    pygame.draw.rect(screen, "black", (x+245, y-25, 125, 50), 3)    # Time Elapse variable
    if selected_algo == "bubble":
        pygame.draw.circle(screen, "green", (x, y), 15)

    pygame.draw.circle(screen, "black", (x, y+70), 15, 3)           # merge toggle option
    pygame.draw.rect(screen, "black", (x+30, y+45, 200, 50), 3)     # text box "Merge Sort"
    pygame.draw.rect(screen, "black", (x+245, y+45, 125, 50), 3)    # Time Elapse variable
    if selected_algo == "merge":
        pygame.draw.circle(screen, "green", (x, y+70), 15)

    pygame.draw.circle(screen, "black", (x, y+140), 15, 3)          # quick toggle option
    pygame.draw.rect(screen, "black", (x+30, y+115, 200, 50), 3)    # text box "Quick Sort"
    pygame.draw.rect(screen, "black", (x+245, y+115, 125, 50), 3)   # Time Elapse variable
    if selected_algo == "quick":
        pygame.draw.circle(screen, "green", (x, y+140), 15)

    pygame.draw.circle(screen, "black", (x, y+210), 15, 3)          # radix toggle option
    pygame.draw.rect(screen, "black", (x+30, y+185, 200, 50), 3)    # text box "Radix Sort"
    pygame.draw.rect(screen, "black", (x+245, y+185, 125, 50), 3)   # Time Elapse variable
    if selected_algo == "radix":
        pygame.draw.circle(screen, "green", (x, y+210), 15)

    pygame.draw.circle(screen, "black", (x, y+280), 15, 3)          # linear toggle option
    pygame.draw.rect(screen, "black", (x+30, y+255, 200, 50), 3)    # text box "Linear Search"
    pygame.draw.rect(screen, "black", (x+245, y+255, 125, 50), 3)   # Time Elapse variable
    if selected_algo == "linear":
        pygame.draw.circle(screen, "green", (x, y+280), 15)

# Function defining window to add Elements to algorithm
def elements(x, y):     # x = 30, y = 430
    # Option to set the size of the array
    pygame.draw.circle(screen, "black", (x, y), 15, 3)
    # pygame.draw.rect(screen, "black", (x+30, y-25, 120, 50), 3)
    # pygame.draw.rect(screen, "blue", (x+170, y-25, 100, 50), 3)

    # Option to randomly fill the array
    pygame.draw.circle(screen, "black", (x, y+70), 15, 3)
    # pygame.draw.rect(screen, "black", (x+30, y+40, 120, 50), 3)
    pygame.draw.circle(screen, "black", (x+210, y+70), 15, 3)
    # pygame.draw.rect(screen, "black", (x+245, y+40, 120, 50), 3)
    if selected_method == "random":
        pygame.draw.circle(screen, "green", (x, y+70), 15)
    elif selected_method == "manual":
        pygame.draw.circle(screen, "green", (x+210, y+70), 15)

    # Option to fill in the array manually
    pygame.draw.circle(screen, "black", (x, y+145), 15, 3)
    pygame.draw.rect(screen, "black", (x+30, y+115, 320, 50), 3)

    # Submit Button
    pygame.draw.rect(screen, "green", (x+90, y+195, 150, 50), 5)

#=============
# PYGAME MAIN
#=============
pygame.init()
screen = pygame.display.set_mode((1280, 720))

selected_algo = None
selected_method = None

def select_algo(name):
    global selected_algo
    selected_algo = name

def select_method(name):
    global selected_method
    selected_method = name

#===============
# CANVAS PLAYER
#===============
rewind = Button(screen, 640+185, 180+340, 75, 50, text="RWD", onClick=lambda: print("REWIND!"))
play_btn = Button(screen, 640+275, 180+340, 50, 50, text="Play", onClick=lambda: print("Play Button!"))
fforward = Button(screen, 640+340, 180+340, 75, 50, text="FFWD", onClick=lambda: print("FFORWARD!"))

#==============
# MENU LISTING
#==============

# Bubble Sort Listing
bubble_text = Button(
    screen, 
    30+30, 50-25, 200, 50, 
    text='Bubble Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("bubble")
    )
bubble_time = TextBox(screen, 30+245, 50-25, 125, 50)
bubble_time.disable()


# Merge Sort Listing
merge_text = Button(
    screen, 
    30+30, 50+45, 200, 50, 
    text='Merge Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("merge")
    )
merge_time = TextBox(screen, 30+245, 50+45, 125, 50)
merge_time.disable()


# Quick Sort Listing
quick_text = Button(
    screen, 
    30+30, 50+115, 200, 50, 
    text='Quick Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("quick")
    )
quick_time = TextBox(screen, 30+245, 50+115, 125, 50)
quick_time.disable()


# Radix Sort Listing
radix_text = Button(
    screen, 
    30+30, 50+185, 200, 50, 
    text='Radix Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("radix")
    )
radix_time = TextBox(screen, 30+245, 50+185, 125, 50)
radix_time.disable()


# Linear Sort Listing
linear_text = Button(
    screen, 
    30+30, 50+255, 200, 50, 
    text='Linear Search', 
    fontSize=25, 
    onClick=lambda: select_algo("linear")
    )
linear_time = TextBox(screen, 30+245, 50+255, 125, 50)
linear_time.disable()

#==========
# ELEMENTS
#==========
size_text = TextBox(screen, 30+30, 430-25, 125, 50, placeholderText="Array Size", fontSize=25)
size_submit = Button(screen, 30+170, 430-25, 100, 50, text='Enter', onClick=lambda: print('Array Entered!'))

rand_button = Button(
    screen, 
    30+30, 430+40, 120, 50, 
    text="Random", 
    radius=20, 
    onClick=lambda: select_method("random")
    )

man_button = Button(
    screen, 
    30+245, 430+40, 120, 50, 
    text="Manual", 
    radius=20, 
    onClick=lambda: select_method("manual")
    )

arr_text = TextBox(screen, 30+30, 430+115, 320, 50, placeholderText="1 2 3 4 5", fontSize=25)
submit_btn = Button(screen, 30+90, 430+195, 150, 50, text='SUBMIT', fontSize=25, radius=20, onClick=lambda: print('SUBMITTED'))
clock = pygame.time.Clock()
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    canvas_player(640, 180)
    menu_listing(30, 50)
    elements(30, 430)

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    # pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
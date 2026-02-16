# Sorting Algorithm Visualization with Pygame
import main
import random
import pygame
import pygame_widgets
from pygame_widgets.button import Button 
from pygame_widgets.textbox import TextBox
import time

# Visualization state variables
visualization_array = []
visualization_colors = []
visualization_running = False
visualization_paused = False
visualization_speed = 50  # milliseconds between frames
current_step = 0
sorting_steps = []  # Will store each step of the sorting process

# Color definitions for visualization
COLOR_DEFAULT = (100, 149, 237)  # Cornflower blue - default bar color
COLOR_COMPARING = (255, 255, 0)   # Yellow - bars being compared
COLOR_SWAPPING = (255, 69, 0)     # Red-Orange - bars being swapped
COLOR_SORTED = (50, 205, 50)      # Lime green - sorted bars
COLOR_PIVOT = (255, 0, 255)       # Magenta - pivot in quicksort

# Function to draw the visualization bars
def draw_visualization(x, y, width, height):
    """Draw animated bars showing the sorting process"""
    global visualization_array, visualization_colors
    
    if not visualization_array:
        # Draw empty canvas if no array
        pygame.draw.rect(screen, "white", (x, y, width, height))
        pygame.draw.rect(screen, "black", (x, y, width, height), 3)
        return
    
    # Draw white background
    pygame.draw.rect(screen, "white", (x, y, width, height))
    
    n = len(visualization_array)
    if n == 0:
        return
    
    # Calculate bar dimensions
    bar_width = (width - 20) / n  # Leave 10px padding on each side
    max_val = max(visualization_array) if visualization_array else 1
    
    # Draw each bar
    for i, val in enumerate(visualization_array):
        bar_height = (val / max_val) * (height - 40)  # Scale to fit canvas
        bar_x = x + 10 + (i * bar_width)
        bar_y = y + height - bar_height - 10
        
        # Get color for this bar
        color = visualization_colors[i] if i < len(visualization_colors) else COLOR_DEFAULT
        
        # Draw the bar
        pygame.draw.rect(screen, color, (bar_x, bar_y, bar_width - 2, bar_height))
        
    # Draw border
    pygame.draw.rect(screen, "black", (x, y, width, height), 3)

# Function defining the Visualization for the algorithms
def canvas_player(x, y):    # x= 660, y=50
    # Draw the visualization canvas
    draw_visualization(x, y, 600, 320)
    
    # Draw control buttons (outlines only, actual buttons handled by pygame_widgets)
    pygame.draw.rect(screen, "black", (x+275, y+340, 50, 50), 3)    # Play Button
    pygame.draw.rect(screen, "black", (x+340, y+340, 75, 50), 3)    # FFWD Button
    pygame.draw.rect(screen, "black", (x+185, y+340, 75, 50), 3)    # RWND Button

# Function defining the Menu listing
def menu_listing(x, y):     # x=30, y=50
    pygame.draw.circle(screen, "black", (x, y), 15, 3)              # bubble toggle option
    pygame.draw.rect(screen, "black", (x+30, y-25, 200, 50), 3)     # text box "Bubble Sort"
    pygame.draw.rect(screen, "black", (x+245, y-25, 225, 50), 3)    # Time Elapse variable
    if selected_algo == "bubble":
        pygame.draw.circle(screen, "green", (x, y), 15)

    pygame.draw.circle(screen, "black", (x, y+70), 15, 3)           # merge toggle option
    pygame.draw.rect(screen, "black", (x+30, y+45, 200, 50), 3)     # text box "Merge Sort"
    pygame.draw.rect(screen, "black", (x+245, y+45, 225, 50), 3)    # Time Elapse variable
    if selected_algo == "merge":
        pygame.draw.circle(screen, "green", (x, y+70), 15)

    pygame.draw.circle(screen, "black", (x, y+140), 15, 3)          # quick toggle option
    pygame.draw.rect(screen, "black", (x+30, y+115, 200, 50), 3)    # text box "Quick Sort"
    pygame.draw.rect(screen, "black", (x+245, y+115, 225, 50), 3)   # Time Elapse variable
    if selected_algo == "quick":
        pygame.draw.circle(screen, "green", (x, y+140), 15)

    pygame.draw.circle(screen, "black", (x, y+210), 15, 3)          # radix toggle option
    pygame.draw.rect(screen, "black", (x+30, y+185, 200, 50), 3)    # text box "Radix Sort"
    pygame.draw.rect(screen, "black", (x+245, y+185, 225, 50), 3)   # Time Elapse variable
    if selected_algo == "radix":
        pygame.draw.circle(screen, "green", (x, y+210), 15)

    pygame.draw.circle(screen, "black", (x, y+280), 15, 3)          # linear toggle option
    pygame.draw.rect(screen, "black", (x+30, y+255, 200, 50), 3)    # text box "Linear Search"
    pygame.draw.rect(screen, "black", (x+245, y+255, 225, 50), 3)   # Time Elapse variable
    if selected_algo == "linear":
        pygame.draw.circle(screen, "green", (x, y+280), 15)

# Function defining window to add Elements to algorithm
def elements(x, y):     # x = 30, y = 430
    # Option to set the size of the array
    pygame.draw.circle(screen, "black", (x, y), 15, 3)
    if selected_method == "random":
        pygame.draw.circle(screen, "green", (x, y), 15)
        pygame.draw.rect(screen, "black", (30+170, 430-25, 125, 50), 5)
        
    # Option to randomly fill the array
    pygame.draw.circle(screen, "black", (x, y+70), 15, 3)
    if selected_method == "manual":
        pygame.draw.circle(screen, "green", (x, y+70), 15)

    # Status indicator
    if status == "idle":
        pygame.draw.circle(screen, "black", (x, y+145), 15, 3)
    elif status == "sorting":
        pygame.draw.circle(screen, "yellow", (x, y+145), 15)
    elif status == "complete":
        pygame.draw.circle(screen, "green", (x, y+145), 15)
    pygame.draw.rect(screen, "black", (30+30, 430+115, 320, 50), 3)

    # Submit Button
    pygame.draw.rect(screen, "green", (x+90, y+195, 150, 50), 5)


def get_size():
    global arr_size
    arr_size = int(size_text.getText())
    return arr_size


def get_array():
    global rand_select
    oof = arr_text.getText()
    return list(map(int, oof.split()))


# Generator functions for animated sorting
def bubble_sort_visual(arr):
    """Generator that yields each step of bubble sort with color info"""
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            # Highlight bars being compared
            colors = [COLOR_DEFAULT] * n
            colors[j] = COLOR_COMPARING
            colors[j+1] = COLOR_COMPARING
            # Mark sorted section
            for k in range(n-i, n):
                colors[k] = COLOR_SORTED
            yield arr[:], colors
            
            if arr[j] > arr[j + 1]:
                # Highlight bars being swapped
                colors[j] = COLOR_SWAPPING
                colors[j+1] = COLOR_SWAPPING
                yield arr[:], colors
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Final state - all sorted
    colors = [COLOR_SORTED] * n
    yield arr[:], colors


def merge_sort_visual(arr, start=0):
    """Generator for merge sort visualization"""
    def merge_visual(arr, left, mid, right):
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1:right+1]
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            colors = [COLOR_DEFAULT] * len(arr)
            colors[k] = COLOR_COMPARING
            yield arr[:], colors
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            colors = [COLOR_DEFAULT] * len(arr)
            yield arr[:], colors
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            colors = [COLOR_DEFAULT] * len(arr)
            yield arr[:], colors
    
    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            yield from merge_sort_recursive(arr, left, mid)
            yield from merge_sort_recursive(arr, mid + 1, right)
            yield from merge_visual(arr, left, mid, right)
    
    yield from merge_sort_recursive(arr, 0, len(arr) - 1)
    colors = [COLOR_SORTED] * len(arr)
    yield arr[:], colors


def quick_sort_visual(arr):
    """Generator for quick sort visualization"""
    def partition_visual(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            colors = [COLOR_DEFAULT] * len(arr)
            colors[high] = COLOR_PIVOT  # Pivot
            colors[j] = COLOR_COMPARING  # Current element
            if i >= 0:
                colors[i] = COLOR_SWAPPING  # Partition boundary
            yield arr[:], colors
            
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                colors[i] = COLOR_SWAPPING
                colors[j] = COLOR_SWAPPING
                yield arr[:], colors
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = yield from partition_visual(arr, low, high)
            yield from quick_sort_recursive(arr, low, pi - 1)
            yield from quick_sort_recursive(arr, pi + 1, high)
    
    yield from quick_sort_recursive(arr, 0, len(arr) - 1)
    colors = [COLOR_SORTED] * len(arr)
    yield arr[:], colors


def radix_sort_visual(arr):
    """Generator for radix sort visualization"""
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        output = [0] * len(arr)
        count = [0] * 10
        
        # Count occurrences
        for i in range(len(arr)):
            digit = (arr[i] // exp) % 10
            count[digit] += 1
            colors = [COLOR_DEFAULT] * len(arr)
            colors[i] = COLOR_COMPARING
            yield arr[:], colors
        
        # Cumulative count
        for i in range(1, 10):
            count[i] += count[i-1]
        
        # Build output array
        i = len(arr) - 1
        while i >= 0:
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1
            colors = [COLOR_DEFAULT] * len(arr)
            colors[i] = COLOR_SWAPPING
            yield arr[:], colors
            i -= 1
        
        # Copy output to arr
        for i in range(len(arr)):
            arr[i] = output[i]
            colors = [COLOR_DEFAULT] * len(arr)
            colors[i] = COLOR_SORTED
            yield arr[:], colors
        
        exp *= 10
    
    colors = [COLOR_SORTED] * len(arr)
    yield arr[:], colors


def linear_search_visual(arr, target):
    """Generator for linear search visualization"""
    for i in range(len(arr)):
        colors = [COLOR_DEFAULT] * len(arr)
        colors[i] = COLOR_COMPARING
        yield arr[:], colors
        
        if arr[i] == target:
            colors[i] = COLOR_SORTED
            yield arr[:], colors
            return
    
    # Not found
    colors = [COLOR_DEFAULT] * len(arr)
    yield arr[:], colors


def start_visualization():
    """Initialize and start the sorting visualization"""
    global visualization_array, visualization_colors, visualization_running
    global sorting_steps, current_step, status
    
    status = "sorting"
    visualization_running = True
    current_step = 0
    sorting_steps = []
    
    # Get the array to sort
    if selected_method == "manual":
        arr = get_array()
    elif selected_method == "random":
        size = get_size()
        arr = [random.randint(10, 100) for _ in range(size)]
    else:
        return
    
    visualization_array = arr[:]
    visualization_colors = [COLOR_DEFAULT] * len(arr)
    
    # Generate all steps based on selected algorithm
    if selected_algo == "bubble":
        sorting_steps = list(bubble_sort_visual(arr[:]))
    elif selected_algo == "merge":
        sorting_steps = list(merge_sort_visual(arr[:]))
    elif selected_algo == "quick":
        sorting_steps = list(quick_sort_visual(arr[:]))
    elif selected_algo == "radix":
        sorting_steps = list(radix_sort_visual(arr[:]))
    elif selected_algo == "linear":
        target = arr[len(arr)//2] if arr else 0  # Search for middle element
        sorting_steps = list(linear_search_visual(arr[:], target))
    else:
        status = "idle"
        return


def update_visualization():
    """Update visualization to next step"""
    global current_step, visualization_array, visualization_colors
    global visualization_running, status
    
    if not visualization_running or not sorting_steps:
        return
    
    if current_step < len(sorting_steps):
        visualization_array, visualization_colors = sorting_steps[current_step]
        current_step += 1
    else:
        visualization_running = False
        status = "complete"
        # Show final sorted array
        final_arr.setText(str(visualization_array))


def run_algos():
    """Run all algorithms and measure timing (original function for timing comparison)"""
    global status
    
    if selected_method == "manual":
        main_arr = get_array()
    elif selected_method == "random":
        rand_arr_size = get_size()
        main_arr = [random.randint(1, 100) for _ in range(rand_arr_size)]
    else:
        return

    time_bub, sorted_bub = main.perform_bubble_sort(main_arr.copy())
    bubble_time_result.setText(f"{time_bub:.8f} s")

    time_merg, sorted_merg = main.perform_merge_sort(main_arr.copy())
    merge_time_result.setText(f"{time_merg:.8f} s")

    time_quic, sorted_quic = main.perform_quick_sort(main_arr.copy())
    quick_time_result.setText(f"{time_quic:.8f} s")

    time_rad, sorted_rad = main.perform_radix_sort(main_arr.copy())
    radix_time_result.setText(f"{time_rad:.8f} s")

    time_lin = main.perform_linear_search(main_arr.copy())
    linear_time_result.setText(f"{time_lin:.8f} s")

    final_arr.setText(str(sorted_bub))


def enable_size():
    size_text.enable()
    size_text.show()


def disable_size():
    size_text.disable()
    size_text.hide()
    size_text.setText("")


def enable_array():
    arr_text.enable()
    arr_text.show()
    

def disable_array():
    arr_text.disable()
    arr_text.hide()
    arr_text.setText("")


def pause_visualization():
    global visualization_paused
    visualization_paused = not visualization_paused


def reset_visualization():
    global visualization_running, visualization_paused, current_step, status
    global visualization_array, visualization_colors, sorting_steps
    visualization_running = False
    visualization_paused = False
    current_step = 0
    status = "idle"
    visualization_array = []
    visualization_colors = []
    sorting_steps = []


#=============
# PYGAME MAIN
#=============
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sorting Algorithm Visualizer")

selected_algo = None
selected_method = "random"
arr_size = None
rand_select = False
status = "idle"

def select_algo(name):
    global selected_algo
    selected_algo = name

def select_method(name):
    global selected_method
    selected_method = name

    if name == "random":
        disable_array()
        enable_size()

    elif name == "manual":
        disable_size()
        enable_array()

#===============
# CANVAS PLAYER
#===============
rewind = Button(screen, 640+185, 180+340, 75, 50, text="Reset", onClick=reset_visualization)
play_btn = Button(screen, 640+275, 180+340, 50, 50, text="Play", onClick=start_visualization)
fforward = Button(screen, 640+340, 180+340, 75, 50, text="Pause", onClick=pause_visualization)

#==============
# MENU LISTING
#==============
# Bubble Sort Listing
bubble_text = Button(
    screen, 
    60, 25, 200, 50, 
    text='Bubble Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("bubble")
    )
bubble_time_result = TextBox(screen, 30+245, 50-25, 225, 50, fontSize=14)


# Merge Sort Listing
merge_text = Button(
    screen, 
    60, 95, 200, 50, 
    text='Merge Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("merge")
    )
merge_time_result = TextBox(screen, 30+245, 50+45, 225, 50, fontSize=14)


# Quick Sort Listing
quick_text = Button(
    screen, 
    30+30, 50+115, 200, 50, 
    text='Quick Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("quick")
    )
quick_time_result = TextBox(screen, 30+245, 50+115, 225, 50, fontSize=14)


# Radix Sort Listing
radix_text = Button(
    screen, 
    30+30, 50+185, 200, 50, 
    text='Radix Sort', 
    fontSize=25, 
    onClick=lambda: select_algo("radix")
    )
radix_time_result = TextBox(screen, 30+245, 50+185, 225, 50, fontSize=14)


# Linear Search Listing
linear_text = Button(
    screen, 
    30+30, 50+255, 200, 50, 
    text='Linear Search', 
    fontSize=25, 
    onClick=lambda: select_algo("linear")
    )
linear_time_result = TextBox(screen, 30+245, 50+255, 225, 50, fontSize=14)

#==========
# ELEMENTS
#==========
size_text = TextBox(screen, 30+170, 430-25, 125, 50, placeholderText="Array Size", fontSize=25)

rand_button = Button(
    screen, 
    30+30, 430-25, 120, 50,
    text="Random", 
    radius=20, 
    onClick=lambda: select_method("random")
    )

man_button = Button(
    screen, 
    30+30, 430+40, 120, 50,
    text="Manual", 
    radius=20, 
    onClick=lambda: select_method("manual")
    )

arr_text = TextBox(screen, 30+170, 430+40, 320, 50, placeholderText="1 2 3 4 5", fontSize=25)

final_arr = TextBox(screen, 60, 545, 500, 150, fontSize=20)

submit_btn = Button(
    screen, 
    575, 590, 150, 50, 
    text='TIME ALL', 
    fontSize=20, 
    radius=20, 
    onClick=lambda: run_algos())

enable_size()
disable_array()


clock = pygame.time.Clock()
running = True
last_update = pygame.time.get_ticks()

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

    # Update visualization at controlled speed
    current_time = pygame.time.get_ticks()
    if visualization_running and not visualization_paused:
        if current_time - last_update > visualization_speed:
            update_visualization()
            last_update = current_time

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
WIDTH = 800
HEIGHT = 600
text = True
cs = 5
def draw():
    global text
    if text:
        screen.blit('background', pos=(0, 0))
        screen.draw.text('press c to start', pos=(300, 300), color='orange', fontsize=50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
current_color = BLACK
def clear_canvas():
    global text
    screen.clear()
    screen.blit('paint', pos=(0, 0))
    text = False
def set_color(color):
    global current_color
    current_color = color
def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        draw_circle(pos)
    elif button == mouse.RIGHT:
        draw_white(pos)
def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
        draw_circle(pos)
    elif mouse.RIGHT in buttons:
        draw_white(pos)
def draw_circle(pos):
    x, y = pos
    screen.draw.filled_circle((x, y), cs, current_color)
def draw_white(pos):
    x, y = pos
    screen.draw.filled_circle((x, y), cs, 'white')
def update():
    global cs
    if keyboard.up:
        cs += 1
        print(cs)
    if keyboard.down:
        cs -= 1
        print(cs)
def on_key_down(key):
    global cs
    if key == keys.C:
        clear_canvas()
    elif key == keys.R:
        set_color(RED)
    elif key == keys.G:
        set_color(GREEN)
    elif key == keys.B:
        set_color(BLUE)
    elif key == keys.Y:
        set_color(YELLOW)
    elif key == keys.O:
        set_color(ORANGE)
    elif key == keys.P:
        set_color(PURPLE)
    elif key == keys.K:
        set_color(BLACK)

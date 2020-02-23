import tcod, tcod.event
import random

def Of(t, func):
    if not (type(t) == "string"):
        raise Exception("string")

    def wrapper():
        pass
    return wrapper

def writestr(x: int, y: int, value: str) -> None:
    for i in range(len(value)):
        c: chr = value[i]
        tcod.console_put_char(0, x+i, y, c)
    tcod.console_flush()

def update():
    pass

def render():
    # Clear
    tcod.console_set_default_foreground(0, tcod.white)

    # Draw Here

    # Display
    tcod.console_flush()

def handleEvent(e):
    if e.type == "QUIT":
        raise SystemExit()

def main():
    screen_width = 100
    screen_height = 100

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    tcod.console_init_root(screen_width, screen_height, 'BEST GAME', False)

    tcod

    while not tcod.console_is_window_closed():
        # Main loop

        for e in tcod.event.wait():
            handleEvent(e)
        
        render()

if __name__ == '__main__':
    main()
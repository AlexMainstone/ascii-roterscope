import sys, random, os, time
import tcod
import math
from random import randrange
from PIL import Image

# GREYSCALE = """$xB%8&WM#*oahkbscalewmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`"""
GREYSCALE = """"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. """

def grey2ascii(x, scale=GREYSCALE):
    if x[1] == 0:
        return chr(32)
    return scale[math.floor(x[0] / 255 * len(scale))-1]

def img_to_ascii(path, res):
    im = Image.open(path).convert('LA').resize((res[0], res[1]))

    out_image = []
    for x in range(0, res[0]):
        out_image.append([])
        for y in range(0, res[1]):
            gvalue = im.getpixel((x, y))
            out_image[x].append(grey2ascii(gvalue))
    im.close()
    return out_image

def video_to_ascii(path, res):
    ascii_video = []

    for file in os.listdir(path):
        ascii_video.append(img_to_ascii(path + file, res))

    return ascii_video

def main():
    screen_width = 160
    screen_height = 90

    video = video_to_ascii("res/animation/", (screen_width, screen_height))
    frame = 0

    tcod.console_set_custom_font('res/Terbert10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_ASCII_INROW)
    cnsl = tcod.console_init_root(screen_width, screen_height, 'Ascii-Roterscope', False)

    start_time = time.clock()
    frame_gap = 0.1
    while not tcod.console_is_window_closed():
        # Main loop
        if time.clock() - start_time > frame_gap:
            tcod.console_flush()
            cnsl.clear()
            start_time = time.clock();

            frame+=1
            if(frame >= len(video)):
                frame = 0
            for x in range(0, screen_width):
                for y in range(0, screen_height):
                    # cnsl.default_fg = (randrange(0,255), randrange(0, 255), randrange(0,255))
                    # cnsl.default_fg = (255, 255, 255)
                    if video[frame][x][y] != ' ':
                        tcod.console_put_char(0, x, y, video[frame][x][y], tcod.BKGND_SET)
                        # tcod.console_set_char_background(0, x, y, (25, 25, 25))


        key = tcod.console_check_for_keypress()

        if key.vk == tcod.KEY_ESCAPE:
            return True

if __name__ == '__main__':
    main()
import sys, random, os, time
import tcod
import math
from random import randrange
from PIL import Image

# the 'darkness' of each character
GREYSCALE = """"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. """

# Converts 255 value to ascii
def grey2ascii(x, scale=GREYSCALE):
    if x[1] == 0:
        return chr(32) #if transparent return 0
    return scale[math.floor(x[0] / 255 * len(scale))-1]

# Converts image to ascii
def img_to_ascii(path, res):
    # Load Image
    im = Image.open(path).resize((res[0], res[1]))
    im_gs = im.convert('LA')

    # Get each ascii pixel
    out_image = []
    for x in range(0, res[0]):
        out_image.append([])
        for y in range(0, res[1]):
            gvalue = im_gs.getpixel((x, y))
            out_image[x].append([grey2ascii(gvalue), im.getpixel((x, y))])

    # Tidy
    im.close()
    im_gs.close()

    return out_image

# Run img-to_ascii for each image in a folder
def video_to_ascii(path, res):
    ascii_video = []

    for file in sorted(os.listdir(path)):
        ascii_video.append(img_to_ascii(path + file, res))

    return ascii_video

def main():
    # resolution
    screen_width = 160
    screen_height = 120

    # Load video data
    video = video_to_ascii("res/jermanimation2/", (screen_width, screen_height))
    # Current frame
    frame = 0


    # setup console
    tcod.console_set_custom_font('res/Terbert10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_ASCII_INROW)
    cnsl = tcod.console_init_root(screen_width, screen_height, 'Ascii-Roterscope', False)

    # Frame clock
    start_time = time.process_time()
    frame_gap = 0.03

    # Main loop
    while not tcod.console_is_window_closed():
        # if time to change frame
        if time.clock() - start_time > frame_gap:
            # Clear console
            tcod.console_flush()
            cnsl.clear()

            # reset clock
            start_time = time.clock();

            # Change frame
            frame+=1
            # Reset video
            if(frame >= len(video)):
                frame = 0
            
            # draw to screen
            for x in range(0, screen_width):
                for y in range(0, screen_height):
                    if video[frame][x][y][0] != ' ': #if transparent
                        # Set Color
                        cnsl.default_fg = (video[frame][x][y][1][0], video[frame][x][y][1][1], video[frame][x][y][1][2])
                        # Draw character
                        tcod.console_put_char(0, x, y, video[frame][x][y][0], tcod.BKGND_SET)


        # Get key
        key = tcod.console_check_for_keypress()
        # Close on escape
        if key.vk == tcod.KEY_ESCAPE:
            return True

if __name__ == '__main__':
    main()
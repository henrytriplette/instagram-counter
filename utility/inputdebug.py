#!/usr/bin/env python

import sys, os, pygame
from pygame import *

ImgOnOff = []
Font = None
LastKey = None

# Set screen size
size = width, height = 128, 128

def showtext(screen, pos, text, color, bgcolor):
    textimg = Font.render(text, 1, color, bgcolor)
    screen.blit(textimg, pos)
    return pos[0] + textimg.get_width() + 5, pos[1]

def drawstatus(screen):
    bgcolor = 50, 50, 50
    screen.fill(bgcolor, (0, 0, 128, 60))

    pos = showtext(screen, (5, 10), 'Keyboard', (255, 255, 255), bgcolor)
    screen.blit(ImgOnOff[key.get_focused()], pos)

    pos = showtext(screen, (5, 30), 'Key', (255, 255, 255), bgcolor)
    if LastKey:
        p = '%d, %s' % (LastKey, key.name(LastKey))
    else:
        p = 'None'
    pos = showtext(screen, pos, p, bgcolor, (255, 255, 55))

def drawhistory(screen, history):
    screen.blit(Font.render('Event History Area', 1, (155, 155, 155), (0,0,0)), (2, 132))
    ypos = 60
    h = list(history)
    h.reverse()
    for line in h:
        r = screen.blit(line, (10, ypos))
        screen.fill(0, (r.right, r.top, 68, r.height))
        ypos -= Font.get_height()


def main():
    #Change display to tft screen
    os.environ["SDL_FBDEV"] = "/dev/fb1"

    pygame.init()

    #Disable mouse pointer
    pygame.mouse.set_visible(False)

    #Set screen size
    size = width, height = 128,128
    screen = pygame.display.set_mode(size)

    global Font
    Font = pygame.font.Font(None, 20)

    global ImgOnOff
    ImgOnOff.append(Font.render("Off", 1, (0, 0, 0), (255, 50, 50)))
    ImgOnOff.append(Font.render("On", 1, (0, 0, 0), (50, 255, 50)))

    history = []

    #let's turn on the joysticks just so we can play with em
    for x in range(joystick.get_count()):
        j = joystick.Joystick(x)
        j.init()
        txt = 'Joystick: ' + j.get_name()
        img = Font.render(txt, 1, (50, 200, 50), (0, 0, 0))
        history.append(img)
    if not joystick.get_count():
        img = Font.render('No Joysticks', 1, (50, 200, 50), (0, 0, 0))
        history.append(img)

    going = True
    while going:
        for e in event.get():
            if e.type == QUIT:
                going = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    going = False
                else:
                    global LastKey
                    LastKey = e.key
            if e.type == VIDEORESIZE:
                screen = pygame.display.set_mode(e.size, RESIZABLE)

        drawstatus(screen)
        drawhistory(screen, history)

        pygame.display.flip()
        time.wait(10)

    quit()


if __name__ == '__main__':
    main()

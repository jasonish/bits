# /usr/bin/env python

# Simple script that will take an argument of "left" or "right" and an
# X coordinate to output a MoveToScreen command that will move a
# window to the left or right screen.  If already on the left-most
# screen, it will be moved to the furthest right screen.
#
# Requires that you are running your multiple displays as one giant
# desktop (ie: Xinerama).  This will not move windows between 2
# independent X displays.

import sys

# The width of your screens.  This script will need to be adapted if
# you have screens of different widths.
screenWidth = 1920

# The ordering of your screens as X seems them.  In my case my left
# most screen is X display 2, the center screen is X display 0 and the
# rightmost screen is X display 1.
screens = [2, 0, 1]

numScreens = len(screens)

def main():
    
    what = sys.argv[1]
    if what not in ["left", "right"]:
        print "Invalid argument."
        return 1

    x = float(sys.argv[2])

    currentScreen = int((x / (screenWidth * numScreens)) * numScreens)
    if what == "left":
        screen = (currentScreen - 1) % numScreens
    elif what == "right":
        screen = (currentScreen + 1) % numScreens

    print "MoveToScreen %d" % screens[screen]

    return 0

if __name__ == "__main__":
    sys.exit(main())


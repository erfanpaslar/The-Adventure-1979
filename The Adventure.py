import os
import random
import pygame
import time
from math import sqrt

# Class for the orange dude


class Player(object):

    def __init__(self, x, y, width, height):  # first_x first_y width height
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect


class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)


class Bridge(object):
    def __init__(self, pos):
        bridges.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)


class BridgeOnBack(object):
    def __init__(self, pos):
        bridgesb.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)


class HalfH(object):
    def __init__(self, pos):
        half_Hs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 25, 50)


class Halfh(object):
    def __init__(self, pos):
        half_hs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 25, 50)


class LineL(object):
    def __init__(self, pos):
        walls.append(self)
        lineLs.append(self)
        self.rect = pygame.Rect(pos[0]+25, pos[1], 3, 50)


class Linel(object):
    def __init__(self, pos):
        linels.append(self)
        self.rect = pygame.Rect(pos[0]-25, pos[1], 3, 50)


# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")  # title
screen = pygame.display.set_mode((1000, 600))  # scale
# gray = (150, 150, 150)
gray = (60, 60, 60)

clock = pygame.time.Clock()
walls = []  # List to hold the walls
bridges = []
littles = []
half_Hs = []
half_hs = []
lineLs = []
linels = []
bridgesb = []

player = Player(500-12, 600-100, 25, 25)  # Create the player

enemyX = 300
enemyY = 300

yellowKeyX = 150
yellowKeyY = 150

blackKeyX = 150
blackKeyY = 150

yellowGateFlag = 0
blackGateFlag = 0

yellowArrowX = 150
yellowArrowY = 150

cupX = 150
cupY = 150

bridgeX = 275
bridgeY = 325

levelYellowUp = [
    "                      ",
    " WWWWWWWWWWWWWWWWWWWW ",
    "E                    E",
    "E                    E",
    " WWWWW WWWWWWWW WWWWW ",
    " WWWWW WWWWWWWW WWWWW ",
    " WW       WW       WW ",
    " WW       WW       WW ",
    " WW WWWWW WW WWWWW WW ",
    " WW WWWWW WW WWWWW WW ",
    "E   W   W WW W   W   E",
    "E   W   W WW W   W   E",
    " WWWW W W WW W W WWWW ",
    "     E E E  E E E    "
]

levelBlueLeft = [
    "WWWWWWWWWWWWWWWWWWWW",
    "                    ",
    "                    ",
    "WWWWW WWWWWWWW WWWWW",
    "WWWWW WWWWWWWW WWWWW",
    "WW       WW       WW",
    "WW       WW       WW",
    "WW WWWWW WW WWWWW WW",
    "WW WWWWW WW WWWWW WW",
    "   W   W WW W   W   ",
    "   W   W WW W   W   ",
    "WWWW W W WW W W WWWW"
]

levelBlueRight = [
    "WWWW W W WW W W WWWW",
    "   W W W    W W W   ",
    "   W W W    W W W   ",
    "WW W W WWWWWW W W WW",
    "WW W W WWWWWW W W WW",
    "   W W        W W   ",
    "   W W        W W   ",
    "WWWW WWWWWWWWWW WWWW",
    "WWWW WWWWWWWWWW WWWW",
    "                    ",
    "                    ",
    "WWWWWWWW    WWWWWWWW"
]

levelBlueCenter = [
    "WW W WWWW  WWWW W WW",
    "   W   WW  WW   W   ",
    "   W   WW  WW   W   ",
    "WWWWWW WW  WW WWWWWW",
    "WWWWWW WW  WW WWWWWW",
    "     W WW  WW W     ",
    "     W WW  WW W     ",
    "WW W W WW  WW W W WW",
    "WW W W WW  WW W W WW",
    "   W W W    W W W   ",
    "   W W W    W W W   ",
    "WWWW W W    W W WWWW"
]

levelBlueDown = [
    "WWWW W W    W W WWWW",
    "   W   W    W   W   ",
    "   W   W    W   W   ",
    "WW WWWWW    WWWWW WW",
    "WW WWWWW    WWWWW WW",
    "WW                WW",
    "WW                WW",
    "WWWW            WWWW",
    "WWWW            WWWW",
    "   W            W   ",
    "   W            W   ",
    "WWWWWWWWWWWWWWWWWWWW"
]

levelBlueUp = [
    "WWWWBWWW    WWWBWWWW",
    "    W  W    W  W    ",
    "    W  W    W  W    ",
    "WW  W  WW  WW  W  WW",
    "WW  W  WW  WW  W  WW",
    "WW  W          W  WW",
    "WW  W          W  WW",
    "WWWWWWbbW  WWWWWWWWW",
    "WWWWWWbbW  WWWWWWWWW",
    "   W    W  W    W   ",
    "   W    W  W    W   ",
    "WW W WWWW  WWWW W WW"
]

levelYellowDownAndBlack = [
    "WWWWWhhh    HHHWWWWW",
    "W    WWW    WWW    W",
    "W    WWW    WWW    W",
    "W    WWWWBBWWWW    W",
    "W    WWWWBBWWWW    W",
    "W     WWWBBWWW     W",
    "W     WWWBBWWW     W",
    "W     WWW  WWW     W",
    "W     WWW  WWW     W",
    "W                  W",
    "W                  W",
    "WWWWWWWW    WWWWWWWW"
]

levelYellowUpAndPurple = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "WWWWWWWW    WWWWWWWW"
]

levelOrangeDown = [
    "WWWWWWWW    WWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW"
]

levelOrangeUp = [
    "WWWWWWWW    WWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "WWWWWWWW    WWWWWWWW"
]

levelGreenCenter = [
    "WWWWWWWW    WWWWWWWW",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "WWWWWWWWWWWWWWWWWWWW"
]

levelGreenLeft = [
    "WWWWWWWW    WWWWWWWW",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "L                   ",
    "WWWWWWWWWWWWWWWWWWWW"
]

levelGreenRight = [
    "WWWWWWWWWWWWWWWWWWWW",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "                   L",
    "WWWWWWWW    WWWWWWWW"
]

########COLORS#########
blue = (0, 0, 255)
yellow = (255, 255, 0)
darkGreen = (46, 225, 110)
green = (34, 177, 76)
lightGreen = (188, 255, 129)
black = (0, 0, 0)
orange = (255, 128, 64)
purple = (163, 73, 164)

colors = [blue, yellow, darkGreen, orange, purple, black, lightGreen]
#####level Ditails##########
yellowDown = []
yellowUp = []
greenCenter = []
greenRight = []
greenLeft = []
orangeDown = []
blueRight = []
blueCenter = []
blueDown = []
blueLeft = []
blueUp = []
orangeUp = []
blackUp = []
purpleUp = []

# yellowDown += [levelYellowDownAndBlack,yellow,yellowDown , levelYellowDownAndBlack,yellow,yellowDown ,  levelYellowUpAndPurple,yellow,yellowUp , levelGreenCenter,darkGreen,greenCenter,0,0]
# yellowUp   += [levelYellowUpAndPurple,yellow,yellowUp, levelYellowUpAndPurple,yellow,yellowUp , levelYellowDownAndBlack,yellow,yellowDown , levelYellowDownAndBlack,yellow,yellowDown,0,0]
# greenCenter+= [levelGreenLeft,lightGreen,greenLeft , levelGreenRight,green,greenRight , levelYellowDownAndBlack,yellow,yellowDown , levelGreenCenter,darkGreen,greenCenter,0,0]
# greenRight += [levelGreenCenter,darkGreen,greenCenter , levelGreenRight,green,greenRight , levelGreenRight,green,greenRight , levelOrangeDown,orange,orangeDown ,0,0]
# greenLeft  += [levelGreenLeft,lightGreen,greenLeft , levelGreenCenter,darkGreen,greenCenter , levelBlueRight,blue,blueRight , levelGreenLeft,lightGreen,greenLeft,1,1]
# orangeDown += [levelOrangeDown,orange,orangeDown , levelOrangeDown,orange,orangeDown , levelGreenRight,green,greenRight , levelOrangeDown,orange,orangeDown, 1,1]
# blueRight  += [levelBlueCenter,blue,blueCenter , levelBlueCenter,blue,blueCenter , levelBlueLeft,blue,blueLeft , levelGreenLeft,darkGreen,greenLeft,0,0]
# blueCenter += [levelBlueRight,blue,blueRight , levelBlueRight,blue,blueRight , levelBlueUp,blue,blueUp , levelBlueDown,blue,blueDown,0,0]
# blueDown   += [levelBlueLeft,blue,blueLeft, levelBlueUp,blue,blueUp , levelBlueCenter,blue,blueCenter , levelBlueDown,blue,blueDown,0,0]
# blueLeft   += [levelBlueUp,blue,blueUp , levelBlueDown,blue,blueDown , levelBlueLeft,blue,blueLeft , levelBlueRight,blue,blueRight,0,0]
# blueUp     += [levelBlueDown,blue,blueDown , levelBlueLeft,blue,blueLeft , levelOrangeUp,orange,orangeUp , levelBlueCenter,blue,blueCenter,0,0]
# orangeUp   += [levelOrangeUp,orange,orangeUp , levelOrangeUp,orange,orangeUp , levelYellowDownAndBlack,black,blackUp , levelBlueUp,blue,blueUp,0,0]
# blackUp    += [levelYellowDownAndBlack,black,blackUp , levelYellowDownAndBlack,black,blackUp , levelYellowUpAndPurple,purple,purpleUp , levelOrangeUp,orange,orangeUp,0,0]
# purpleUp   += []


# 0:left lvl, 1:left lvl color, 2:right lvl name  3:right lvl, 4:left lvl color, 5:right lvl name  6:up lvl, 7:up lvl color, 8:up lvl name  9:down lvl, 10:down lvl color, 11:down lvl name  12:enemy 13:enemy Fixed
yellowDown += [{"lvlName": levelYellowDownAndBlack, "color": yellow, "listName": yellowDown}, {"lvlName": levelYellowDownAndBlack, "color": yellow,   "listName": yellowDown}, {"lvlName": levelYellowUpAndPurple, "color": yellow,
                                                                                                                                                                                "listName": yellowUp}, {"lvlName": levelGreenCenter,       "color": darkGreen, "listName": greenCenter}, {"enemy": 0, "enemyFixed": 0, "key": "yellowKey", "arrow": False, "cup": False, "levelName": "yellowDown", "openGates": {"yellow": False, "black": False}}]
yellowUp += [{"lvlName": levelYellowUpAndPurple, "color": yellow, "listName": yellowUp}, {"lvlName": levelYellowUpAndPurple, "color": yellow,   "listName": yellowUp}, {"lvlName": levelYellowDownAndBlack,
                                                                                                                                                                        "color": yellow, "listName": yellowDown}, {"lvlName": levelYellowDownAndBlack, "color": yellow,    "listName": yellowDown}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": "yellow", "cup": False, "levelName": "yellowUp"}]
greenCenter += [{"lvlName": levelGreenLeft, "color": lightGreen, "listName": greenLeft}, {"lvlName": levelGreenRight,        "color": green,    "listName": greenRight}, {"lvlName": levelYellowDownAndBlack,
                                                                                                                                                                          "color": yellow, "listName": yellowDown}, {"lvlName": levelGreenCenter,       "color": darkGreen, "listName": greenCenter}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "greenCenter"}]
greenRight += [{"lvlName": levelGreenCenter, "color": darkGreen, "listName": greenCenter}, {"lvlName": levelGreenRight,        "color": green,    "listName": greenRight}, {"lvlName": levelGreenRight,
                                                                                                                                                                            "color": green, "listName": greenRight}, {"lvlName": levelOrangeDown,        "color": orange,    "listName": orangeDown}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "greenRight"}]
greenLeft += [{"lvlName": levelGreenLeft, "color": lightGreen, "listName": greenLeft}, {"lvlName": levelGreenCenter,       "color": darkGreen, "listName": greenCenter}, {"lvlName": levelBlueRight,
                                                                                                                                                                          "color": blue,  "listName": blueRight}, {"lvlName": levelGreenLeft,         "color": lightGreen, "listName": greenLeft}, {"enemy": 1, "enemyFixed": 1, "key": False, "arrow": False, "cup": False, "levelName": "greenLeft"}]
orangeDown += [{"lvlName": levelOrangeDown, "color": orange,    "listName": orangeDown}, {"lvlName": levelOrangeDown,        "color": orange,   "listName": orangeDown}, {"lvlName": levelGreenRight,
                                                                                                                                                                          "color": green, "listName": greenRight}, {"lvlName": levelOrangeDown,        "color": orange,    "listName": orangeDown}, {"enemy": 1, "enemyFixed": 1, "key": "blackKey", "arrow": False, "cup": False, "levelName": "orangeDown"}]
blueRight += [{"lvlName": levelBlueCenter,        "color": blue,      "listName": blueCenter}, {"lvlName": levelBlueCenter,        "color": blue,     "listName": blueCenter}, {"lvlName": levelBlueLeft,
                                                                                                                                                                                "color": blue,  "listName": blueLeft}, {"lvlName": levelGreenLeft,         "color": darkGreen, "listName": greenLeft}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blueRight"}]
blueRight += [{"lvlName": levelBlueCenter, "color": blue,      "listName": blueCenter}, {"lvlName": levelBlueCenter,        "color": blue,     "listName": blueCenter}, {"lvlName": levelBlueLeft,
                                                                                                                                                                         "color": blue,  "listName": blueLeft}, {"lvlName": levelGreenLeft,         "color": darkGreen, "listName": greenLeft}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blueRight"}]
blueCenter += [{"lvlName": levelBlueRight, "color": blue,      "listName": blueRight}, {"lvlName": levelBlueRight,         "color": blue,     "listName": blueRight}, {"lvlName": levelBlueUp,
                                                                                                                                                                       "color": blue,  "listName": blueUp}, {"lvlName": levelBlueDown,          "color": blue,      "listName": blueDown}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blueCenter"}]
blueDown += [{"lvlName": levelBlueLeft, "color": blue,      "listName": blueLeft}, {"lvlName": levelBlueUp,            "color": blue,     "listName": blueUp}, {"lvlName": levelBlueCenter,
                                                                                                                                                                "color": blue,  "listName": blueCenter}, {"lvlName": levelBlueDown,          "color": blue,      "listName": blueDown}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blueDown"}]
blueLeft += [{"lvlName": levelBlueUp, "color": blue,      "listName": blueUp}, {"lvlName": levelBlueDown,          "color": blue,     "listName": blueDown}, {"lvlName": levelBlueLeft,
                                                                                                                                                              "color": blue,  "listName": blueLeft}, {"lvlName": levelBlueRight,         "color": blue,      "listName": blueRight}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blueLeft"}]
blueUp += [{"lvlName": levelBlueDown, "color": blue,      "listName": blueDown}, {"lvlName": levelBlueLeft,          "color": blue,     "listName": blueLeft}, {"lvlName": levelOrangeUp,
                                                                                                                                                                "color": orange, "listName": orangeUp}, {"lvlName": levelBlueCenter,        "color": blue,      "listName": blueCenter}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blueUp"}]
orangeUp += [{"lvlName": levelOrangeUp, "color": orange,    "listName": orangeUp}, {"lvlName": levelOrangeUp,          "color": orange,   "listName": orangeUp}, {"lvlName": levelYellowDownAndBlack,
                                                                                                                                                                  "color": black, "listName": blackUp}, {"lvlName": levelBlueUp,            "color": blue,      "listName": blueUp}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "orangeUp"}]
blackUp += [{"lvlName": levelYellowDownAndBlack, "color": black,     "listName": blackUp}, {"lvlName": levelYellowDownAndBlack, "color": black,    "listName": blackUp}, {"lvlName": levelYellowUpAndPurple, "color": purple,
                                                                                                                                                                          "listName": purpleUp}, {"lvlName": levelOrangeUp,          "color": orange,    "listName": orangeUp}, {"enemy": 0, "enemyFixed": 0, "key": False, "arrow": False, "cup": False, "levelName": "blackUp", "openGates": {"yellow": False, "black": False}}]
purpleUp += [{"lvlName": levelYellowUpAndPurple, "color": purple,    "listName": purpleUp}, {"lvlName": levelYellowUpAndPurple, "color": purple,   "listName": purpleUp}, {"lvlName": levelYellowUpAndPurple,
                                                                                                                                                                           "color": purple, "listName": purpleUp}, {"lvlName": levelYellowDownAndBlack, "color": black,     "listName": blackUp}, {"enemy": 0, "enemyFixed": 0, "key": False, "cup": "cup", "arrow": False, "levelName": "purpleUp"}]


things = {"key": None}


def main(lvlName, color, nextPossibleLevels):
    thereIsAEnemy = nextPossibleLevels[4]["enemy"]
    alwaysEnemy = nextPossibleLevels[4]["enemyFixed"]
    trapped = 0

    isYellowKey = 0
    isBlackKey = 0
    isArrow = 0
    isCup = 0
    gotYellowKeyFromTop = 0
    # gotYellowKeyFromDown=0
    gotBlackKeyFromTop = 0
    # gotBlackKeyFromDown=0
    gotArrow = 0
    gotCup = 0

    colorIndex = 0

    if nextPossibleLevels[4]["key"] == "yellowKey":
        isYellowKey = 1
    if nextPossibleLevels[4]["key"] == "blackKey":
        isBlackKey = 1

    if nextPossibleLevels[4]["arrow"] == "yellow":
        isArrow = 1
    if nextPossibleLevels[4]["cup"] == "cup":
        isCup = 1

    if things["key"] == "yellowKey":
        print("have yellow key")
        isYellowKey = 1
        gotYellowKeyFromTop = 1

    if things["key"] == "blackKey":
        print("have black key")
        isBlackKey = 1
        gotBlackKeyFromTop = 1

    if things["key"] == "arrow":
        print("have arrow")
        isArrow = 1
        gotArrow = 1

    if things["key"] == "cup":
        print("have cup")
        isCup = 1
        gotCup = 1

    x = 0
    y = 0
    ######## global vars ##########
    global walls
    walls = []
    global bridges
    bridges = []
    global littles
    littles = []
    global half_Hs
    half_Hs = []
    global half_hs
    half_hs = []
    global lineLs
    lineLs = []
    global linels
    linels = []
    global bridgesb
    bridgesb = []

    end_rect = []
    # * Drawing the level
    for row in lvlName:
        for col in range(len(row)):
            if row[col] == "W":  # 50x50 solid
                Wall((x, y))

            if row[col] == 'B':  # 50x50 not solid on Top
                Bridge((x, y))

            if row[col] == 'b':  # 50x50 not solid on back
                BridgeOnBack((x, y))

            if row[col] == 'H':  # 25x50 not solid
                HalfH((x, y))

            if row[col] == 'h':
                Halfh((x+25, y))

            if row[col] == "E":
                end_rect.append(pygame.Rect(x, y, 50, 50))

            if row[col] == "L":
                LineL((x, y))

            if row[col] == "l":
                Linel((x+50, y))

            x += 50
        y += 50
        x = 0  # at first was 0 but i changed it to -50 to start putting end_rect that doesn't shown

    # * Initializing images
    imgEnemy = pygame.image.load("images/enemy.png")
    imgGate = pygame.image.load("images/gate.png")

    if isYellowKey:  # it means the level has the yellow key
        imgYellowKey = pygame.image.load("images/yellowKey"+".png")
    if isBlackKey:
        imgBlackKey = pygame.image.load("images/blackKey"+".png")
    if isArrow:
        imgArrow = pygame.image.load("images/arrow.png")
    if isCup:
        imgCup = pygame.image.load("images/cup.png")

    def Imgs(x, y, Img):
        screen.blit(Img, (int(x), int(y)))

    global enemyY
    global enemyX
    global yellowKeyY
    global yellowKeyX
    global blackKeyY
    global blackKeyX
    global yellowArrowX
    global yellowArrowY
    global cupX
    global cupY
    global yellowGateFlag
    global blackGateFlag

    # * mainloop
    running = True
    while running:
        clock.tick(60)
        for e in pygame.event.get():  # this is all events i think
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        # Move the player if an arrow key is pressed
        # this is a tuple of all keys i think, and if the key not pressed the value is 0
        key = pygame.key.get_pressed()
        if not trapped:
            if key[pygame.K_LEFT]:
                player.move(-5, 0)
            if key[pygame.K_RIGHT]:
                player.move(5, 0)
            if key[pygame.K_UP]:
                player.move(0, -5)
            if key[pygame.K_DOWN]:
                player.move(0, 5)

        if player.rect[0] <= 0:
            player.move(990, 0)
            if enemyX < 200:
                nextPossibleLevels[0]["listName"][4]["enemy"] = 1
                enemyX = 1050
            # if i had the yellow key and also the next level had a yellow key should remove the next lvl's yellow key to avoid duplicate keys and just i have it in things.
            if ((gotYellowKeyFromTop) and isYellowKey) and nextPossibleLevels[4]["key"] == "yellowKey":
                nextPossibleLevels[4]["key"] = False
            if ((gotBlackKeyFromTop) and isBlackKey) and nextPossibleLevels[4]["key"] == "blackKey":
                nextPossibleLevels[4]["key"] = False
            if (gotArrow and isArrow) and nextPossibleLevels[4]["arrow"] == "yellow":
                nextPossibleLevels[4]["arrow"] = False
            if (gotCup and isCup) and nextPossibleLevels[4]["cup"] == "cup":
                nextPossibleLevels[4]["cup"] = False
            return(nextPossibleLevels[0]["lvlName"], nextPossibleLevels[0]["color"], nextPossibleLevels[0]["listName"])

        if player.rect[0] >= 1000:
            player.move(-990, 0)
            if 800 <= enemyX:
                nextPossibleLevels[1]["listName"][4]["enemy"] = 1
                enemyX = -50
            if ((gotYellowKeyFromTop) and isYellowKey) and nextPossibleLevels[4]["key"] == "yellowKey":
                nextPossibleLevels[4]["key"] = False
            if ((gotBlackKeyFromTop) and isBlackKey) and nextPossibleLevels[4]["key"] == "blackKey":
                nextPossibleLevels[4]["key"] = False
            if (gotArrow and isArrow) and nextPossibleLevels[4]["arrow"] == "yellow":
                nextPossibleLevels[4]["arrow"] = False
            if (gotCup and isCup) and nextPossibleLevels[4]["cup"] == "cup":
                nextPossibleLevels[4]["cup"] = False
            return(nextPossibleLevels[1]["lvlName"], nextPossibleLevels[1]["color"], nextPossibleLevels[1]["listName"])

        if player.rect[1] <= 0:
            player.move(0, 590)
            if enemyY < 200:
                nextPossibleLevels[2]["listName"][4]["enemy"] = 1
                enemyY = 650
            if ((gotYellowKeyFromTop) and isYellowKey) and nextPossibleLevels[4]["key"] == "yellowKey":
                nextPossibleLevels[4]["key"] = False
            if ((gotBlackKeyFromTop) and isBlackKey) and nextPossibleLevels[4]["key"] == "blackKey":
                nextPossibleLevels[4]["key"] = False
            if (gotArrow and isArrow) and nextPossibleLevels[4]["arrow"] == "yellow":
                nextPossibleLevels[4]["arrow"] = False
            if (gotCup and isCup) and nextPossibleLevels[4]["cup"] == "cup":
                nextPossibleLevels[4]["cup"] = False
            return(nextPossibleLevels[2]["lvlName"], nextPossibleLevels[2]["color"], nextPossibleLevels[2]["listName"])

        if player.rect[1] >= 600:
            player.move(0, -590)
            if 400 <= enemyY:
                nextPossibleLevels[3]["listName"][4]["enemy"] = 1
                enemyY = -50
            if ((gotYellowKeyFromTop) and isYellowKey) and nextPossibleLevels[4]["key"] == "yellowKey":
                nextPossibleLevels[4]["key"] = False
            if ((gotBlackKeyFromTop) and isBlackKey) and nextPossibleLevels[4]["key"] == "blackKey":
                nextPossibleLevels[4]["key"] = False
            if (gotArrow and isArrow) and nextPossibleLevels[4]["arrow"] == "yellow":
                nextPossibleLevels[4]["arrow"] = False
            if (gotCup and isCup) and nextPossibleLevels[4]["cup"] == "cup":
                nextPossibleLevels[4]["cup"] = False
            return(nextPossibleLevels[3]["lvlName"], nextPossibleLevels[3]["color"], nextPossibleLevels[3]["listName"])

        else:
            nextPossibleLevels[0]["listName"][4]["enemy"] = 0
            nextPossibleLevels[1]["listName"][4]["enemy"] = 0
            nextPossibleLevels[2]["listName"][4]["enemy"] = 0
            nextPossibleLevels[3]["listName"][4]["enemy"] = 0

        # * Changing Screen Color
        screen.fill((60, 60, 60))

        # * Enemy Moves
        if (thereIsAEnemy or alwaysEnemy):
            Imgs(enemyX, enemyY, imgEnemy)
            enemyDistance = sqrt(
                ((player.rect[0]-enemyX)**2 + (player.rect[1] - enemyY)**2))  # enemy distance

            if not trapped:
                if player.rect[0] >= enemyX:
                    if enemyDistance > 200:
                        enemyX += 1.5
                    enemyX += 2

                if player.rect[1] >= enemyY:
                    if enemyDistance > 200:
                        enemyY += 1.5
                    enemyY += 2

                if player.rect[0] <= enemyX:
                    if enemyDistance > 200:
                        enemyX -= 1.5
                    enemyX -= 2

                if player.rect[1] <= enemyY:
                    if enemyDistance > 200:
                        enemyY -= 1.5
                    enemyY -= 2

            # is enemy going to next page
            # if 0<= enemy.rect[0] <=200:
            #     nextPossibleLevels[12]=1
            # elif 800 <= enemy.rect[0] <=1000:
            #     nextPossibleLevels[12]=1
            # elif 0<= enemy.rect[1] <= 200:
            #     nextPossibleLevels[12]=1
            # elif 400<= enemy.rect[1] <=600:
            #     nextPossibleLevels[12]=1

            if 0 <= enemyX <= 200 or 800 <= enemyX <= 1000 or 0 <= enemyY <= 200 or 400 <= enemyY <= 600:
                nextPossibleLevels[4]["enemy"] = 1

        if (thereIsAEnemy or alwaysEnemy) and -20 < enemyX - player.rect[0] < 10 and -5 < enemyY-player.rect[1] < 20:
            # * trapped
            print("Trapped")
            player.rect[0] = int(enemyX)+13
            player.rect[1] = int(enemyY)+63
            trapped = 1

        # Just added this to make it slightly fun ;)
        for er in end_rect:
            if player.rect.colliderect(er):
                return 0
        #         raise (SystemExit, "You win!")#it rase an error and exit the game

        ############################################

        ############## keys(yellow and black) ###########
        #! if we didn't have the key the gate Should not be closed
        try:
            if not nextPossibleLevels[4]["openGates"]["yellow"] and (nextPossibleLevels[4]["levelName"] == "yellowDown" and things["key"] != "yellowKey" and 445 < player.rect[0] < 555 and 400 < player.rect[1] < 450):
                player.rect[1] = 451
            elif not nextPossibleLevels[4]["openGates"]["yellow"] and (nextPossibleLevels[4]["levelName"] == "yellowDown" and things["key"] == "yellowKey" and 445 < player.rect[0] < 555 and 400 < player.rect[1] < 450):
                nextPossibleLevels[4]["openGates"]["yellow"] = True

            if not nextPossibleLevels[4]["openGates"]["black"] and (nextPossibleLevels[4]["levelName"] == "blackUp" and things["key"] != "blackKey" and 445 < player.rect[0] < 555 and 400 < player.rect[1] < 450):
                player.rect[1] = 451
            elif not nextPossibleLevels[4]["openGates"]["black"] and (nextPossibleLevels[4]["levelName"] == "blackUp" and things["key"] == "blackKey" and 445 < player.rect[0] < 555 and 400 < player.rect[1] < 450):
                nextPossibleLevels[4]["openGates"]["black"] = True
        except:
            pass

        if isYellowKey:
            if -25 < player.rect[0]-yellowKeyX < 25:

                if -1 < player.rect[1]-yellowKeyY < 10:  # got key from the top
                    gotYellowKeyFromTop = 1
                    gotBlackKeyFromTop = 0
                    gotArrow = 0
                    gotCup = 0
                    if things["key"] == "blackKey":
                        nextPossibleLevels[4]["key"] = "blackKey"
                    if things["key"] == "arrow":
                        nextPossibleLevels[4]["arrow"] = "yellow"
                    elif things["key"] == "cup":
                        nextPossibleLevels[4]["cup"] = "cup"
                    things["key"] = "yellowKey"
            if gotYellowKeyFromTop:
                yellowKeyY = player.rect[1]-25
                yellowKeyX = player.rect[0]-1
            Imgs(yellowKeyX, yellowKeyY, imgYellowKey)

        if isBlackKey:
            if -25 < player.rect[0]-blackKeyX < 25:
                if -1 < player.rect[1]-blackKeyY < 10:  # got key from the top
                    gotYellowKeyFromTop = 0
                    gotBlackKeyFromTop = 1
                    gotArrow = 0
                    gotCup = 0
                    if things["key"] == "yellowKey":
                        nextPossibleLevels[4]["key"] = "yellowKey"
                    if things["key"] == "arrow":
                        nextPossibleLevels[4]["arrow"] = "yellow"
                    elif things["key"] == "cup":
                        nextPossibleLevels[4]["cup"] = "cup"
                    things["key"] = "blackKey"
            if gotBlackKeyFromTop:
                blackKeyY = player.rect[1]-25
                blackKeyX = player.rect[0]-1
            Imgs(blackKeyX, blackKeyY, imgBlackKey)

        if isArrow:
            if -25 < player.rect[0]-yellowArrowX < 25:
                if -1 < player.rect[1]-yellowArrowY < 10:  # got arrow from the top
                    gotYellowKeyFromTop = 0
                    gotBlackKeyFromTop = 0
                    gotArrow = 1
                    gotCup = 0
                    if things["key"] == "yellowKey":
                        nextPossibleLevels[4]["key"] = "yellowKey"
                    elif things["key"] == "blackKey":
                        nextPossibleLevels[4]["key"] = "blackKey"
                    elif things["key"] == "cup":
                        nextPossibleLevels[4]["cup"] = "cup"
                    things["key"] = "arrow"
            if gotArrow:
                yellowArrowY = player.rect[1]-25
                yellowArrowX = player.rect[0] - 1

            Imgs(yellowArrowX, yellowArrowY, imgArrow)

        if isCup:
            if -45 < player.rect[0]-cupX < 45:
                if -1 < player.rect[1]-cupY < 10:  # got arrow from the top
                    gotYellowKeyFromTop = 0
                    gotBlackKeyFromTop = 0
                    gotArrow = 0
                    gotCup = 1
                    if things["key"] == "yellowKey":
                        nextPossibleLevels[4]["key"] = "yellowKey"
                    elif things["key"] == "blackKey":
                        nextPossibleLevels[4]["key"] = "blackKey"
                    elif things["key"] == "arrow":
                        nextPossibleLevels[4]["arrow"] = "yellow"
                    things["key"] = "cup"
            if gotCup:
                cupY = player.rect[1]-45
                cupX = player.rect[0] - 5

            Imgs(cupX, cupY, imgCup)

        #################################################

        for bridgeb in bridgesb:
            pygame.draw.rect(screen, color, bridgeb.rect)

        pygame.draw.rect(screen, color, player.rect)
        if nextPossibleLevels[4]["levelName"] == "yellowDown":
            if yellowGateFlag or gotYellowKeyFromTop:
                Imgs(450+25, 300, imgGate)
                yellowGateFlag = 1
            else:
                Imgs(450+25, 350, imgGate)
        if nextPossibleLevels[4]["levelName"] == "blackUp":
            if blackGateFlag or gotBlackKeyFromTop:
                Imgs(450+25, 300, imgGate)
                blackGateFlag = 1
            else:
                Imgs(450+25, 350, imgGate)

        if (gotCup and nextPossibleLevels[4]["levelName"] == "yellowUp"):
            colorIndex += 1
            color = colors[colorIndex % len(colors)]
            trapped = 1
            time.sleep(.1)

        for wall in walls:
            pygame.draw.rect(screen, color, wall.rect)
        for bridge in bridges:
            pygame.draw.rect(screen, color, bridge.rect)
        for halfH in half_Hs:
            pygame.draw.rect(screen, color, halfH.rect)
        for halfh in half_hs:
            pygame.draw.rect(screen, color, halfh.rect)
        for lineL in lineLs:
            pygame.draw.rect(screen, black, lineL.rect)
        for linel in linels:
            pygame.draw.rect(screen, black, linel.rect)

        if nextPossibleLevels[4]["levelName"] == "blueUp":
            Imgs(bridgeX, bridgeY, pygame.image.load("images/bridge.png"))

        pygame.display.flip()


while 1:
    levelYellowDownAndBlack, yellow, yellowDown = main(
        levelYellowDownAndBlack, yellow, yellowDown)

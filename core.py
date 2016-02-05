from constants import *

# Setting
pygame.init()

screenResolution = (640, 480)
gameCaption = "test game"
gameFont = pygame.font.SysFont("Arial", 12)
gameBackgroundColor = WHITE
FPS = 60

pygame.display.set_caption(gameCaption)
surface = pygame.display.set_mode(screenResolution)
clock = pygame.time.Clock()
keyboardPrev = []
keyboardInput = []
instanceList = []


def game_end():
    # Game End
    pygame.quit()
    quit()


# --- Useful Function ---


def draw_text(x,y,text="", color=BLACK):
    # Draws text
    _txt = gameFont.render(str(text), True, color)
    surface.blit(_txt, (x, y))


def display_get_width():
    # Get width of display
    return screenResolution[0]


def display_get_height():
    # Get height of display
    return screenResolution[1]


def keyboard_button(key):
    # Check if a keyboard button is on hold
    try:
        if keyboardInput[key]:
            return True
    except:
        return False


def keyboard_released(key):
    # Check if a keyboard button is released
    try:
        if keyboardPrev[key] and not keyboardInput[key]:
            return True
    except:
        return False


def keyboard_pressed(key):
    # Check if a keyboard button is pressed
    try:
        if not keyboardPrev[key] and keyboardInput[key]:
            return True
    except:
        return False


def instance_create(obj, x=0, y=0):
    # Create an instance of an Object
    ins = obj(x, y)
    ins.init()
    instanceList.append(ins)
    return ins


# game_control


def game_start(game_init=None):
    # Start game

    if game_init is not None:
        game_init()
    while True:
        # Background
        surface.fill(gameBackgroundColor)

        # Get Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end()
            global keyboardInput
            keyboardInput = pygame.key.get_pressed()

        # Go through instances
        for instance in instanceList:
            # Executes codes in update
            instance.update()

        global keyboardPrev
        keyboardPrev = keyboardInput
        pygame.display.update()
        clock.tick(FPS)
    print "end"
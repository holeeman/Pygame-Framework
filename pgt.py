import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
surface = pygame.Surface((640, 480))
surface.fill((255, 255, 255))
mouse_input = [0,0,0]
mouse_prev = [0,0,0]
point = None
drawing = False

class Point(object):
    def __init__(self, surface, position):
        self.surface = surface
        self.position = position
        self.p1 = None
        self.p2 = self
        pygame.draw.circle(self.surface, (0, 0, 0), self.position, 2)

    def connect(self):
        if self.p1 != None:
            pygame.draw.line(self.surface, (0, 0, 0), self.p1.position, self.position, 4)

def mouse_button(key):
    if mouse_input[key]:
        return True
    return False


def mouse_released(key):
    if mouse_prev[key] and not mouse_input[key]:
        return True
    return False


def mouse_pressed(key):
    if not mouse_prev[key] and mouse_input[key]:
        return True
    return False

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit();
        global mouse_input, point, drawing
        mouse_input = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
            
        if mouse_released(0):
            drawing = False
        
        if drawing:
            print mouse_pos
            p1 = point
            point = Point(surface, mouse_pos)
            point.p1 = p1
            point.connect()

        if mouse_pressed(0):
            drawing = True
            point = None

    screen.blit(surface, (0, 0))        
    pygame.display.update()

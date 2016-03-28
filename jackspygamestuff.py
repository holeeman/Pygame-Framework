import pygame, time

class Screen():
	def __init__(self,background, screensize):
		self.background = background
		self.screensize = ()
pygame.init()	
clock = pygame.time.Clock()

#h = int(raw_input("Height of screen: "))
#w = int(raw_input("Width of screen: "))
#x = int(raw_input("Icon width: "))
#y = int(raw_input("Icon height: "))
#b = int(raw_input("Buffer size: "))

h = 400
w = 600
x = 75
y = 75
b = 0
FPS = 60


clist = [(w/2 - b - x, h/2 - b - y, x, y), (w/2+b,h/2-b-y, x, y), (w/2-b-x, h/2+b, x, y), (w/2+b, h/2+b, x, y)]
	
display = pygame.display.set_mode((w, h))

room = "player select"

while True:
	# Background
        display.fill((255, 255, 255))
	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
		exit()
	if room == "title":
		print "not available"
	if room == "player select":
		for c in clist:
			pygame.draw.rect(display, (0, 0, 0), c)
		
        pygame.display.update()
	if b < 65:
		b = b + 2
	clist = [(w/2 - b - x, h/2 - b - y, x, y), (w/2+b,h/2-b-y, x, y), (w/2-b-x, h/2+b, x, y), (w/2+b, h/2+b, x, y)]
	clock.tick(60)


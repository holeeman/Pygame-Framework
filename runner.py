from player import *


class timer(Object):
    def init(self):
        self.time = 60
        self.count = 0
        self.pl1 = None
        self.pl2 = None

    def update(self):
        draw_text(300, 20, self.time - (self.count/60))
        check = str(mouse_pressed(M_LEFT))+":"+str(mouse_button(M_MIDDLE))+":"+str(mouse_released(M_RIGHT))+":"
        draw_text(10,100, str(mouse_x())+"/"+str(mouse_y())+" "+check)
        draw_text(10,20, point_distance(self.pl1.x,self.pl1.y,self.pl2.x,self.pl2.y))
        draw_text(10,40, point_direction(self.pl1.x,self.pl1.y,self.pl2.x,self.pl2.y))
        self.count += 1


def game_init():
    p1 = instance_create(Player, 120, 200)
    p2 = instance_create(Player, 400, 200)
    p1.dummy = False
    p2.flip = True

game_start(game_init)

from player import *


def game_init():
    p1 = instance_create(Player, 120, 200)
    p2 = instance_create(Player, 400, 200)
    p1.dummy = False
    p2.flip = True
    print p2.flip

game_start(game_init)
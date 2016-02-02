from core import *
from sprite import *
import math


class Player(Object):

    def init(self):
        self.hp = 100
        self.mhp = 100
        self.speed = 3
        self.sprite_index = spr_idle
        self.image = self.sprite_index
        self.image_index = 0
        self.ground = 200
        self.gravity = 10
        self.vspeed = 0
        self.ispeed = 1.5
        self.punch = False
        self.flip = False
        self.dummy = True

    def update(self):
        # Animate
        self.image = pygame.transform.flip(self.sprite_index.get_image(int(math.floor(self.image_index/(FPS/self.sprite_index.image_count)))),self.flip,False)
        self.image_index += self.ispeed;
        if self.image_index > FPS:
            self.image_index = 0
            if self.punch is True:
                self.punch = False
                self.sprite_index = spr_idle
                self.ispeed = 1.5

        # Draw self
        surface.blit(self.image, (self.x,self.y))

        # Move
        if keyboard_pressed(K_UP) and not self.dummy:
            if self.y >= self.ground:
                self.vspeed = -30

        if keyboard_button(K_RIGHT) and self.punch == False and not self.dummy:
            self.sprite_index = spr_walk
            self.ispeed = 1.5
            self.x += self.speed
        if keyboard_button(K_LEFT) and self.punch == False and not self.dummy:
            self.sprite_index = spr_walk
            self.ispeed = 1.5
            self.x -= self.speed

        if keyboard_released(K_LEFT) or keyboard_released(K_RIGHT):
            self.sprite_index = spr_idle
            self.ispeed = 1.5

        if keyboard_pressed(ord('z')) and self.punch == False and not self.dummy:
            self.punch = True
            self.sprite_index = spr_punch
            self.ispeed = 2

        # Vertical Position due to the vertical speed
        self.y += self.vspeed
        self.vspeed += self.gravity/2

        # Gravity
        if self.y < self.ground:
            self.y += self.gravity/4
        self.y = min(self.ground, self.y)

        if self.hp <= 0:
            game_end()

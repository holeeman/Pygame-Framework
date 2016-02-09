from core import *
from classes import *
import glob, os, json
spr_list = glob.glob('*.png')
font = pygame.font.SysFont("Arial", 14)
menu = ["Hit Box", "Hurt Box", "Clear", "Save"]


def check_box(box):
    if mouse_x() > box[0]+box[2]:
        return False
    if mouse_x() < box[0]:
        return False
    if mouse_y() > box[1]+box[3]:
        return False
    if mouse_y() < box[1]:
        return False
    return True


class SpriteHandler(Object):

    def init(self):
        self.width = 200
        self.current_sprite = None
        self.current_file_name = ""
        self.current_index = -1
        self.current_frame = 0
        self.default_sprite_width = 150
        self.default_sprite_height = 150
        self.boxes = []
        self.generator = None

    def update(self):
        for i in range(len(spr_list)):
            if i % 2 == 0:
                pygame.draw.rect(surface, (127, 127, 127), (0, self.y+i*20, self.width, 20))
            if i == self.current_index:
                color = RED
            else:
                color = BLACK
            draw_text(self.x, self.y+i*20, spr_list[i], color)

        if mouse_pressed(M_LEFT):
            if check_box((self.x, self.y, self.width, len(spr_list)*20)):
                # Load Sprite
                index = min(len(spr_list)-1,(mouse_y()-self.y)/20)
                self.current_index = index
                self.current_sprite = Sprite(spr_list[index], self.default_sprite_width, self.default_sprite_height)
                self.current_frame = 0
                self.current_file_name = ""
                self.boxes = []
                self.generator.clear_box()
                for b in range(self.current_sprite.image_count):
                    self.boxes.append([])
                # Check if .hb file already exists
                if os.path.isfile(spr_list[index]+".hb"):
                    load = open(spr_list[index]+".hb", 'r')
                    self.boxes = json.load(load)
                    try:
                        self.generator.set_box(self.boxes[self.current_frame][0],self.boxes[self.current_frame][1])
                    except:
                        pass
                self.current_file_name = spr_list[index]+".hb"

            if self.current_sprite is not None:
                if check_box((250, 500, 90*self.current_sprite.image_count, 75)):
                    # Change Frame
                    self.current_frame = min(self.current_sprite.image_count, (mouse_x()-250)/90)
                    self.generator.clear_box()
                    try:
                        self.generator.set_box(self.boxes[self.current_frame][0],self.boxes[self.current_frame][1])
                    except:
                        pass

        if self.current_sprite is not None:
            draw_sprite(450, 100, self.current_sprite, self.current_frame)
            for frame in range(self.current_sprite.image_count):
                if self.current_frame == frame:
                    color = RED
                else:
                    color = BLACK
                image = pygame.transform.scale(self.current_sprite.get_image(frame), (75, 75))
                pygame.draw.rect(image, color, (0, 0, 75, 75), 1)
                surface.blit(image, (250+frame*90, 500))
        if keyboard_pressed(K_RETURN):
            try:
                print self.boxes
            except:
                print "error"


class BoxGenerator(Object):

    def init(self):
        self.hurtBoxes = []
        self.hitBoxes = []
        self.drawRect = False
        self.mode = 0 # 0 for hit and 1 for hurt
        self.handler = None

    def clear_box(self):
        self.hurtBoxes = []
        self.hitBoxes = []

    def set_box(self, hit, hurt):
        self.hitBoxes = hit
        self.hurtBoxes = hurt

    def update(self):
        if self.handler.current_sprite is not None:
            if 200 < mouse_x() < 770 and mouse_y() < 500:
                if mouse_pressed(M_LEFT):
                    self.x = mouse_x()
                    self.y = mouse_y()
                    self.drawRect = True

            if mouse_released(M_LEFT) and self.drawRect:
                rect = (self.mode, self.x-450, self.y-100, mouse_x()-self.x, mouse_y()-self.y)
                if self.mode:
                    self.hurtBoxes.append(rect)
                else:
                    self.hitBoxes.append(rect)
                # Save Box
                self.handler.boxes[self.handler.current_frame] = self.hitBoxes, self.hurtBoxes
                self.drawRect = False

            if self.drawRect:
                if self.mode == 0:
                    color = RED
                else:
                    color = BLUE
                pygame.draw.rect(surface, color, (self.x, self.y, min(770, max(200,mouse_x()))-self.x, min(500, mouse_y())-self.y),1)
        pygame.draw.rect(surface, RED, (770, 100, 20, 20))
        pygame.draw.rect(surface, BLUE, (770, 120, 20, 20))
        for m in range(len(menu)):
            if m == self.mode:
                color = RED
            else:
                color = BLACK
            draw_text(800, 100+m*20,menu[m], color)

        if mouse_pressed(M_LEFT):
            if check_box((800, 100, 60, len(menu)*20)):
                index = min(len(menu)-1, (mouse_y()-100)/20)
                if index < 2:
                    self.mode = index
                elif index == 2:
                    # Clear Box
                    self.hitBoxes = []
                    self.hurtBoxes = []
                    self.handler.boxes[self.handler.current_frame] = self.hitBoxes, self.hurtBoxes
                elif index == 3:
                    # Save as .hb
                    if self.handler.current_file_name is not "":
                        f = open(self.handler.current_file_name,"w")
                        json.dump(self.handler.boxes, f)
                        f.close()
        if len(self.hitBoxes) > 0 or len(self.hurtBoxes) > 0:
            for rectangle in self.hitBoxes:
                pygame.draw.rect(surface, RED, (rectangle[1]+450,rectangle[2]+100,rectangle[3],rectangle[4]), 1)
            for rectangle in self.hurtBoxes:
                pygame.draw.rect(surface, BLUE, (rectangle[1]+450,rectangle[2]+100,rectangle[3],rectangle[4]), 1)

def game_init():
    display_resize(1024,768)
    draw_set_font(font)
    handler = instance_create(SpriteHandler)
    generator = instance_create(BoxGenerator)
    generator.handler = handler
    handler.generator = generator
game_start(game_init)

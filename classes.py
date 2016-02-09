from constants import *
import os, json

class Object(object):
    # Object class

    def __init__(self, x=0, y=0):
        super(Object, self).__init__()
        self.x = x
        self.y = y

    def init(self):
        pass

    def update(self):
        pass


class Sprite(object):
    # Sprite class

    def __init__(self, file_name, width=0, height=0, alpha=True):
        if alpha:
            self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        else:
            self.sprite_sheet = pygame.image.load(file_name).convert()
        self.sprite = []
        self.file_name = file_name
        self.sheet_width = self.sprite_sheet.get_size()[0]
        self.sheet_height = self.sprite_sheet.get_size()[1]
        self.image_count = 0
        if width == 0 or height == 0:
            width = self.sheet_width
            height = self.sheet_height
        self.image_width = width
        self.image_height = height
        for yy in range(self.sheet_height/height):
            for xx in range(self.sheet_width/width):
                image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                image.blit(self.sprite_sheet, (0, 0), (xx*width, yy*height, width, height))
                self.sprite.append(image)
                self.image_count += 1

    def get_image(self, index=0):
        try:
            return self.sprite[index]
        except:
            return self.sprite[0]


class SpriteExt(Sprite):
    # Can use hit box methods
    def __init__(self, file_name, width=0, height=0, alpha=True):
        Sprite.__init__(self, file_name, width, height, alpha)
        self.box = None
        self.box_reversed = []
        if os.path.isfile(file_name+".hb"):
            f = open(file_name+".hb", 'r')
            self.box = list(json.load(f))
            for frame_index in range(len(self.box)):
                self.box_reversed.append([])
                for type_index in range(len(self.box[frame_index])):
                    self.box_reversed[frame_index].append([])
                    for box_index in range(len(self.box[frame_index][type_index])):
                        self.box_reversed[frame_index][type_index].append([0,0,0,0,0])
                        rbox = self.box_reversed[frame_index][type_index][box_index]
                        rbox[0] = type_index
                        rbox[1] = self.image_width-self.box[frame_index][type_index][box_index][1]
                        rbox[2] = self.box[frame_index][type_index][box_index][2]
                        rbox[3] = self.box[frame_index][type_index][box_index][3] * -1
                        rbox[4] = self.box[frame_index][type_index][box_index][4]
            print self.box
            print self.box_reversed


    def get_box(self, frame, box_type):
        if self.box is not None:
            if frame < len(self.box):
                return self.box[frame][box_type]

    def get_box_reversed(self, frame, box_type):
        if self.box is not None:
            if frame < len(self.box):
                box = self.box_reversed[frame][box_type]
                return box

from enum import Enum
from PIL import Image


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Encoder:
    def __init__(self):
        # width, height of the picture
        self.width = -1
        self.height = -1

        # used when saving binary numbers to each pixel
        self.last_width = 0
        self.last_height = 0
        self.last_color = None

        self.img = None
        self.pixel_access = None

    def load_image(self, file_path: str):
        self.img = Image.open(file_path)
        self.pixel_access = self.img.load()

        width, height = self.img.size

        self.width = width
        self.height = height

        self.last_width = 0
        self.last_height = 0

    @staticmethod
    def convert_char_to_binary_list(c: str):
        return format(ord(c), '08b')

    def get_next_coordinate_and_color(self):

    def save_binary_number_to_picture(self, binary_number):


    def save_message(self, message: str):
        for character in message:
            binary_character = self.convert_char_to_binary_list(character)

            for binary_number in binary_character:
                self.save_binary_number_to_picture(binary_number)

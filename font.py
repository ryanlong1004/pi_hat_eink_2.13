from PIL import ImageFont
import os


class Font:
    def __init__(self, size, path):
        self.size = size
        self.path = path
        self.font = ImageFont.truetype(path, size)

    def __call__(self):
        return get_font(self.size)


def get_font(size):
    return ImageFont.truetype(os.path.join("./font", "Font.ttc"), size)


FONT_20 = get_font(20)  # 26 max characters horizontally
FONT_18 = get_font(18)  # 28 max characters horizontally

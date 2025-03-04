#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from lib.waveshare_epd import epd2in13b_V4
import time
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)


def get_font(size):
    return ImageFont.truetype(os.path.join("./font", "Font.ttc"), size)


FONT_20 = get_font(20)
FONT_18 = get_font(18)


class EPDDisplay:
    def __init__(self):
        self.picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pic")
        self.libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib")
        if os.path.exists(self.libdir):
            sys.path.append(self.libdir)
        self.epd = epd2in13b_V4.EPD()

    def init_and_clear(self):
        logging.info("init and Clear")
        self.clear()
        time.sleep(1)

    def draw_image(self, orientation):
        if orientation == "horizontal":
            logging.info("1.Drawing on the Horizontal image...")
            image_size = (self.epd.height, self.epd.width)  # 250*122
        else:
            logging.info("2.Drawing on the Vertical image...")
            image_size = (self.epd.width, self.epd.height)  # 122*250

        black_image = Image.new("1", image_size, 255)
        ry_image = Image.new("1", image_size, 255)
        drawblack = ImageDraw.Draw(black_image)

        drawblack.text((10, 0), "hello world", font=FONT_20, fill=0)
        drawblack.text((10, 20), "2.13inch e-Paper b V4", font=FONT_20, fill=0)
        drawblack.text((120, 0), "微雪电子", font=FONT_20, fill=0)
        drawblack.line((20, 50, 70, 100), fill=0)
        drawblack.line((70, 50, 20, 100), fill=0)
        drawblack.rectangle((20, 50, 70, 100), outline=0)

        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(ry_image))
        time.sleep(2)

    def display_bmp_files(self, image_path):
        logging.info("%s read bmp file", image_path)
        black_image = Image.open(os.path.join(self.picdir, image_path))
        ry_image = Image.open(os.path.join(self.picdir, image_path))
        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(ry_image))
        time.sleep(2)

    def diplay_bmp_files_on_window(self, image_path):
        logging.info("%s read bmp file on window", image_path)
        blackimage1 = Image.new("1", (self.epd.height, self.epd.width), 255)  # 250*122
        redimage1 = Image.new("1", (self.epd.height, self.epd.width), 255)  # 250*122
        newimage = Image.open(os.path.join(self.picdir, image_path))
        blackimage1.paste(newimage, (0, 0))
        self.epd.display(self.epd.getbuffer(blackimage1), self.epd.getbuffer(redimage1))

    def clear_and_sleep(self):
        self.clear()
        self.sleep()

    def clear(self):
        logging.info("Clear...")
        self.epd.init()
        self.epd.clear()

    def sleep(self):
        logging.info("Goto Sleep...")
        self.epd.sleep()

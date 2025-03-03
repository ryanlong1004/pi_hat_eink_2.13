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
        self.epd.init()
        self.epd.Clear()
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
        drawry = ImageDraw.Draw(ry_image)

        drawblack.text((10, 0), "hello world", font=FONT_20, fill=0)
        drawblack.text((10, 20), "2.13inch e-Paper b V4", font=FONT_20, fill=0)
        drawblack.text((120, 0), "微雪电子", font=FONT_20, fill=0)
        drawblack.line((20, 50, 70, 100), fill=0)
        drawblack.line((70, 50, 20, 100), fill=0)
        drawblack.rectangle((20, 50, 70, 100), outline=0)
        drawry.line((165, 50, 165, 100), fill=0)
        drawry.line((140, 75, 190, 75), fill=0)
        drawry.arc((140, 50, 190, 100), 0, 360, fill=0)
        drawry.rectangle((80, 50, 130, 100), fill=0)
        drawry.chord((85, 55, 125, 95), 0, 360, fill=1)

        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(ry_image))
        time.sleep(2)

    def display_bmp_files(self, image_path):
        logging.info("3. Reading bmp file")
        black_image = Image.open(os.path.join(self.picdir, image_path))
        ry_image = Image.open(os.path.join(self.picdir, image_path))
        self.epd.display(self.epd.getbuffer(black_image), self.epd.getbuffer(ry_image))
        time.sleep(2)

        logging.info("4. Reading bmp file on window")
        black_image_window = Image.new(
            "1", (self.epd.height, self.epd.width), 255
        )  # 250*122
        ry_image_window = Image.new(
            "1", (self.epd.height, self.epd.width), 255
        )  # 250*122
        new_image = Image.open(os.path.join(self.picdir, "100x100.bmp"))
        black_image_window.paste(new_image, (0, 0))
        self.epd.display(
            self.epd.getbuffer(black_image_window), self.epd.getbuffer(ry_image_window)
        )

    def clear_and_sleep(self):
        logging.info("Clear...")
        self.epd.init()
        self.epd.clear()
        logging.info("Goto Sleep...")
        self.epd.sleep()

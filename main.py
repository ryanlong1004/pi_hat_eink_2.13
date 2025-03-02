#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from lib.waveshare_epd import epd2in13b_V4
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)


class EPDDisplay:
    def __init__(self):
        self.picdir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pic"
        )
        self.libdir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
        )
        if os.path.exists(self.libdir):
            sys.path.append(self.libdir)
        self.epd = epd2in13b_V4.EPD()
        self.font20 = ImageFont.truetype(os.path.join(self.picdir, "Font.ttc"), 20)
        self.font18 = ImageFont.truetype(os.path.join(self.picdir, "Font.ttc"), 18)

    def init_and_clear(self):
        logging.info("epd2in13b_V4 Demo")
        logging.info("init and Clear")
        self.epd.init()
        self.epd.Clear()
        time.sleep(1)

    def draw_horizontal_image(self):
        logging.info("1.Drawing on the Horizontal image...")
        HBlackimage = Image.new("1", (self.epd.height, self.epd.width), 255)  # 250*122
        HRYimage = Image.new("1", (self.epd.height, self.epd.width), 255)  # 250*122
        drawblack = ImageDraw.Draw(HBlackimage)
        drawry = ImageDraw.Draw(HRYimage)
        drawblack.text((10, 0), "hello world", font=self.font20, fill=0)
        drawblack.text((10, 20), "2.13inch e-Paper b V4", font=self.font20, fill=0)
        drawblack.text((120, 0), "微雪电子", font=self.font20, fill=0)
        drawblack.line((20, 50, 70, 100), fill=0)
        drawblack.line((70, 50, 20, 100), fill=0)
        drawblack.rectangle((20, 50, 70, 100), outline=0)
        drawry.line((165, 50, 165, 100), fill=0)
        drawry.line((140, 75, 190, 75), fill=0)
        drawry.arc((140, 50, 190, 100), 0, 360, fill=0)
        drawry.rectangle((80, 50, 130, 100), fill=0)
        drawry.chord((85, 55, 125, 95), 0, 360, fill=1)
        self.epd.display(self.epd.getbuffer(HBlackimage), self.epd.getbuffer(HRYimage))
        time.sleep(2)

    def draw_vertical_image(self):
        logging.info("2.Drawing on the Vertical image...")
        LBlackimage = Image.new("1", (self.epd.width, self.epd.height), 255)  # 122*250
        LRYimage = Image.new("1", (self.epd.width, self.epd.height), 255)  # 122*250
        drawblack = ImageDraw.Draw(LBlackimage)
        drawry = ImageDraw.Draw(LRYimage)
        drawblack.text((2, 0), "hello world", font=self.font18, fill=0)
        drawblack.text((2, 20), "2.13 epd b V4", font=self.font18, fill=0)
        drawblack.text((20, 50), "微雪电子", font=self.font18, fill=0)
        drawblack.line((10, 90, 60, 140), fill=0)
        drawblack.line((60, 90, 10, 140), fill=0)
        drawblack.rectangle((10, 90, 60, 140), outline=0)
        drawry.rectangle((10, 150, 60, 200), fill=0)
        drawry.arc((15, 95, 55, 135), 0, 360, fill=0)
        drawry.chord((15, 155, 55, 195), 0, 360, fill=1)
        self.epd.display(self.epd.getbuffer(LBlackimage), self.epd.getbuffer(LRYimage))
        time.sleep(2)

    def display_bmp_files(self):
        logging.info("3.read bmp file")
        Blackimage = Image.open(os.path.join(self.picdir, "2in13b_V4b.bmp"))
        RYimage = Image.open(os.path.join(self.picdir, "2in13b_V4b.bmp"))
        self.epd.display(self.epd.getbuffer(Blackimage), self.epd.getbuffer(RYimage))
        time.sleep(2)

        logging.info("4.read bmp file on window")
        blackimage1 = Image.new("1", (self.epd.height, self.epd.width), 255)  # 250*122
        redimage1 = Image.new("1", (self.epd.height, self.epd.width), 255)  # 250*122
        newimage = Image.open(os.path.join(self.picdir, "100x100.bmp"))
        blackimage1.paste(newimage, (0, 0))
        self.epd.display(self.epd.getbuffer(blackimage1), self.epd.getbuffer(redimage1))

    def clear_and_sleep(self):
        logging.info("Clear...")
        self.epd.init()
        self.epd.clear()
        logging.info("Goto Sleep...")
        self.epd.sleep()


def main():
    try:
        display = EPDDisplay()
        display.init_and_clear()
        display.draw_horizontal_image()
        display.draw_vertical_image()
        display.display_bmp_files()
        display.clear_and_sleep()
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13b_V4.epdconfig.module_exit(cleanup=True)
        exit()


if __name__ == "__main__":
    main()

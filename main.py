#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from epd_display import EPDDisplay
from lib.waveshare_epd import epd2in13b_V4

logging.basicConfig(level=logging.DEBUG)


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

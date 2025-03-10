#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import time
from epd_display import EPDDisplay
from lib.waveshare_epd import epd2in13b_V4

logging.basicConfig(level=logging.DEBUG)


def main():
    try:
        write("Working")
        # display.draw_image("horizontal")
        # time.sleep(10)
        # display.draw_image("vertical")
        # time.sleep(10)
        # display.display_bmp_files("processed_fear_and_greed_index.png")
        # time.sleep(5)
        # display.diplay_bmp_files_on_window("bluehound.bmp")
        # display.clear_and_sleep()
    except IOError as e:
        logging.info(e)
    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd2in13b_V4.epdconfig.module_exit(cleanup=True)
        exit()


def write(txt: str):
    display = EPDDisplay()
    display.init_and_clear()
    display.draw_text(txt)


if __name__ == "__main__":
    main()

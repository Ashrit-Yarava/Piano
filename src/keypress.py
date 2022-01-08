#!/usr/bin/python3
import os
import sys
import termios
import time
import tty


# Adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
def get_key(button_delay: float = 0.0, print_output: bool = False):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if(print_output):
        print(str(ch))
    if(button_delay > 0):
        time.sleep(button_delay)
    return ch

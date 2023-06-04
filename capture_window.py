import time

from PIL import ImageGrab
import win32gui


def get_mswug_window():
    hwnd = win32gui.FindWindow(None, r'Microsoft Ultimate Word Games')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.SetWindowPos(hwnd, None, 0, 0, 1600, 1000, 0)
    # This is necessary to let the window resize and redraws itself
    time.sleep(1)
    dimensions = win32gui.GetWindowRect(hwnd)
    image = ImageGrab.grab(dimensions)
    return dimensions, image


def get_letter_box(image):
    box = (482, 682, 1123, 766)
    region = image.crop(box)
    return region


def get_words_box(image):
    box = (172, 226, 1308, 499)
    region = image.crop(box)
    return region

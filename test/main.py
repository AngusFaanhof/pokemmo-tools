import time, json, pyautogui
from imgcompare import image_diff_percent
from PIL import Image

from pynput import keyboard
from pynput.keyboard import Key


# im = pyautogui.screenshot(region=(10, 10, 100, 100))
# im.show()

region = (3070, 620, 20, 180)

print(pyautogui.locateOnScreen("test2.png", region=region, confidence=0.9))
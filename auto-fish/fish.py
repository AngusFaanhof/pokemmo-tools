from operator import truediv
import time, json, pyautogui
from imgcompare import image_diff_percent
from PIL import Image

from pynput import keyboard
from pynput.keyboard import Key


UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'
IM_LANDED = Image.open("resources/landed.png")
IM_FLED = Image.open("resources/battle.png")

raining = False
cooldown = 6.5
pause = False

with open("settings.json", "r") as file:
	data = json.load(file)
	catch_region = tuple(data["catchArea"])
	battle_region = tuple(data["battleArea"])


def catch():
	time.sleep(5.8)					# Wait for encounter animation
	pyautogui.press(['down', 'z'])			# Throw rock
	time.sleep(1.7)					# wait for throw animation

	im = pyautogui.screenshot(region=battle_region)
	time.sleep(0.7)					# wait for

	if image_diff_percent(im, IM_FLED) < 5:
		time.sleep(0.15)
		pyautogui.press('z')

		return True

	return False


IV_REGION = (3070, 620, 20, 180)
def check_iv():
	return pyautogui.locateOnScreen("resources/31.png", region=IV_REGION, confidence=0.95) != None

def fish():
	pyautogui.press('1')
	time.sleep(3.1)

	im = pyautogui.screenshot(region=catch_region)
	pyautogui.press('z')

	return image_diff_percent(im, IM_LANDED) < 5


def press(key, seconds=0.1):
	pyautogui.keyDown(key)
	time.sleep(seconds)
	pyautogui.keyUp(key)


def safari_route():
	press(UP, 0.1)
	press('z', 5)
	press(UP, 0.2)
	pyautogui.press('3')
	press(UP, 0.78)
	press(RIGHT, 0.48)
	press(UP, 0.16)


def start():
	# safari_route()

	remaining = 30
	landed = fish()

	while remaining > 0:
		while not landed:
			landed = fish()
		
		if catch():
			remaining -= 1
			time.sleep(13)
			pyautogui.click(x=3030, y=590)

			if check_iv():
				pyautogui.click(x=3434, y=593)

			else:
				pyautogui.click(x=3155, y=590)
				pyautogui.press("down")
				pyautogui.press("z")
				time.sleep(0.1)
				pyautogui.press("up")
				pyautogui.press("z")


		time.sleep(0.2)
		landed = False

	press('z', 1)

def test():
	pyautogui.press("right", presses=13)

def on_press(key):
	global pause
	if key == Key.delete:
		safari_route()

	elif key == Key.end:
		start()		


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

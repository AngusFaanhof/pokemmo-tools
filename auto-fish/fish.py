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


with open("settings.json", "r") as file:
	data = json.load(file)
	catch_region = tuple(data["catchArea"])
	battle_region = tuple(data["battleArea"])


def catch():
	time.sleep(6.7)					# Wait for encounter animation
	pyautogui.press(['down', 'z'])			# Throw rock
	time.sleep(1.7)					# wait for throw animation

	im = pyautogui.screenshot(region=battle_region)
	time.sleep(0.7)					# wait for

	if image_diff_percent(im, IM_FLED) < 5:
		time.sleep(0.15)
		pyautogui.press('z')

		return True

	return False


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


def on_press(key):
	if key == Key.delete:
		safari_route()

	elif key == Key.end:
		remaining = 30

		landed = fish()
		while remaining > 0:
			while not landed:
				landed = fish()

			if catch():
				time.sleep(13)
				pyautogui.press('escape')
				remaining -= 1

			time.sleep(0.2)
			landed = False


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

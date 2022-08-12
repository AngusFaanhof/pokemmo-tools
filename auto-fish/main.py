import time, json
from imgcompare import image_diff_percent
from PIL import Image
from pyautogui import press, screenshot

IM_LANDED = Image.open("resources/landed.png")
IM_FLED = Image.open("resources/battle.png")

with open("settings.json", "r") as file:
	data = json.load(file)
	catch_region = tuple(data["catchArea"])
	battle_region = tuple(data["battleArea"])

remaining = 30

def interact(seconds):
	press('z', seconds)

def catch():
	time.sleep(6.5)					# Wait for encounter animation
	press(['down', 'z'])			# Throw rock
	time.sleep(1.7)					# wait for throw animation

	im = screenshot(region=battle_region)
	time.sleep(0.7)					# wait for

	if image_diff_percent(im, IM_FLED) < 5:
		time.sleep(0.15)
		press('z')

		return True

	return False


def fish():
	press('p')
	time.sleep(3.1)

	im = screenshot(region=catch_region)
	press('z')

	return image_diff_percent(im, IM_LANDED) < 5


while remaining > 0:
	landed = fish()
	while not landed:
		landed = fish()

	if catch():
		time.sleep(13)
		press('escape')

		remaining -= 1

	time.sleep(0.2)


def on_press(key):
	if key == Key.delete:
		press('s')
		interact(3.5)

	elif key == Key.end:
		press('up', 0.2)
		interact(5)
		press('up', 0.3)
		time.sleep(0.3)
		safari_route()

	elif key == Key.page_down:
		# victory_road()
		battle_frontier()

	elif key == Key.home:
		pyautogui.press("f")
		time.sleep(12.3)
		pyautogui.press("z")
		pyautogui.press("z")
		pyautogui.press("z")


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
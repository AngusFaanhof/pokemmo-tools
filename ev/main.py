import pyautogui, time
from pynput import keyboard
from pynput.keyboard import Key


def press(key, seconds=0.1):
	pyautogui.keyDown(key)
	time.sleep(seconds)
	pyautogui.keyUp(key)


def base_pokecenter():
	press('down', 1.4)
	
	time.sleep(0.6)
	press('3', 0.05)


# victory road hoen
def hp_ev():
	base_pokecenter()

	press("down", 0.2)
	press("left", 0.6)
	press("up", 0.7)
	press("left", 0.15)
	press("up", 1.5)


# fuchsia city
def atk_ev():
	base_pokecenter()

	press("right", 2.25)
	press("up", 0.9)
	press("right", 4.2)


# island 2
def satk_ev():
	base_pokecenter()

	press("right", 0.6)
	press("up", 0.2)
	press("right", 0.7)
	press("up", 0.8)
	press("z", 2)


# victory road
def def_ev():
	press('left', 0.35)
	press('down', 1.4)

	time.sleep(0.6)
	press('3', 0.05)

	press('down', 0.9)
	press('right', 0.1)
	press('down', 0.4)
	press('right', 0.2)
	press('down', 0.72)
	press('left', 0.08)
	press('down', 0.64)
	press('right', 0.56)
	press('down', 0.80)
	press('left', 0.24)
	press('up', 0.08)

# battle frontier
def sdef_ev():
	base_pokecenter()

	press("right", 1.5)
	press("down", 0.4)
	press("right", 1.1)
	press("down", 0.2)
	press("z", 2)


# island 5
def spd_ev():
	base_pokecenter()

	press("left", 0.4)
	press("down", 0.4)
	press("right", 1.15)
	press("up", 0.5)


def on_press(key):
	if key == Key.delete:
		press("8", 0.05)

		time.sleep(3)
		press("z", 3.5)

	elif key == Key.end:
		hp_ev()
		# atk_ev()
		# def_ev()
		# satk_ev()
		# sdef_ev()
		# spd_ev()

	elif key == Key.home:
		pyautogui.press("7")

		time.sleep(12.3)

		pyautogui.press("z")
		pyautogui.press("z")
		pyautogui.press("z")


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

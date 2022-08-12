import json, os
from pyautogui import screenshot
from pynput.mouse import Listener

json_file = open("settings.json", "r+")
settings = json.load(json_file)

class Area:
	def __init__(self):
		self.x_start = 0
		self.y_start = 0
		self.x_end = 0
		self.y_end = 0

	def box(self):
		return (self.x_start, self.y_start, self.x_end - self.x_start, self.y_end - self.y_start)


#Select area
area = Area()
done = False

def handle_selection():
	if done:
		file_name = "resources/battle.png"
		field = "battleArea"
	else:
		file_name = "resources/landed.png"
		field = "catchArea"

	if os.path.exists(file_name):
		os.remove(file_name)

	screenshot(file_name, region=area.box())
	settings[field] = area.box()


def on_click(x, y, button, pressed):
	global done

	if pressed:
		area.x_start = x
		area.y_start = y

	else:
		area.x_end = x
		area.y_end = y

		handle_selection()

		if done:
			return False

		done = True


with Listener(on_click=on_click) as listener:
	listener.join()

json_file.seek(0)
json.dump(settings, json_file)
json_file.truncate()

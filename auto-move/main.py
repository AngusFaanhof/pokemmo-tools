import pyautogui, time
# from pynput import keyboard
# from pynput.keyboard import Key, Controller

# LEFT = Key.left
# RIGHT = Key.right
# DOWN = Key.down
# UP = Key.up

with pyautogui.hold('alt'):
	pyautogui.pressc('tab')

# pyautogui.keyDown('right')
# time.sleep(0.8)
# pyautogui.keyUp('right')

def bike(key, steps):
	secs = 0.45 + 0.08 * (steps - 1)
	pyautogui.keyDown(key)
	time.sleep(secs)
	pyautogui.keyUp(key)

bike('right', 5)
bike('left', 5)
bike('right', 5)
bike('left', 5)


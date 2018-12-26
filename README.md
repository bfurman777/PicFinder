# PicFinder
This tool detects and clicks template image(s) on the screen in real time.

Place all template images in a "templates" folder in the same directory as picfinder.py.

To make template images:
Set the "taking_screenshots" variable in picfinder.py to True. 
This will send screenshots to a "screenshots" folder in the same directory as the script.
Crop the screenshot so that the image contains only the template.
This ensures the image template looks exactly the same as the script sees it in on the screen.
This image should be exactly the same every time it will be detected.
For example, in a 2D game, crop the image so only the face of an enemy remains with no background.

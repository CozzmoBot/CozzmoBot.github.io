import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse=pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.

pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
pyautogui.doubleClick()    # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

pyautogui.keyDown('shift') # Press the Shift key down and hold it.
pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
pyautogui.keyUp('shift')   # Let go of the Shift key.

pyautogui.hotkey('ctrl', 'q') # Press the Ctrl-C hotkey combination.
pyautogui.hotkey('ctrl', 'q') # Press the Ctrl-C hotkey combination.
pyautogui.hotkey('ctrl', 'q') # Press the Ctrl-C hotkey combination.
pyautogui.hotkey('ctrl', 'q') # Press the Ctrl-C hotkey combination.
pyautogui.hotkey('ctrl', 'q') # Press the Ctrl-C hotkey combination.
pyautogui.hotkey('ctrl', 'cmd', 'q') # Press the Ctrl-C hotkey combination.

##for i in range (1, 1000):
##    pyautogui.alert('''Never gonna give you up
##Never gonna let you down
##Never gonna run around and desert you
##Never gonna make you cry
##Never gonna say goodbye
##Never gonna tell a lie and hurt you''') # Make an alert box appear and pause the program until OK is clicked.

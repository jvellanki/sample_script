from datetime import datetime

import pywinauto
import time
import logging
from pywinauto import Application
from pywinauto.keyboard import send_keys

# Create and configure logger using the basicConfig() function
logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')

# Creating an object of the logging
logger = logging.getLogger()
logger.warning('warning')

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
"""
logger.debug("This is a harmless debug Message")
logger.info("This is just an information")
logger.warning("It is a Warning. Please make changes")
logger.error("You are trying to divide by zero")
logger.critical("Internet is down")
"""

logger.info("=================Start of the test ================")

# Application(backend="uia").start(cmd_line=r"C:\windows\system32\notepad.exe", timeout=10)
path_notepad = r"C:\Program Files\Notepad++\notepad++.exe"
Application(backend="uia").start(cmd_line=path_notepad, timeout=10)
logger.info("Launched the Notepad application")

# notepad_app=Application(backend="uia").connect(path=r"C:\windows\system32\notepad.exe")
notepad_app=Application(backend="uia").connect(path=path_notepad)
time.sleep(3)

"""
# Go to File menu
notepad_app.Dialog.child_window(title="File", control_type="MenuItem").click_input()
logger.info("File menu clicked")

# open a new file
notepad_app.Dialog.child_window(title="New Ctrl+N", auto_id="41001", control_type="MenuItem").click_input()
logger.info("New file opened")
"""

# time.sleep(3)
send_keys("{ENTER}")
send_keys('Hey, You have started Automation of notepad', with_spaces=True)
send_keys("{ENTER}")
send_keys('Hey, You have started Automation of notepad', with_spaces=True)
send_keys("{ENTER}")

logger.info("Entered the text in file")

notepad_app.Dialog.child_window(title="File", control_type="MenuItem").click_input()
logger.info("File menu clicked")

# notepad_app.Dialog.print_control_identifiers()
notepad_app.Dialog.child_window(title="Save	Ctrl+S", auto_id="41006", control_type="MenuItem").click_input()

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# convert datetime obj to string
str_current_datetime = str(current_datetime)

# create a file object along with extension
file_name = "try_automation_" + str_current_datetime + ".txt"

send_keys( file_name, with_spaces=True)
notepad_app.Dialog.child_window(title="Save", control_type="Button").click_input()
logger.info("Saved the text in file in: " + file_name)

time.sleep(3)
"""
logger.info("Close the file")

notepad_app.Dialog.child_window(title="File", control_type="MenuItem").click_input()
logger.info("File menu clicked")

time.sleep(3)
# notepad_app.Dialog.print_control_identifiers()
notepad_app.Dialog.child_window(title="Close Ctrl+W", auto_id="41003", control_type="MenuItem").click_input()
"""
logger.info("===================End of the test==================")

"""
time.sleep(3)
notepad_app.Dialog.child_window(title="File", control_type="MenuItem").click_input()
notepad_app.Dialog.child_window(title="Close Ctrl+W", auto_id="41003", control_type="MenuItem").click_input()
"""

import pyautogui
import subprocess
import time
print("Hello !")
# Open Notepad++
subprocess.Popen(['notepad++.exe'])

# Wait for Notepad++ to open
time.sleep(2)

# Define the message you want to type
message = "Hello, Notepad++ Automation!"

# Type the message into Notepad++
pyautogui.typewrite(message)

# Save the file (you can modify the path and filename)
pyautogui.hotkey('ctrl', 's')

# Wait for the "Save As" dialog to appear (you can adjust the duration)
time.sleep(2)

# Type the file name
filename = "automated_message.txt"
pyautogui.typewrite(filename)

# Press Enter to save the file
pyautogui.press('enter')

# Close Notepad++
pyautogui.hotkey('alt', 'f4') 

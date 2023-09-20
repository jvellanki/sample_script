import time
from pywinauto import Application

# Launch Notepad
app = Application().start("notepad.exe")

# Wait for Notepad to open
time.sleep(2)

# Select the Notepad window
notepad = app.Notepad

# new code added
print (" new code added ")

# Type some text into Notepad
notepad.type_keys("Hello, pywinauto!")

# made some changes to code
print(" Hello world")

# made some more changes to code
print (" more changes ")

# Save the file
app.Notepad.menu_select("File -> Save As...")
save_dialog = app.SaveAs
save_dialog.FileNameEdit.type_keys("example.txt")
save_dialog.Save.click()

# Close Notepad
app.Notepad.menu_select("File -> Exit")

# Handle the confirmation dialog if it appears
if app.Confirmation.wait("exists", timeout=3):
    app.Confirmation.Yes.click()

# Close the Save As dialog if it appears
if save_dialog.exists():
    save_dialog.Cancel.click()
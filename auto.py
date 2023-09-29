from pywinauto.application import Application
import time

# Start Notepad
app = Application().start('notepad.exe')
time.sleep(1)  # Give some time for Notepad to open

# Select the main Notepad window
main_window = app.top_window()

# Type some text
main_window.Edit.type_keys("Hello, pywinauto!")

# Save the file
main_window.menu_select("File -> Save")
save_dialog = app.window(title="Save As")
save_dialog.Edit.set_edit_text("example563.txt")
save_dialog.Save.click()

# Close Notepad
main_window.menu_select("File -> Exit")

# Wait for Notepad to close
app.wait_not('exists', timeout=10)

print("Script completed.")

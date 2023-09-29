import subprocess
import time
import pyautogui
print("Hello !")

# Path to the Windows Calculator executable
calculator_exe = "calc.exe"

try:
    # Open Windows Calculator
    subprocess.Popen(calculator_exe)
    print("Windows Calculator is now open.")

    # Wait for Calculator to open
    time.sleep(2)

    # Perform basic addition (e.g., 5 + 3)
    pyautogui.typewrite("5")
    pyautogui.press("plus")
    pyautogui.typewrite("3")
    pyautogui.press("enter")

    # Wait for the result to appear
    time.sleep(1)

    # Capture the result
    result = pyautogui.screenshot(region=(500, 250, 200, 100))  # Adjust the region as needed

    # Save the result as an image (optional)
    result.save("calculator_result.png")
    print("Screenshot saved as 'calculator_result.png'.")

except FileNotFoundError:
    print("Error: The Windows Calculator executable was not found.")

except Exception as e:
    print(f"An error occurred: {e}")

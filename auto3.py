import subprocess
print("Hello")

# Path to the Windows Calculator executable
calculator_exe = "calc.exe"

try:
    # Open Windows Calculator
    subprocess.Popen(calculator_exe)
    print("Windows Calculator is now open.")

except FileNotFoundError:
    print("Error: The Windows Calculator executable was not found.")

except Exception as e:
    print(f"An error occurred: {e}") 

# used bard for help with script and understanding the script

import os
# This line imports the os module.

# Declare and assign values to variables
# Username info: os.popen("whoami") executes the whoami command using the os module.read() reads the output of the command.strip() removes leading and trailing whitespaces.
# IP adress info: os.popen("ip a") executes the ip a command.grep '^inet ' filters the output to lines starting with "inet ".# awk '{print $2}' extracts the second word (IP address) from each line.read() reads the filtered output
# .strip() removes leading and trailing whitespaces.
# hardware_info:os.popen("lshw -short") executes the lshw -short command using the os module..read() reads the output of the command.
username = os.popen("whoami").read().strip()
ip_address = os.popen("ip a | grep '^inet ' | awk '{print $2}'").read().strip()
hardware_info = os.popen("lshw -short").read()

# Print information using the print() function
# Prints the username with the format "Current user: username"
# Prints the IP address with the format "IP address: IP address"
# Prints a header "--- Hardware Information ---".
# Prints the hardware information retrieved using os.popen.
print(f"Current user: {username}")
print(f"IP address: {ip_address}")
print("--- Hardware Information ---")
print(hardware_info)

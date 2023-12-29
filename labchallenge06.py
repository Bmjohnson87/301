# Revised
# The Python module “os” must be utilized
# At least three variables must be declared and referenced in Python
# The Python function print() must be used at least three times
# received help from A. Carroll using his script to understand
# used bard and chatgpt to help understand the outputgi
#\n represents the newline character
# It's used to create line breaks within strings, instructing the program to move the text to the next line when printing or displaying it

# The Python module “os” must be utilized.
# This line imports the os module.
import os


# Declare and initialize three variables to store bash commands
# This command displays the current user's username
directive1 = "whoami"  

# This command displays information about network interfaces
directive2 = "ip a"    

# This command displays hardware information in a condensed format
directive3 = "lshw -short"  

# The .read() part reads the output of the command and stores it in the variable outcome1
outcome1 = os.popen(directive1).read()


# This line prints a descriptive header to indicate the output that will follow
print("Result of 'whoami' command:")  

# This line prints the actual output of the whoami command, which is stored in the directive1 variable.
print(outcome1)  

# Execute the second command and store the result in outcome2
outcome2 = os.popen(directive2).read()

# print("\nResult of 'ip a' command:") header
print("\nResult of 'ip a' command:")  

# Prints the output of the ip a command
print(outcome2)  


# Executes the third command (directive3) and stores the output in outcome3
outcome3 = os.popen(directive3).read()



# Prints a header for the output of the lshw -short command
print("\nResult of 'lshw -short' command:") 

# Prints the output of the lshw -short command for outcome3
print(outcome3)  




#Introduction to Shell
#The filesystem manages files and directories(or folders).
import os

# --Working with Directories--
#This is like typing 'pwd' or 'cd' in the shell
current_dir = os.getcwd()
print(f"Current Shell Directory: {current_dir}")

#Open terminal or cmd
'''
pwd
(shows the current directory)
ls
(shows the lists of folders in the current directory)
cd Documents
(change directory to Documents)
mkdir Ice_Project
(creates a folder named "Ice_Project" in your current location)
echo "print('Hello World')" > hello.py
(creates a file "hello.py" and added one line of code immediately)
'''
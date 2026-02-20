### Program Description
This python program is a simple password strength checker by checking for length, character diversity, and sequence matching with common passwords using an external dataset. This was made for a course project for CS3090 Ethics of Computing.

### How to Run the Program
Download the zip file from the Releases section, unzip it and run the python executable. Alternatively, download the passwordChecker.py and passwords.txt, place them in a folder, then run passwordChecker.py.

The program will prompt you to enter a password, please do not enter any password you actually want to use, details [below](#limitations-and-considerations). After you enter the password, the program will return a report containing potential issues with the password including character diversity, exact match or partial match with common password patterns, and a summarizing score on a scale of 1-10, indicating how strong the input password is.

#### Limitations and Considerations
This program was made for educational and demonstration purposes ONLY. Do not use it to strength test passwords you want to use or have been using. 

This tool has the potential to be misused, that is, the purpose, even if demonstrational, is supposed to check password strength, which is sensitive information. For that reason, only run code downloaded from this repository. Other users and redistributors may very well modify the program for malice such as storing and using the password you input. 

On the user end, this strength checker is based on a very limited data set, and is by no means extensive. It may very well give you a false sense of security if you get a high strength score.

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from names import Names
from letter import Letter
import os

DIR = os.path.dirname(__file__)+"/ReadyToSend"  # Directory of the current script


#write the letter
def write_letter(real_name):
    letter = Letter()
    letter.content = letter.content.replace("[name]", real_name)
    # Ensure the final path is constructed correctly and names are applied
    file_path = os.path.join(DIR, f"{real_name}.txt")
    with open(file_path, "w") as file:
        file.write(letter.content)
    

#get the names
invited = Names()

#iterate through the names
for name in invited.names:
    write_letter(name)


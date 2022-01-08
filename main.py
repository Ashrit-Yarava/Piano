from src.key import KeyManager
from src.keypress import get_key
from src import get_file_path

from os.path import exists
from src.playsound import playsound

manager = KeyManager()

while(True):
    char = get_key()
    key = manager[char]
    
    if(manager[char] is None):
        print("Invalid Entry")
    elif(manager[char] == ""):
        print("Invalid Entry")
    elif("octave" in manager[char]):
        print("Invalid Entry")
    else:
        file_path = get_file_path(key)
        playsound(file_path)


    # Provide a method for exiting program.
    if(char == ' '):
        print("Shutting down piano")
        exit(0)

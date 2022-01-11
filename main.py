from src.key import KeyManager
from src.keypress import get_key
from src import get_file_path

from os.path import exists
from src.playsound import playsound

manager = KeyManager()

while(True):
    char = get_key()
    key = manager[char]
    
    if(key == ""):
        print("Invalid Key")
    elif("octave" in key):
        print("Changed Octave")
    else:
        file_path = get_file_path(key)
        print(file_path)
        playsound(file_path, block = False)


    # Provide a method for exiting program.
    if(char == ' '):
        print("Shutting down piano")
        exit(0)

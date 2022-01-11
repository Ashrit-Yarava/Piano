# Keys that will be played with the left hand.
left_keys = {
    # White Keys.
    'q': 'c',
    'w': 'd',
    'e': 'e',
    'r': 'f',
    't': 'g',
    'y': 'a',
    'u': 'b',

    # Black keys
    '2': 'c-sharp',
    '3': 'd-sharp',
    '5': 'f-sharp',
    '6': 'g-sharp',
    '7': 'a-sharp'
}

# Keys that will be played with the right hand.
right_keys = {
    # White Keys.
    'v': 'c',
    'b': 'd',
    'n': 'e',
    'm': 'f',
    ',': 'g',
    '.': 'a',
    '/': 'b',

    # Black keys
    'g': 'c-sharp',
    'h': 'd-sharp',
    'k': 'f-sharp',
    'l': 'g-sharp',
    ';': 'a-sharp'
}

octaves = {
    # Left hand octaves.
    'a': 1,
    's': 2,
    'd': 3,
    'f': 4,

    # Right hand octaves.
    'i': 5,
    'o': 6,
    'p': 7 
}


class KeyManager:
    def __init__(self):
        # Save previously entered items to the class.
        self.left = left_keys
        self.right = right_keys
        self.octaves = octaves
        self.valid_keys = list(self.left.keys()) + list(self.right.keys()) + list(self.octaves.keys())

        # Initial Octaves.
        self.left_octave = 4
        self.right_octave = 5

    def __getitem__(self, input):
        # Identifies entered input and returns the key along with octave that is associated with it.
        if(input == ' '):
            print("Shutting down piano")
            exit(0)
        if(self.valid_key(input)):
            if(input in list(self.octaves)):
                new_octave = self.octaves[input]
                if(new_octave >= 1 and new_octave <= 4):
                    self.left_octave = new_octave
                if(new_octave >= 5 and new_octave <= 7):
                    self.right_octave = new_octave
                return f"{new_octave} octave."
            if(input in list(self.left.keys())):
                return f"{self.left_octave}-{self.left[input]}"
            if(input in list(self.right.keys())):
                return f"{self.right_octave}-{self.right[input]}"
        else:
            return ""

    
    def valid_key(self, key):
        if(key not in self.valid_keys):
            return False
        else:
            return True

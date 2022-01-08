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
    '2': 'c#',
    '3': 'd#',
    '5': 'f#',
    '6': 'g#',
    '7': 'a#'
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
    'g': 'c#',
    'h': 'd#',
    'k': 'f#',
    'l': 'g#',
    ';': 'a#'
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

        # Initial Octaves.
        self.left_octave = 4
        self.right_octave = 5

    def __getitem__(self, input):
        # Identifies entered input and returns the key along with octave that is associated with it.
        if(input == ' '):
            print("Shutting down piano")
            exit(0)
        if(input in list(self.left.keys())):
            return f"{self.left_octave}-{self.left[input]}"
        if(input in list(self.right.keys())):
            return f"{self.right_octave}-{self.right[input]}"
        if(input in list(self.octaves.keys())):
            if(self.octaves[input] < 5 and self.octaves[input] >= 1):
                self.left_octave = self.octaves[input]
                return self.left_octave + " octave."
            if(self.octaves[input] >= 5 and self.octaves[input] <= 7):
                self.right_octave = self.octaves[input]
                return self.right_octave + " octave."
        return

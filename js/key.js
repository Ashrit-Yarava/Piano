const left_key = new Map([
        // White Keys
        ['q', 'c'],
        ['w', 'd'],
        ['e', 'e'],
        ['r', 'f'],
        ['t', 'g'],
        ['y', 'a'],
        ['u', 'b'],
        // Black Keys
        ['2', 'c-sharp'],
        ['3', 'd-sharp'],
        ['5', 'f-sharp'],
        ['6', 'g-sharp'],
        ['7', 'a-sharp']
])
left = Array.from(left_key.keys())

const right_key = new Map([
        // White Keys
        ['v', 'c'],
        ['b', 'd'],
        ['n', 'e'],
        ['m', 'f'],
        [',', 'g'],
        ['.', 'a'],
        ['/', 'b'],
        // Black Keys
        ['g', 'c-sharp'],
        ['h', 'd-sharp'],
        ['k', 'f-sharp'],
        ['l', 'g-sharp'],
        [';', 'a-sharp']
])
right = Array.from(right_key.keys())

const octaves = new Map([
        // Left Hand Octaves.
        ['a', 1],
        ['s', 2],
        ['d', 3],
        ['f', 4],
        // Right Hand Octaves.
        ['i', 5],
        ['o', 6],
        ['p', 7]
])
const octaveKeys = Array.from(octaves.keys())
const validInput = octaveKeys.concat(left, right)

class KeyManager {
        
        constructor() {
                this.left = left_key
                this.right = right_key
                this.octaves = octaves
                this.validInput = validInput
                
                this.leftOctave = 4
                this.rightOctave = 5
        }

        getKey(input) {
                if(!validInput.includes(input)) {
                        return "Invalid Input"
                }
                if(Array.from(this.left.keys()).includes(input)) {
                        return this.leftOctave + "-" + this.left.get(input)
                }
                if(Array.from(this.right.keys()).includes(input)) {
                        return this.rightOctave + "-" + this.right.get(input)
                }
                if(Array.from(this.octaves.keys()).includes(input)) {
                        let newOctave = this.octaves.get(input)
                        if(newOctave >= 1 && newOctave <= 4) {
                                this.leftOctave = newOctave 
                        }
                        if(newOctave >= 5 && newOctave <= 7) {
                                this.rightOctave = newOctave
                        }
                        return newOctave + " octave"
                }
                return ""
        }

}

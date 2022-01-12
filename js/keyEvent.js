manager = new KeyManager()

function keyPress(event) {
        let output = manager.getKey(String.fromCharCode(event.which))
        console.log(output)
        if(output != "" && output != "Invalid Input" && !output.includes('octave')) {
               const audio = new Audio("keys/" + output + ".mp3")
               audio.play()
                var octave = output.charAt(0)
                if(octave == '1' || octave == '2' || octave == '3' || octave == '4') {
                        if(output.includes('sharp')) {
                                clickAnimationBlack('left' + output.substring(1))
                        } else {
                                clickAnimationWhite('left' + output.substring(1))
                        }
                } else {
                        if(output.includes('sharp')) {
                                clickAnimationBlack('right' + output.substring(1))
                        } else {
                                clickAnimationWhite('right' + output.substring(1))
                        }
                }
        }
        if(output.includes('octave')) {
               var octave = parseInt(output.charAt(0)) 
               if(octave >= 1 && octave <= 4) {
                        document.getElementById('leftOct').innerHTML = "Left Octave: " + octave
               } else { 
                        document.getElementById('rightOct').innerHTML = "Right Octave: " + octave
                }
                
        }
}

manager = new KeyManager()

function keyPress(event) {
        console.log(event.which)
        let output = manager.getKey(String.fromCharCode(event.which))
        if(output != "" && output != "Invalid Input") {
               const audio = new Audio("keys/" + output + ".mp3")
               audio.play()
        }
        var octave = output.charAt(0)
        if(octave == '1' || octave == '2' || octave == '3' || octave == '4') {
                clickAnimation('left' + output.substring(1))
        }
}

manager = new KeyManager()

function keyPress(event) {
        console.log(event.which)
        let output = manager.getKey(String.fromCharCode(event.which))
        if(output != "" && output != "Invalid Input") {
               const audio = new Audio("keys/" + output + ".mp3")
               console.log(output)
               audio.play()
        }
}

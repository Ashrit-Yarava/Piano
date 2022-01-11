function clickAnimation(id) {
        document.getElementById(id).animate(
        [
                {"border-top": "1px solid #777",
                "border-left": "1px solid #999",
                "border-bottom": "1px solid #999",
                "box-shadow": "2px 0 3px rgba(0,0,0,0.1) inset,-5px 5px 20px rgba(0,0,0,0.2) inset,0 0 3px rgba(0,0,0,0.2)",
                "background": "linear-gradient(to bottom,#fff 0%,#e9e9e9 100%)"},
                {"height" : "16em",
                "width" : "4em",
                "z-index" : "1",
                "border-left" : "1px solid #bbb",
                "border-bottom" : "1px solid #bbb",
                "border-radius" : "0 0 5px 5px",
                "box-shadow" : "-1px 0 0 rgba(255,255,255,0.8) inset,0 0 5px #ccc inset,0 0 3px rgba(0,0,0,0.2)",
                "background" : "linear-gradient(to bottom,#eee 0%,#fff 100%)",}
        ], { duration: 5})
}

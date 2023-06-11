let button = document.getElementById("button")

function backgroundColor(){
    // find the select menu
    let select = document.getElementById("background");
    // find the value of the select menu
    let colorValue  = select.options['selectedIndex'];

    // log the value of the menu
    console.log(colorValue)

    // change the background depending value of the select-menu
    if (colorValue == 0){
        document.body.style.backgroundColor = "red";
    
    } else if (colorValue == 1){
        document.body.style.backgroundColor = "green";
    
    } else if (colorValue == 2){
        document.body.style.backgroundColor = "blue";
    
    } else {
        console.log("no color set")
    }
}

// run the function whenever the button is clicked
button.addEventListener('click', backgroundColor)


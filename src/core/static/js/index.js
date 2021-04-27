
var button = documento.getElementById("action-btn");

button.addEventListener("click",function(){
    var amigos = document.getElementById("#amigos");

    if(amigos.style.display === "none"){
        amigos.style.display = "block"
    } else {
        amigos.style.display = "none"
    }


});
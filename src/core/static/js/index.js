var button = document.getElementById("botao");

button.addEventListener("click",function(){
    var amigos = document.getElementById("amigos");
    var espaco = document.getElementById("espaco");

    if(amigos.style.display === "block"){
        botao.style.color = "black"
        amigos.style.display = "none"
        espaco.style.display = "none"
    } else {
        botao.style.color = "white"
        amigos.style.display = "block"
        espaco.style.display = "block"
    }
});
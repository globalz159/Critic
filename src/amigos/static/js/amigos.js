var button = document.getElementById("botao");
var buscar_amigo = document.getElementById("buscar_amigo");


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

buscar_amigo.addEventListener("click",function(){
    var searchbar = document.getElementById("searchbar-nav");
    var primeiro_amigo = document.getElementsByClassName("amigos-box")[0];

    if(searchbar.style.display === "block"){
        searchbar.style.display = "none"
        buscar_amigo.style.color = "white"
        primeiro_amigo.style.margin = "0px 0px 0px 20px"
    } else {
        buscar_amigo.style.color = "red"
        searchbar.style.display = "block"
        primeiro_amigo.style.margin = "40px 0px 0px 20px"
    }
});
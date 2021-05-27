var button_comentar = document.getElementById("btn_comentar");


button_comentar.addEventListener("click",function(){
    var novo_comentario_form = document.getElementById("id_novo_comentario");

    if(novo_comentario_form.style.display === "block"){
        novo_comentario_form.style.display = "none"
    } else {
        novo_comentario_form.style.display = "block"
    }
});

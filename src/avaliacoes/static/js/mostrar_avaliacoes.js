var app_selector = document.getElementById("app_selector");
console.log(app_selector.value);

function mudar_visibilidade_avaliacoes(){
    if(app_selector.value == 'filme'){
        var avaliacoes_visiveis = document.getElementById("id_avaliacoes_filmes");
        var avaliacoes_invisiveis1 = document.getElementById("id_avaliacoes_livros");
        var avaliacoes_invisiveis2 = document.getElementById("id_avaliacoes_series");
        console.log("Igual filme");
    }else if(app_selector.value == 'livro'){
        var avaliacoes_visiveis = document.getElementById("id_avaliacoes_livros");
        var avaliacoes_invisiveis1 = document.getElementById("id_avaliacoes_filmes");
        var avaliacoes_invisiveis2 = document.getElementById("id_avaliacoes_series");
        console.log("Igual livro");
    }else if(app_selector.value == 'serie'){
        var avaliacoes_visiveis = document.getElementById("id_avaliacoes_series");
        var avaliacoes_invisiveis1 = document.getElementById("id_avaliacoes_livros");
        var avaliacoes_invisiveis2 = document.getElementById("id_avaliacoes_filmes");
        console.log("Igual serie");
    }
    avaliacoes_visiveis.style.display = "block"
    avaliacoes_invisiveis1.style.display = "none"
    avaliacoes_invisiveis2.style.display = "none"
};

app_selector.addEventListener("change",function(){
    mudar_visibilidade_avaliacoes();
});
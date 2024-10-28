const apiBaseUrl = "https://pokeapi.co/api/v2/pokemon/";

async function searchPokemon() {
  // DECLARANDO AS VARIÁVEIS
  const search = document
    .getElementById("search-bar")
    .value.toLowerCase()
    .trim();
  const url = apiBaseUrl + search;

  try {
    // REQUISIÇÃO DA URL DA SEARCH E VAI RETORNAR UMA PROMISE
    const response = await fetch(url);

    // VERIFICANDO SE O POKÉMON FOI ENCONTRADO
    if (!response.ok) {
      throw new Error("Pokémon não encontrado. Verifique o nome ou número.");
    }

    // CONVERTENDO EM JSON
    const obj = await response.json();
    
    // URL DA IMAGEM
    const pokeImage =
      "<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" +
      obj.id +
      ".png' id='pokemon-img' alt='" +
      obj.name + 
      "'>";
    
    const pokeName = obj.name;
    const pokeHeight = obj.height;
    const pokeWeight = obj.weight;

    // CRIANDO UM ARRAY PARA GUARDAR A TIPAGEM DO POKÉMON
    const pokeTypesArray = obj.types.map((type) => type.type.name);
    // CRIANDO UM ARRAY PARA GUARDAR OS STATUS DO POKÉMON
    const pokeStatsArray = obj.stats.map((baseStat) => baseStat.base_stat);
    // CRIANDO UM ARRAY PARA GUARDAR AS HABILIDADES DO POKÉMON
    const pokeAbilities = obj.abilities.map((ability) => ability.ability.name);

    // MOSTRANDO NA TELA
    document.getElementsByClassName("pokemon-image")[0].innerHTML = pokeImage;
    document.getElementById("pokemon-name").innerHTML = pokeName;
    document.getElementById("pokemon-height").innerHTML = pokeHeight / 10 + "m";
    document.getElementById("pokemon-weight").innerHTML = pokeWeight / 10 + "kg";
    document.getElementById("hp-stat").innerHTML = pokeStatsArray[0];
    document.getElementById("attack-stat").innerHTML = pokeStatsArray[1];
    document.getElementById("defense-stat").innerHTML = pokeStatsArray[2];
    document.getElementById("sp-attack-stat").innerHTML = pokeStatsArray[3];
    document.getElementById("sp-defense-stat").innerHTML = pokeStatsArray[4];
    document.getElementById("speed-stat").innerHTML = pokeStatsArray[5];

    // LIMPAR O CONTEÚDO ANTES PARA EVITAR REPETIÇÕES
    document.getElementById("pokemon-abilities").innerHTML = "";
    document.getElementsByClassName("pokemon-types-text")[0].innerHTML = "";

    // MOSTRANDO AS HABILIDADES DO POKÉMON
    if (pokeAbilities.length > 0) {
      for (var i = 0; i < pokeAbilities.length; i++) {
        document.getElementById("pokemon-abilities").innerHTML += pokeAbilities[i] + " ";
      }
    } else {
      document.getElementById("pokemon-abilities").innerHTML = "Nenhuma habilidade encontrada.";
    }

    // MOSTRANDO AS TIPAGENS DO POKÉMON
    if (pokeTypesArray.length > 0) {
      for (var i = 0; i < pokeTypesArray.length; i++) {
        document.getElementsByClassName("pokemon-types-text")[0].innerHTML += pokeTypesArray[i] + " ";
      }
    } else {
      document.getElementsByClassName("pokemon-types-text")[0].innerHTML = "Nenhum tipo encontrado.";
    }

  } catch (error) {
    // MENSAGEM DE ERRO SE ALGO DER ERRADO
    console.error("Erro:", error);
    document.getElementsByClassName("pokemon-image")[0].innerHTML = `<p style="color:red;">${error.message}</p>`;
  }
}

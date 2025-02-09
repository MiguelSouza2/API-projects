async function getSearch() {
    

    let searchRequest = document.getElementById("searchInput").value;
    console.log(searchRequest);
    const apiBaseUrl = `https://pensador-api.vercel.app/?term=${searchRequest}&max=10`;

    let obj;
    let phrases = [];
    let areaPhrases = document.getElementById("areaPhrases");
    
    if(searchRequest != "") {
        try {    
            response = await fetch(apiBaseUrl);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            obj = await response.json();

            phrases = obj.frases;

            areaPhrases.innerHTML = "";
            for (var i = 0; i < phrases.length; i++) {
                areaPhrases.innerHTML +=
                "<br><br>autor: " + phrases[i].autor + "<br>frase: " + phrases[i].texto;
            }
            
        } catch(e){
            console.error("Error:", e);
            areaPhrases.innerHTML = "Error fetching data from API.";
        }
    }

}

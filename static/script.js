function aggiorna_temperatura() {
    document.getElementById("tempinterna").innerText = {{database.tinterna}} ;
}

setInterval(aggiorna_temperatura, 1000);
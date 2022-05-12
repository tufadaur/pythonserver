function aggiornadati(){
    var xmlhttp = new XMLHttpRequest();
    var url = "/static/json/db.json";
    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myArr = JSON.parse(this.responseText);
            document.getElementById("t_interna").innerHTML = myArr['t_interna'];
            document.getElementById("caldaia").innerHTML = myArr['stato_caldaia'];
            document.getElementById("t_esterna").innerHTML = myArr['t_esterna'];
            document.getElementById("h_interna").innerHTML = myArr['h_interna'];
            document.getElementById("h_esterna").innerHTML = myArr['h_esterna'];
            document.getElementById("soglia").innerHTML = myArr['soglia_attuale'];
            document.getElementById("confort").innerHTML = myArr['temperature'][0];
            document.getElementById("eco").innerHTML = myArr['temperature'][1];
            document.getElementById("hot").innerHTML = myArr['temperature'][2];
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

setInterval (aggiornadati , 1000) ;
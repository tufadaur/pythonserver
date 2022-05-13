function aggiornadati(){
    var xmlhttp = new XMLHttpRequest();
    var url = "/static/json/db.json";
    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myArr = JSON.parse(this.responseText);
            document.getElementById("t_interna").innerHTML = myArr['t_interna'];
            document.getElementById("caldaia").innerHTML = myArr['stato_caldaia'];
            document.getElementById("h_interna").innerHTML = myArr['h_interna'];
            document.getElementById("soglia").innerHTML = myArr['soglia_attuale'];
     
            
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

setInterval (aggiornadati , 10000) ;
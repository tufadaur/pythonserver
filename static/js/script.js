function aggiornadati(){
    var xmlhttp = new XMLHttpRequest();
    var url = "/static/json/db.json";
    
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myArr = JSON.parse(this.responseText);
            myFunction(myArr);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
    
    function myFunction(arr) {
        document.getElementById("t_interna").innerHTML = arr['t_interna'];
    }

    
}

setInterval (aggiornadati , 1000) ;
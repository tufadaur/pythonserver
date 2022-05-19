// Create a client instance
client = new Paho.MQTT.Client("broker.hivemq.com", 8000, "peppe");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("tufadaur/termostato");
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {

    var topic = message.destinationName;
    var payload = message.payloadString;
    console.log (payload) ;

    obj = JSON.parse(payload);

    document.getElementById('temperatura').innerText = obj.temperatura.toFixed(1) ;
    document.getElementById('umidita').innerText = obj.umidita.toFixed(1)  ;

}

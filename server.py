from re import S
from flask import Flask, render_template , request
import time
import json

app = Flask(__name__)

@app.route('/')
def index():
  return render_template(
    'index.html',
    title="Controllo Termostato")
    
        
  
  
@app.route('/termostato' , methods=['GET'])
def apiweb():
  
  #ORARIO ATTUALE

  curr_time = time.localtime()
  datacompleta = time.strftime("%H:%M:%S", curr_time)
  orario = time.strftime("%H", curr_time)
  
  #RICEVO ARGOMENTI DA CHIAMATA API ()
  tinterna = request.args.get('t_interna')
  hinterna = request.args.get('h_interna')
  rele = request.args.get('stato_rele')

  #APRO IL FILE JSON DATABASE  
  with open('static/json/db.json') as f:
   database = json.load(f)
  
  # CONTROLLO I DATI RICEVUTI E SE PRESENTI LI SCRIVO SUL FILE JSON 
  
  if(tinterna is not None):
    database["t_interna"] = tinterna
  if(hinterna is not None):
    database["h_interna"] = hinterna   
  if(rele is not None):
    database["stato_rele"] = rele
    
  #determino orario fascia e temperatura di soglia
  
  
  print ("orario attuale", orario)

  soglia_attuale = database["temperature_orarie"][int(orario)]
  print ("soglia attuale", soglia_attuale)

  temp_interna = database["t_interna"]
  print ("temperatura interna" , temp_interna )

  if (temp_interna < soglia_attuale):
    database["stato_caldaia"] = "ON"
  
  if (temp_interna > soglia_attuale):
    database["stato_caldaia"] = "OFF"

  print ("Stato Caldaia :", database["stato_caldaia"])
  #SCRIVO LA DATA DELL ULTIMA CHIAMATA API
  
  database["soglia_attuale"] = soglia_attuale
  database["last"] =  datacompleta
  	
  # SCRIVO IL FILE JSON
  
  with open('static/json/db.json', 'w') as json_file:
   json.dump(database, json_file)
  
  return (database["stato_caldaia"])


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 80)
from flask import Flask, render_template , request
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
  with open('static/json/db.json') as f:
   database = json.load(f)
  return render_template(
        'index.html',
        title="Controllo Termostato",
        description="Progettone di Andrea Tufanari",
        database = database)
  
  
@app.route('/termostato' , methods=['GET'])
def apiweb():
  
  #ORARIO ATTUALE
  now = datetime.now()
  orario = now.strftime("%H")
  print("date and time =", orario)
  datacompleta = now.strftime("%d/%m/%Y, %H:%M:%S")
  
  #RICEVO ARGOMENTI DA CHIAMATA API ()
  tinterna = request.args.get('t_interna')
  hinterna = request.args.get('h_interna')
  testerna = request.args.get('t_esterna')
  hesterna = request.args.get('h_esterna')
  rele = request.args.get('stato_rele')

  #APRO IL FILE JSON DATABASE  
  with open('static/json/db.json') as f:
   database = json.load(f)

  
  
  # CONTROLLO I DATI RICEVUTI E SE PRESENTI LI SCRIVO SUL FILE JSON 
  
  if(tinterna is not None):
    database["t_interna"] = tinterna
  if(hinterna is not None):
    database["h_interna"] = hinterna   
  if(testerna is not None):
    database["t_esterna"] = testerna
  if(hesterna is not None):
    database["h_esterna"] = hesterna  
  if(rele is not None):
    database["stato_rele"] = rele
    
  
  # DETERMINO SE ACCENDERE LA CALDAIA
  
  
  fasciaperorario = database["orari"][int(orario)]
  tempsoglia = database["temperature"][int(fasciaperorario)]
  tempinterna = database["t_interna"]
  isteresi = "0.5"
  
  if (tempinterna < tempsoglia ):
  	caldaia = True
  
  if (tempinterna > (tempsoglia + isteresi)):
  	caldaia = False
  
  database["stato_caldaia"] = caldaia 
  database["stato_rele"] = rele
  
  #SCRIVO LA DATA DELL ULTIMA CHIAMATA API
  
  database["last"] =  datacompleta
  database["fascia"] = fasciaperorario
  	
  # SCRIVO IL FILE JSON
  
  with open('static/json/db.json', 'w') as json_file:
   json.dump(database, json_file)
  
  return (database)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 8001)
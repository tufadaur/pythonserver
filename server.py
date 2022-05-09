from flask import Flask , request
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!" 
  
  
@app.route('/termostato' , methods=['GET'])
def apiweb():
  
  #ORARIO ATTUALE
  now = datetime.now()
  orario = now.strftime("%H:%M:%S")
  print("date and time =", orario)
  
  #RICEVO ARGOMENTI DA CHIAMATA API ()
  tinterna = request.args.get('tinterna')
  hinterna = request.args.get('hinterna')
  testerna = request.args.get('testerna')
  hesterna = request.args.get('hesterna')
  caldaia = request.args.get('caldaia')

  #APRO IL FILE JSON DATABASE  
  with open('db.json') as f:
   database = json.load(f)

  # LEGGO LE 6 FASCIE ORARIE 
  tfascia1 = database["tfascia1"] 	
  tfascia2 = database["tfascia2"] 
  tfascia3 = database["tfascia3"] 
  tfascia4 = database["tfascia4"] 
  tfascia5 = database["tfascia5"] 
  tfascia6 = database["tfascia6"] 	   
   
  # DETERMINO LA FASCIA ATTUALE E LA SCRIVO SUL FILE JSON 
  if (orario >= tfascia1 and orario < tfascia2 ):
   print ("fascia 1")
   fasciaattuale = 1
  if (orario >= tfascia2 and orario < tfascia3 ):
   print ("fascia 2")
   fasciaattuale = 2
  if (orario >= tfascia3 and orario < tfascia4 ):
   print ("fascia 3")
   fasciaattuale = 3
  if (orario >= tfascia4 and orario < tfascia5 ):
   print ("fascia 4")
   fasciaattuale = 4
  if (orario >= tfascia5 and orario < tfascia6 ):
   print ("fascia 5")
   fasciaattuale = 5
  if (orario >= tfascia6 and orario < tfascia1 ):
   print ("fascia 6")
   fasciaattuale = 6
  
  database["fasciaattuale"] = fasciaattuale
  
  # CONTROLLO I DATI RICEVUTI E SE PRESENTI LI SCRIVO SUL FILE JSON 
  
  if(tinterna is not None):
    database["tinterna"] = tinterna
  if(hinterna is not None):
    database["hinterna"] = hinterna    
  if(testerna is not None):
    database["testerna"] = testerna
  if(hesterna is not None):
    database["hesterna"] = hesterna    
  if(caldaia is not None):
    database["caldaia"] = caldaia
    
  # DETERMINO LA TEMPERATURA SOGLIA PER LA FASCIA 
  
  if (fasciaattuale == 1):
   database["tempsoglia"] = database["tempf1"]
  if (fasciaattuale == 2):
   database["tempsoglia"] = database["tempf2"]
  if (fasciaattuale == 3):
   database["tempsoglia"] = database["tempf3"]
  if (fasciaattuale == 4):
   database["tempsoglia"] = database["tempf4"]
  if (fasciaattuale == 5):
   database["tempsoglia"] = database["tempf5"]
  if (fasciaattuale == 6):
   database["tempsoglia"] = database["tempf6"]
  
  # DETERMINO SE ACCENDERE LA CALDAIA
  
  tempsoglia = database["tempsoglia"]
  tempinterna = database["tinterna"]
  
  if (tempinterna <= tempsoglia ):
  	caldaia = 1
  else:
  	caldaia = 0
  
  database["caldaia"] = caldaia 
  	
  # SCRIVO IL FILE JSON
  
  with open('db.json', 'w') as json_file:
   json.dump(database, json_file)
  
  return (employee_data)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 8001)
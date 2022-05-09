from flask import Flask , request
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!" 
  
  
@app.route('/termostato' , methods=['GET'])
def search():
 
  
 fascia1 = "00:00:00"
 fascia2 = "06:00:00"
 fascia3 = "08:00:00"
 fascia4 = "13:00:00"
 fascia5 = "16:00:00"
 fascia6 =  "23:00:00"

  
  now = datetime.now()
  
  orario = now.strftime("%H:%M:%S")
  print("date and time =", orario)
  
  if (orario >= fascia1 and orario < fascia2 ):
	print ("fascia1")
  if (orario >= fascia2 and orario < fascia3 ):
	print ("fascia2")
  if (orario >= fascia3 and orario < fascia4 ):
	print ("fascia3")
  if (orario >= fascia4 and orario < fascia5 ):
	print ("fascia4")
  if (orario >= fascia5 and orario < fascia6 ):
	print ("fascia5")
  if (orario >= fascia6 and orario < fascia1 ):
	print ("fascia6")


  with open('db.json') as f:
   employee_data= json.load(f)
   
   temp1 = request.args.get('temp1')
   temp2 = request.args.get('temp2')
   temp3 = request.args.get('temp3')
   stato1 = request.args.get('stato1')
   stato2 = request.args.get('stato2')
   stato3 = request.args.get('stato3')
  
  if(temp1 is not None):
    employee_data["temp1"] = temp1

  if(temp2 is not None):
    employee_data["temp2"] = temp2
     
  if(temp3 is not None):
    employee_data["temp3"] = temp3

  if(stato1 is not None):
    employee_data["stato1"] = stato1
    
  if(stato2 is not None):
    employee_data["stato2"] = stato2
    
  if(stato3 is not None):
    employee_data["stato3"] = stato3
  
  
  
  
  with open('db.json', 'w') as json_file:
   json.dump(employee_data, json_file)
  
  return (employee_data)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 8001)
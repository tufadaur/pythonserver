from flask import Flask , request

import json

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!" 
  
  
@app.route('/termostato' , methods=['GET'])
def search():

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
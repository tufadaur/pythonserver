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
  
   employee_dict = json.loads(employee_data)

  return (employee_dict)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 8001)
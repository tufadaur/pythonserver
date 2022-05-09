from flask import Flask , request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!" 
  
  
@app.route('/termostato' , methods=['GET'])
def search():
    args = request.args
    temp1 = args.get('temp1')
    temp2 = args.get('temp2')
    
    	if None in (temp1, temp2):
    		return ("non ci sono")
    	
  return (args)
    

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 8001)
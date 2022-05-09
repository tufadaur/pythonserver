from flask import Flask , request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!" 
  
  
@app.route('/termostato/')
def termostato():
    temp1 = request.args.get('temp1')
    return temp1

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0" , port = 8001)
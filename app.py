from flask import Flask,redirect,render_template,request,make_response,jsonify
import json
from prediction import trying_to_predict_life
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST'])

def sayhi():
  if request.method=='POST':
      json_data = request.get_json()
      #json_data = json.loads(json_data)

      data = [[json_data['sodium'], json_data['vitamin_a'], 0, 0, 0, 0, json_data['vitamin_d'], json_data['calcium'], json_data['caffeine'], 0]]
      #df = pd.DataFrame(data)
      output=trying_to_predict_life(data)

      #print (output)
      #print(type(output))

      lis = output.tolist()
      final_data = {
        'food' : lis
      }
    

      return jsonify(final_data)
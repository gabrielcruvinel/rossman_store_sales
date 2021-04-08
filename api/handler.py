from flask import Flask, request, Response, jsonify
from rossman import Rossmann
import pickle
import pandas as pd 
import json

#loading model

model = pickle.load(open('../model_sales_prediction.pkl', 'rb'))

app = Flask(__name__)
@app.route('/rossmann/predict', methods = ['POST'])

def rossman_predict():

    data = request.get_json()

    data = json.loads(data) 
    if data:
        if isinstance(data, dict): #unico exemplo
            data_raw = pd.DataFrame(data, index=[0])
        else: #multiplos exemplos
            data_raw = pd.DataFrame(data, columns=data[0].keys())
        
        #instancio
        pipeline = Rossmann()

        #data cleaning
        df1 = pipeline.data_cleaning(data_raw)
        #feature engineering
        df2 = pipeline.feature_engineering(df1)
        #data preparation
        df3 = pipeline.data_preparation(df2)

        #prediction
        df_response = pipeline.get_prediction(model, data_raw, df3)

        return df_response
    else:
        return Response('{}', status=200, mimetype='application/json')
if __name__ == '__main__':
    app.debug = True
    app.run()

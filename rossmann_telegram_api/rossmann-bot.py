import requests 
import pandas as pd
import json
from flask import Flask, request, Response

#constants
TOKEN = '1703315442:AAEwH0_cm_qyd2qmce_ONMf1kF4iy95zhys'

#INFO BOT
#https://api.telegram.org/bot1703315442:AAEwH0_cm_qyd2qmce_ONMf1kF4iy95zhys/getMe


#GET UPDATES
#https://api.telegram.org/bot1703315442:AAEwH0_cm_qyd2qmce_ONMf1kF4iy95zhys/getUpdates

#SEND MESSAGE
#https://api.telegram.org/bot1703315442:AAEwH0_cm_qyd2qmce_ONMf1kF4iy95zhys/sendMessage?chat_id=780358759&text=Ola peao

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)
    r = requests.post(url, json={'text': text})

    print('Status code{}'.format(r.status_code))
    
    return None

def load_dataset(store_id):
    df10 = pd.read_csv('../data/test.csv')
    df_store_raw = pd.read_csv('../data/store.csv', low_memory=False)
    df_test = pd.merge(df10, df_store_raw, how='left', on='Store')


    #choose store for prediction
    #df_test = df_test[df_test['Store'] == 22]

    #multiple stores
    df_test = df_test[df_test['Store'] == store_id]

    if not df_test.empty:

        #remove_closed_days
        df_test = df_test[df_test['Open'] !=0]
        df_test = df_test[~df_test['Open'].isnull()]
        df_test = df_test.drop('Id', axis=1)

        #convert df to json
        data = json.dumps(df_test.to_dict(orient='records'))
    else:
        data = 'error'
    return data

def predict(data):
    #API CALL

    #HOST
    url = 'http://127.0.0.1:5000/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post(url, json=data, headers=header)
    print('Status code{}'.format(r.status_code))

    d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())
    
    return d1
def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    store_id.replace('/', '')
    try:
        store_id = int(store_id)
    except ValueError:
        store_id = 'error'
    return chat_id, store_id
#API INITIALIZE 
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        chat_id, store_id = parse_message(message)
        if store_id != 'error':
            #load
            data = load_dataset(store_id)

            if data != 'error':
                #predict
                d1 = predict(data)
                #calculation
                d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()

                #send message
                msg = 'Store number {} will sell ${:.2f} in the next 6 weeks'.format(d2['store'].values[0], d2['prediction'].values[0])

                send_message(chat_id, msg)
                return Response('OK', status=200)                 
            else:
                send_message(chat_id, 'Store not Available')
                return Response('Ok', status=200)
        else:
            send_message(chat_id, 'Store ID Wrong')
            return Response('Ok', status=200)

    else:
        return '<h1> Rossmann Telegram Bot </h1>'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

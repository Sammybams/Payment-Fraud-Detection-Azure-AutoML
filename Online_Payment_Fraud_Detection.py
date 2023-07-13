import streamlit as st
st.set_page_config(page_title="Online Payment Fraud Detection App", page_icon="💳")

from PIL import Image

import urllib.request
import json
import os
import ssl

st.title('Online Payment Fraud Detection')

fraud_case = {0:"No Fraud Detected",
              1:"Fraud Detected"}

type_map = {"PAYMENT":"PAYMENT",
            "TRANSFER":"TRANSFER",
            "CASH OUT":"CASH_OUT",
            "DEBIT":"DEBIT",
            "CASH IN":"CASH OUT"}

step = st.number_input('Enter window of transaction (in hours)', min_value=1, max_value=10)

type = st.selectbox(
    'Select Transaction Type',
    (type_map.keys()))

amount = st.number_input('Enter the amount of the transaction', min_value=0.01)
oldbalanceOrg = st.number_input('Enter the initial balance of originator before the transaction', min_value=0.0)
newbalanceOrig = st.number_input('Enter the new balance of originator after the transaction', min_value=0.0)
oldbalanceDest = st.number_input('Enter the initial balance of recipient before the transaction', min_value=0.0)
newbalanceDest = st.number_input('Enter the new balance of recipient after the transaction', min_value=0.0)

# newbalanceOrig = oldbalanceOrg - amount
# newbalanceDest = oldbalanceDest + amount

if (oldbalanceOrg==0):
    percentInOut = 0
else:
    percentInOut = amount / oldbalanceOrg

from dotenv import load_dotenv
load_dotenv('variable.env')


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

data =  {
  "Inputs": {
    "data": [
      {
        "step": step,
        "type": type_map[type],
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "percentInOut": percentInOut
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

def predict(data):
    body = str.encode(json.dumps(data))

    body = str.encode(json.dumps(data))

    url = os.environ.get('ENDPOINT')
    # Replace this with the primary/secondary key or AMLToken for the endpoint
    api_key = os.environ.get('KEY')
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        #print(result)

        #print(int("".join(result.decode().split()[1])[1]))
        prediction = int("".join(result.decode().split()[1])[1])

    except urllib.error.HTTPError as error:
        # print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        # print(error.info())
        # print(error.read().decode("utf8", 'ignore'))
        prediction = error.read().decode("utf8", 'ignore')
    
    return prediction

def batch_predict(file):
    
    features = ["step", "type", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]
    predictions = []
    for i in range(file[features].shape[0]):
      features
      features = ["step", "type", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]
      file['percentInOut'] = file['amount']/file['oldbalanceOrg']
      file.loc[file['percentInOut']==float('inf'), 'percentInOut'] = float(0)

      step, type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, percentInOut = file[features].iloc[i].to_list()
      data =  {
        "Inputs": {
          "data": [
            {
              "step": step,
              "type": type_map[type],
              "amount": amount,
              "oldbalanceOrg": oldbalanceOrg,
              "newbalanceOrig": newbalanceOrig,
              "oldbalanceDest": oldbalanceDest,
              "newbalanceDest": newbalanceDest,
              "percentInOut": percentInOut
            }
          ]
        },
        "GlobalParameters": {
          "method": "predict"
        }
      }

      predictions.append(predict(data))
    
    file["isFlaggedFraud"] = predictions
    return file
  
if st.button("Run"):
    st.header("Prediction")

    # Calls prediction function on data
    prediction = predict(data)
    
    # Catches if output was an HTTPError
    try:

      output = fraud_case[prediction]
      if prediction:
          st.warning(f'{output}', icon="")
          image = Image.open('images/Fraud-Alert.jpeg')
      else:
          st.success(f'{output}', icon="✅")
          image = Image.open('images/Pass.png')

      # st.markdown(f'#### *{output}*')
      st.image(image)

    except:
        st.warning(f'{prediction}', icon="⚠️")
        
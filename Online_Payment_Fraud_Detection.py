import streamlit as st
st.set_page_config(page_title="Online Payment Fraud Detection App", page_icon="💳")


from PIL import Image
import urllib.request
import json
import os
import ssl

st.title('Online Payment Fraud Detection')

fraud_case = {0:" No Fraud Detected",
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

oldbalanceOrg = st.number_input('Enter the balance of originator before the transaction', min_value=0.0)
oldbalanceDest = st.number_input('Enter the balance of recipient before the transaction', min_value=0.0)
amount = st.number_input('Enter the amount of the transaction', min_value=0.01, max_value=oldbalanceOrg)


newbalanceOrig = oldbalanceOrg - amount
newbalanceDest = oldbalanceDest + amount

if (oldbalanceOrg==0):
    percentOut = 0
else:
    percentOut = amount / oldbalanceOrg


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
        "step": 0,
        "type": "example_value",
        "amount": 0.0,
        "oldbalanceOrg": 0.0,
        "newbalanceOrig": 0.0,
        "oldbalanceDest": 0.0,
        "newbalanceDest": 0.0,
        "percentOut": 0.0
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

body = str.encode(json.dumps(data))

if st.button("Run"):
    st.header("Prediction")
    prediction = 0

    if prediction:
        image = Image.open('images/Fraud-Alert.jpeg')
    else:
        image = Image.open('images/Pass.png')

    
    st.image(image)

    st.markdown("<br>", unsafe_allow_html=True)
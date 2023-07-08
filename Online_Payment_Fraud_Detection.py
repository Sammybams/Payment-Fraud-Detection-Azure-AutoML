import streamlit as st
st.set_page_config(page_title="Online Payment Fraud Detection App", page_icon="💳")

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


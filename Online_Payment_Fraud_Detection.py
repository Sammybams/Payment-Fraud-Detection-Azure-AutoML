import streamlit as st
st.set_page_config(page_title="Online Payment Fraud Detection App", page_icon="💳")

st.title('Online Payment Fraud Detection')

fraud_case = {0:" No Fraud Detected",
              1:"Fraud Detected"}
type_map = {"PAYMENT":"PAYMENT",
            "TRANSFER":"TRANSFER",
            "CASH OUT":"CASH_OUT",
            "DEBIT":"DEBIT",
            "CASH IN":"CASH OUT",

}

type = st.selectbox(
    'Select Disorder Type',
    (sorted(crime.DISORDER_TYPE.unique())))

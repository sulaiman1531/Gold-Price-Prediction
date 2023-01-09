import streamlit as st
import pickle


st.title('Gold Price Prediction')
Model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
Date=col1.date_input('Enter date')
GLD=col2.number_input('Enter gold price')
if st.button('predict'):
    data=[[Date,GLD]]
    result=Model.predict(data)[0]
    st.success(result)

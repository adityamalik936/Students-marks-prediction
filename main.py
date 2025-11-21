import streamlit as st 
import pickle
import warnings
warnings.filterwarnings('ignore')
st.title("Student Marks Predictor")
sh=st.number_input("enter study hours")
btn=st.button("predict")

if btn:
    if sh<=12:
        m=pickle.load(open("smp.pkl","rb"))
        t=m.predict([[sh]])[0][0].round(2)
        st.success(f"predict marks : {t}")
    else:
        st.warning("invalid input")
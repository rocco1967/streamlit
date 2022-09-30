# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:23:55 2022

@author: 39333
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import ElasticNet
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import pandas #as pd
import pickle
import streamlit as st
from PIL import Image
model = pickle.load(open('streamlit.pk','rb'))
@st.cache
def predict(Gender, Age, Height, Weight, Duration, Heart_Rate,Body_Temp):
    prediction = model.predict(pandas.DataFrame([[Gender, Age, Height, Weight, Duration,Heart_Rate,Body_Temp]], columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate','Body_Temp']))
    prediction=abs(prediction)
    return prediction
image = Image.open('dottore.png.png')
image2= Image.open('allenamento.PNG')
st.image(image2)
#st.image(image)
st.title('..........Calcolo Calorie........')
#st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")

st.header('     Immetti i dati:')
#st.header('      attenzione digita in Gender 0 =Donna  1= Uomo')
#st.header('Duration=durata esercizio fisico in minuti')
#st.header('Body_Temp=temperatura corporea a fine esercizio')
#st.header('Heart_Rate=battito cardiaco a fine esercizio')
st.header('programma di rete neurale addestrato su 15000 dati clinici')
st.write('seleziona sesso   donna =0 uomo=1')
#Gender = st.number_input('Gender:', min_value=0.0, max_value=1.0,value=1.0)
Gender = st.select("seleziona sesso"["0","1"])
st.write('inserisci eta^')
Age = st.number_input('Age:', min_value=12.0,max_value=80.0,value=12.0)
st.write('inserisci atezza in centimetri')
Height = st.number_input('Height:', min_value=120.0,max_value=210.0,value=120.0)
st.write('inserisci peso in kg reale please')
Weight = st.number_input('Weight:', min_value=35.0,max_value=160.0,value=35.0)
st.write('inserisci durata esercizio(corsa ecc ecc) in minuti')         
Duration = st.number_input('Duration:', min_value=10.0, max_value=240.0, value=10.0)
st.write('inserisci battito cardiaco a fine esercizio')         
Heart_Rate = st.number_input('Heart_Rate:', min_value=50.0,max_value=230.0,value=50.0)
st.write('inserisci temperatura corporea a fine esercizio se^ non puoi inserisci 37 ')         
Body_Temp = st.number_input('Body_Temp:', min_value=35.0,max_value=41.0,value=35.0)

if st.button('Calcolo Calorie'):
    Calorie_Bruciate = predict(Gender, Age, Height, Weight, Duration, Heart_Rate,Body_Temp)
    st.success(f' calcolo calorie {Calorie_Bruciate[0]:.2f} KCAL')
st.image(image)    

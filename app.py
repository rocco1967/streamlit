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
    return prediction
image = Image.open('dottore.png.png')
st.image(image)
st.title('Calcolo Calorie')
#st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")

st.header('Immetti i dati:')
Gender = st.number_input('Gender:', min_value=0.0, max_value=1.0,value=1.0)
Age = st.number_input('Age:', min_value=1.0,max_value=80.0,value=1.0)
Height = st.number_input('Height:', min_value=1.0,max_value=210.0,value=1.0)
Weight = st.number_input('Weight:', min_value=1.0,max_value=160.0,value=1.0)
Duration = st.number_input('Duration:', min_value=1.0, max_value=240.0, value=1.0)
Heart_Rate = st.number_input('Heart_Rate:', min_value=1.0,max_value=230.0,value=1.0)
Body_Temp = st.number_input('Body_Temp:', min_value=1.0,max_value=41.0,value=1.0)

if st.button('Calcolo Calorie'):
    Calorie_Bruciate = predict(Gender, Age, Height, Weight, Duration, Heart_Rate,Body_Temp)
    st.success(f' calcolo calorie {Calorie_Bruciate[0]:.2f} KCAL')

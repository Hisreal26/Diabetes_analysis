import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns
import plotly.express as px

#read a csv file
#import csv file
#convert file to dataframe


st.title("Diabetes.csv")
#import my csv file
df = pd.read_csv("Diabetes.csv")
st.write(df.head())

df = pd.read_csv("Diabetes.csv")
st.write(df.tail())


numpy==2.2.6
matplotlib==3.10.3
pandas==2.2.3
scikit-learn==1.7.0
seaborn==0.13.2
streamlit==1.45.1




#import  python -m pip install scikit-learn
#import -m pip install matlib
#import -m pip install seaborn

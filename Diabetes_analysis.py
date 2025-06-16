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
st.markdown("# FIRST FIVE ARGUMENT")
st.write(df.head())

df = pd.read_csv("Diabetes.csv")
st.markdown("# LAST FIVE ARGUMENT")
st.write(df.tail())





#import  python -m pip install scikit-learn
#import -m pip install matlib
#import -m pip install seaborn

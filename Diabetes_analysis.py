import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns

#read a csv file
#import csv file
#convert file to dataframe

df = pd.read_csv("Diabetes.csv")
st.write(df.head())

df = pd.read_csv("Diabetes.csv")
st.write(df.tail())





#import  python -m pip install scikit-learn
#import -m pip install matlib
#import -m pip install seaborn
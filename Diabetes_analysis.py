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
st.markdown("# FIRST SEVEN ARGUMENT")
st.write(df.head(7))

df = pd.read_csv("Diabetes.csv")
st.markdown("# LAST SEVEN ARGUMENT")
st.write(df.tail(7))

#code for data inspection
st.markdown("#### DESCRIBE")
Hisreal_ = df.describe()
st.table(Hisreal_)

#code for data inspection
st.markdown("#### OVERVIEW")
Hisreal_ = df.shape
st.table(Hisreal_)

st.markdown("## UNIVARIATE VARIABLES")
#code to pick a column in a table - univariate
df = pd.read_csv("Diabetes.csv")
BMI = df["BMI"].describe()
st.markdown("### BMI")
st.write(BMI)

st.title("HISTOGRAM REPRESENTATION")
BMI =px.histogram(df["BMI"], x = "BMI", title = "BloodPressure")
st.plotly_chart(BMI, use_container_width = True)

st.markdown("### BIVARIATE ANALYSIS")
st. markdown("Pregnancies vs Blood Pressure")
bp = px.bar(df,x = "Pregnancies", y = "BloodPressure", title="Distribution of Pregnancies vs Blood Pressure")
st.write(df("Pregnancies, BloodPreesure").describe())



#import  python -m pip install scikit-learn
#import -m pip install matlib
#import -m pip install seaborn

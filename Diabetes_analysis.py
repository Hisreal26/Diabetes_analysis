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
BloodPressure =px.histogram(df["BloodPressure"], x = "BloodPressure", title = "BloodPressure")
st.plotly_chart(BloodPressure, use_container_width = True)

st.title("BAR REPRESENTATION")
BloodPressure =px.bar(df["BloodPressure"], y = "BloodPressure", title = "BloodPressure")
st.plotly_chart(BloodPressure, use_container_width = True)

st.title("PIE REPRESENTATION")
BloodPressure =px.pie(df["BloodPressure"], y = "BloodPressure", title = "BloodPressure")
st.plotly_chart(BloodPressure, use_container_width = True)

st.title("PIE REPRESENTATION")
counted = df["Pregnancies"].value_counts().reset_index()
counted.columns = ["Pregnancies", "count"]
Pregnancies2 = px.pie(counted, names="Pregnancies", values="count", title="BloodPressure")
st.plotly_chart(Pregnancies2, use_container_width = True)




#import  python -m pip install scikit-learn
#import -m pip install matlib
#import -m pip install seaborn

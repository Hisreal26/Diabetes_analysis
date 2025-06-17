import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly_express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


st.title("# DIABETES ANALYSIS")
st.markdown("## OVERVIEW")

#import my csv file
st.markdown("### FIRST SEVEN OBSERVATIONS")
df = pd.read_csv("Diabetes.csv")
st.write(df.head(7))

st.markdown("### LAST SEVEN OBSERVATIONS")
df = pd.read_csv("Diabetes.csv")
st.write(df.tail(7))

st.markdown("### DATA INFO")
AK = df.shape
st.write(AK)

st.markdown("### CORRELATION")
correlation = df.corr()
st.write(correlation)

st.markdown("### BLOOD PRESSURE")
st.write(df["BloodPressure"].describe())

st.markdown("### FIRST 5 BLOOD PRESSURE")
st.write(df["BloodPressure"].head())

#UNIVARIATE ANALYSIS
st.markdown("### UNIVARIATE ANALYSIS")
st.markdown("### BLOOD PRESSURE ANALYSIS")
df = pd.read_csv("Diabetes.csv")
st.write(df["BloodPressure"].describe())

st.markdown("### BODY MASS INDEX ANALYSIS")
df = pd.read_csv("Diabetes.csv")
st.write(df["BMI"].describe())

st.markdown("### PREGNANCIES ANALYSIS")
df = pd.read_csv("Diabetes.csv")
st.write(df["Pregnancies"].describe())

st.markdown("### SKIN THICKNESS ANALYSIS")
df = pd.read_csv("Diabetes.csv")
st.write(df["SkinThickness"].describe())

st.markdown("### GLUCOSE ANALYSIS")
df = pd.read_csv("Diabetes.csv")
st.write(df["Glucose"].describe())

st.markdown("### INSULIN ANALYSIS")
df = pd.read_csv("Diabetes.csv")
st.write(df["Insulin"].describe())

st.title("HISTOGRAM REPRESENTATION")
BP = px.histogram(df["BloodPressure"], y= "BloodPressure", title="Pressure Distribution")
st.plotly_chart(BP, use_container_width=True)

st.title("BAR REPRESENTATION")
BP2 = px.bar(df["BloodPressure"], y= "BloodPressure", title="Pressure Distribution")
st.plotly_chart(BP2, use_container_width=True)

Pregg = px.bar(df["Pregnancies"], y ="Pregnancies", title = "Pregnancies Distribution")
st.plotly_chart(Pregg, use_container_width = True)

#BIVARIATE ANALYSIS
st.markdown("## BIVARIATE ANALYSIS")
st.markdown("### Blood Pressure vs Pregnancies")
df2 = pd.DataFrame(df["BloodPressure"],df["Pregnancies"])
st.write(df2)


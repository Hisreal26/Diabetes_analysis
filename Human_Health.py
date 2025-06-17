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
st.markdown("### FIRST 5 OBSERVATION")
df = pd.read_csv("Diabetes.csv")
st.write(df.head(10))

st.markdown("### LAST 5 OBSERVATION")
df = pd.read_csv("Diabetes.csv")
st.write(df.tail(10))

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
st.markdown("### BLOOD PRESSURE")
st.write(df["BloodPressure"].describe())

fig = px.bar(df["BloodPressure"], y= "BloodPressure", title="")
st.plotly_chart(fig, use_container_width=True)

#BIVARIATE ANALYSIS
st.markdown("## BIVARIATE ANALYSIS")
st.markdown("### Blood Pressure vs Pregnancies")

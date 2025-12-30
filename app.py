
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA Project", layout="wide")
st.title("Exploratory Data Analysis")

# Load dataset
df = pd.read_csv("dataset.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Summary Statistics")
st.write(df.describe())

st.subheader("Missing Values")
st.write(df.isnull().sum())

numeric_df = df.select_dtypes(include='number')

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.subheader("Feature Distribution")
col = st.selectbox("Select Column", numeric_df.columns)
fig2, ax2 = plt.subplots()
sns.histplot(df[col], kde=True, ax=ax2)
st.pyplot(fig2)

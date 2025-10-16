import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Page Config
st.set_page_config(page_title="Student Performance Dashboard For TITAN SUKKUR ", layout="wide")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("StudentsPerformance.csv")
    return df

df = load_data()

# Title
st.title("📊 Student Performance Visualization Dashboard")
st.markdown("Use filters to explore the dataset interactively!")

# Sidebar filters
st.sidebar.header("Filter Data")
gender = st.sidebar.multiselect("Select Gender:", df["gender"].unique(), default=df["gender"].unique())
test = st.sidebar.multiselect("Select Test Preparation:", df["test preparation course"].unique(), default=df["test preparation course"].unique())
education = st.sidebar.multiselect("Parent Education Level:", df["parental level of education"].unique(), default=df["parental level of education"].unique())

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["test preparation course"].isin(test)) &
    (df["parental level of education"].isin(education))
]

st.dataframe(filtered_df.head())

# KPI summary
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Math Score", round(filtered_df["math score"].mean(), 2))
col2.metric("Average Reading Score", round(filtered_df["reading score"].mean(), 2))
col3.metric("Average Writing Score", round(filtered_df["writing score"].mean(), 2))

# Visual 1
st.subheader("Average Scores by Gender")
fig1, ax1 = plt.subplots()
sns.barplot(x="gender", y="math score", data=filtered_df, ci=None, ax=ax1)
st.pyplot(fig1)

# Visual 2
st.subheader("Distribution of Reading Scores")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["reading score"], bins=20, kde=True, ax=ax2)
st.pyplot(fig2)

# Visual 3
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots()
sns.heatmap(filtered_df[["math score", "reading score", "writing score"]].corr(), annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("Built by *Ahmed Sabur* • Powered by Streamlit & Matplotlib")

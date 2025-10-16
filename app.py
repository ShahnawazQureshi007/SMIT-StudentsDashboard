import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("StudentsPerformance.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
gender = st.sidebar.multiselect("Gender", df["gender"].unique(), default=df["gender"].unique())
prep = st.sidebar.multiselect("Test Preparation", df["test preparation course"].unique(), default=df["test preparation course"].unique())
parent_edu = st.sidebar.multiselect("Parental Education", df["parental level of education"].unique(), default=df["parental level of education"].unique())

filtered_df = df[
    (df["gender"].isin(gender)) &
    (df["test preparation course"].isin(prep)) &
    (df["parental level of education"].isin(parent_edu))
]

st.title("📊 Student Performance Dashboard (Plotly Edition)")
st.markdown("### Explore the Kaggle dataset interactively with dynamic visualizations!")

# KPI cards
col1, col2, col3 = st.columns(3)
col1.metric("Average Math Score", round(filtered_df["math score"].mean(), 2))
col2.metric("Average Reading Score", round(filtered_df["reading score"].mean(), 2))
col3.metric("Average Writing Score", round(filtered_df["writing score"].mean(), 2))

st.divider()

# Visualization 1
fig1 = px.histogram(filtered_df, x="math score", color="gender", nbins=20, title="Distribution of Math Scores")
st.plotly_chart(fig1, use_container_width=True)

# Visualization 2
fig2 = px.box(filtered_df, x="parental level of education", y="reading score", color="gender", title="Reading Scores by Parental Education")
st.plotly_chart(fig2, use_container_width=True)

# Visualization 3
fig3 = px.scatter(filtered_df, x="math score", y="writing score", color="gender", size="reading score",
                  hover_data=["test preparation course"], title="Math vs Writing Scores Correlation")
st.plotly_chart(fig3, use_container_width=True)

# Footer
st.divider()
st.markdown("Built by **Ahmed Sabur** | Powered by Streamlit + Plotly")

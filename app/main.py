
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data(filepath):
    data = pd.read_csv(filepath, parse_dates=["Timestamp"])
    return data

data = load_data("../data/benin-malanville.csv")

# Title and Description
st.title("Environmental Data Dashboard")
st.write("Explore insights from environmental sensor data over a year.")

# Sidebar - User Options
st.sidebar.header("Filter Options")
selected_feature = st.sidebar.selectbox(
    "Select Feature for Visualization",
    options=data.columns[1:],  # Skip 'Timestamp'
    index=0
)

# Display Data and Summary
st.subheader("Dataset Overview")
st.dataframe(data.head())

st.subheader("Summary Statistics")
st.write(data.describe())

# Visualization
st.subheader(f"Visualization of {selected_feature}")

fig, ax = plt.subplots()
sns.histplot(data[selected_feature], kde=True, bins=30, ax=ax)
ax.set_title(f"Distribution of {selected_feature}")
st.pyplot(fig)

# Time Series Visualization
if "Timestamp" in data.columns:
    st.subheader("Time Series Visualization")
    fig, ax = plt.subplots(figsize=(10, 5))
    data.set_index("Timestamp")[selected_feature].plot(ax=ax, linewidth=0.8)
    ax.set_title(f"{selected_feature} Over Time")
    st.pyplot(fig)

nano app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Streamlit App with Pandas and Plotly")

# Sample Data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Display DataFrame
st.write("### Sample Data")
st.dataframe(df)

# Create a Plotly Bar Chart
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

# Display the Plotly Chart
st.plotly_chart(fig)

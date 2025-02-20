import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np



# Load CSV
vehicles_df = pd.read_csv('vehicles_us.csv')

# Header
st.header("Vehicle Price by Decade")

# Histogram

    # Define decade bins
bins = np.arange(1900, 2030, 10)  # Decade bins from 1900 to 2020
labels = [f"{int(start)}s" for start in bins[:-1]]  # Create labels for each decade

    # Assign each model_year to a decade bin
vehicles_df['decade'] = pd.cut(vehicles_df['model_year'], bins=bins, labels=labels, right=False)

# Create a histogram using Plotly Express
fig_1 = px.histogram(vehicles_df, x="price", color="decade",
                   nbins=400, barmode="stack",
                   title="Histogram of Price Distribution by Decade",
                   labels={"price": "Price ($)", "decade": "Decade"},
                   opacity=0.7)

    # Update the x axis to only show prices 0 to 50,000, since the majority of prices are below 50,000
fig_1.update_xaxes(range=[0, 60000])

# Show the plot
st.plotly_chart(fig_1)

# Header 2
st.header("Vehicle Price by Model Year")

# Scatter plot
fig_3 = px.scatter(vehicles_df, 
                 x='model_year', 
                 y='price', 
                 title='Vehicle Price vs. Model Year',
                 labels={'model_year': 'Model Year', 'price': 'Price'},
                 trendline="ols")

# Show the plot
st.plotly_chart(fig_3)

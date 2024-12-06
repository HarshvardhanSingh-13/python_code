import streamlit as st
import pandas as pd
import numpy as np

# Display Title
st.title('Hello World')

# Display Text
st.write('Hi Everyone this is my first file')

# Creating a simple DataFrame

df = pd.DataFrame(
    {
        "First Column":[1,2,3,4],
        "Second Column":[10,11,12,13]
    }
)

# Display the DataFrame

st.write("Hey, This is the DataFrame")
st.write(df)

# Create a Line Chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
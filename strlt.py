import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


uploaded_file = st.file_uploader("Vyber fajl")

if uploaded_file is not None:
  xls = pd.read_excel(uploaded_file, parse_dates=['date'], usecols=['date', 'price'])
  st.write(xls)
else:
  st.info('Nics nenačet.')

# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Descriptive Statistics')
#   st.write(df.describe())
# else:
#   st.info('☝️ Upload a CSV file')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

fig2 = px.line(chart_data)

st.plotly_chart(fig2)
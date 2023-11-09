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


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

fig2 = px.line(chart_data)

st.plotly_chart(fig2)
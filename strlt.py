import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

fig2 = px.line(chart_data)

st.plotly_chart(fig2)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as po

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

fig = po.Figure()
fig.add_trace(po.Scatter(x=chart_data.index, y=chart_data['a']))

st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import pandas as pd
import numpy as np

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)


# import plotly.graph_objects as po

# st.header('Line chart')

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# fig = po.Figure()
# fig.add_trace(po.Scatter(x=chart_data.index, y=chart_data['a']))

# st.plotly_chart(fig, use_container_width=True)

# import plotly.express as px

# fig2 = px.line(chart_data)

# st.plotly_chart(fig2)
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st


st.header('Jezdítko')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
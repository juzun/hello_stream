import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time


st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')

with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')
  
    with st.form('my_form'):
        st.subheader('**Order your coffee**')

        # Input widgets
        coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
        coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
        brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
        serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
        milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
        owncup_val = st.checkbox('Bring own cup')

        # Every form must have a submit button
        submitted = st.form_submit_button('Submit')

    if submitted:
        st.markdown(f'''
            ☕ You have ordered:
            - Coffee bean: `{coffee_bean_val}`
            - Coffee roast: `{coffee_roast_val}`
            - Brewing: `{brewing_val}`
            - Serving type: `{serving_type_val}`
            - Milk: `{milk_val}`
            - Bring own cup: `{owncup_val}`
            ''')
    else:
        st.write('☝️ Place your order!')


    # Short example of using an object notation
    st.header('2. Example of object notation')

    form = st.form('my_form_2')
    selected_val = form.slider('Select a value')
    form.form_submit_button('Submit')


with col3:
    if user_food != '':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')
  
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    st.balloons()




# uploaded_file = st.file_uploader("Vyber fajl")

# if uploaded_file is not None:
#   xls = pd.read_excel(uploaded_file, parse_dates=['date'], usecols=['date', 'price'])
#   st.write(xls)
# else:
#   st.info('Nics nenačet.')



# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# fig2 = px.line(chart_data)

# st.plotly_chart(fig2)
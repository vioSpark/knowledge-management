import streamlit as st
import pandas as pd
import numpy as np

st.title('How many hours should you train an officer for?')


st.sidebar.write('How many articles would you like to see?')
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 20,step=1
)


st.sidebar.write('Sorted By')

genre = st.sidebar.radio(
      "",
      ('# Citations', '# Keywords', 'Publication Date'))

st.sidebar.write('Options')

add_checkbox1 = st.sidebar.checkbox('Main Arguments',value=True,key='Argument')
add_checkbox2 = st.sidebar.checkbox('# Citations',value=True,key='Citations')
add_checkbox3 = st.sidebar.checkbox('Author',value=True,key='Author')
add_checkbox4 = st.sidebar.checkbox('URL',value=True,key='URL')
add_checkbox4 = st.sidebar.checkbox('Keywords',value=True,key='Keywords')

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

st.dataframe(df)
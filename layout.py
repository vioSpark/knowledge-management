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
add_checkbox5 = st.sidebar.checkbox('Keywords',value=True,key='Keywords')
add_checkbox6 = st.sidebar.checkbox('Date Published',value=True,key='Date Published')

df = pd.DataFrame(np.array([['ans1', 'Main Arguments1', 3,'Author1','URL1','Keywords1','01-01-2019'], ['ans2', 'Main Arguments2', 6,'Author2','URL2','Keywords2','01-01-2020'], ['ans3', 'Main Arguments3', 9,'Author3','URL3','Keywords3','01-01-2021']]),
                   columns=['Answer', 'Main Arguments', '# Citations', 'Author', 'URL', 'Keywords', 'Date Published'])


checkbox_list = [True,add_checkbox1,add_checkbox2,add_checkbox3,add_checkbox4,add_checkbox5,add_checkbox6]

st.dataframe(df.loc[:,checkbox_list])

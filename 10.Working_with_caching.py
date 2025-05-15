import streamlit as st 
import pandas as pd 
from transformers import pipeline

@st.cache_data
def read_data():
   df= pd.read_csv("https://github.com/laxmimerit/All-CSV-ML-Data-Files-Download/raw/master/IMDB-Dataset.csv")
   return df.head()

def update_session_state():
   if 'counter' not in st.session_state:
      st.session_state.counter =0 

   st.write('Counter:',st.session_state.counter)
   st.session_state.counter +=1
 
st.set_page_config(page_title='Working with caching data',page_icon=":smile:",layout='centered')
st.title('Working with Caching and Session State')

import time
#example of caching 
st.button('Increment Counter')
startttime = time.time()
result = read_data()
st.write('Result of expensive computation:',result)
st.write(startttime - time.time())
# update session state
update_session_state()

@st.cache_resource
def load_model():
   model=pipeline('sentiment-analysis')
   st.success('Loaded NLP model from hugging Face!')
   return model

model = load_model()
st.success('Got model successfully!')
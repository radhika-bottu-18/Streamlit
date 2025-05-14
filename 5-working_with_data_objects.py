import streamlit as st 
import pandas as pd 
st.title('Streamlit Data objects Examples :rocket:')

#Json
json_data = {
    'name':'Radhika',
    'age' : 30,
    'city': 'Hyderabad'
}

st.write(json_data)
st.json(json_data)

df = pd.read_csv('data.csv',index_col=0)
#st.write(df)
st.dataframe(df)
## in table the columns are not interactive 
st.table(df.head())

st.code(""" 
 import os 
 import pandas as pd
 json_data = {
    'name':'Radhika',
    'age' : 30,
    'city': 'Hyderabad'
}
""")

st.metric('Accuracy :',value=80,delta=-5)

st.metric('Accuracy :',value=90,delta=+10)

st.metric('Accuracy :',value=90,delta=(90-70))


edited_data = st.data_editor(df)
st.write(edited_data)
edited_data.to_csv('edited_data.csv')
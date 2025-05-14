import streamlit as st 

st.title('Streamlit Interactive Widgets Examples :rocket:')

button = st.button('Click me')
if button :
    st.write('You clicked me button')

checkbox = st.checkbox('Check me to enable something!! :smile:')

if checkbox : 
    st.write('Checked box is clicked. Something has happened here .!!')

radio = st.radio('Choose and option',['NLP','DP','GenAI','ML'])
st.write('you have selected  ',radio)

selectbox = st.selectbox('Choose a option:',['NLP','ML','DL','AI','GenAI'])

st.write('you have selected :',selectbox)

multiselect = st.multiselect('Choose multiple items : ',['NLP','DL','ML','GENAI','AI','CV'])
st.write('your selection is ',multiselect)

rating = st.slider('select your rating',min_value=0.5,max_value=5.0,step=0.5)
st.write('your selected rating is ',rating)

selectslider = st.select_slider('select a value',['NLP','DL','ML','GENAI','AI','CV'])
st.write('selected slider is ',selectslider)
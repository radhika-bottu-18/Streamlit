import streamlit as st 
st.title('Streamlit with text input examples :smile:')
name = st.text_input('Enter your name')
feedback  = st.text_area('Enter your feedback here.')
age= st.number_input('Enter your age here')
date = st.date_input('Enter a date')
time = st.time_input('Pick a time')
color = st.color_picker('Pick a color')
# display inputs 
st.write('Name :',name)
st.write('Feedback : ', feedback)
st.write('Age :',age)
st.write('Date : ',date)
st.write('Time:',time) 
st.write('Color : ',color)

paracolor = st.color_picker('pick the paragraph color')
html_code = """
<h1 style = "color:{};">A Heading with selected color</h1>
<p style = "color:{};">My paragraph</p>
""".format(color,paracolor)
st.markdown(html_code,unsafe_allow_html=True)
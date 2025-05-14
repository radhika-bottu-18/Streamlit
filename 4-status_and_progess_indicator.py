import streamlit as st 
import time 

st.title('Streamlit status and progress indicator example :rocket:')
empty = st.empty()
empty.text('This text will be replaced after 5 seconds')
time.sleep(5)
empty.text('This is a new text data')

## progress bar 
progess = st.progress(0)
status_text = st.empty()
for i in range(100):
    time.sleep(0.1)
    progess.progress(i)
    status_text.text('Progress: {}'.format(i))
status_text.text('Progress is done !!')

with st.spinner('Waiting ...'):
    time.sleep(5)

st.success('Process is done')
st.warning('Warning message')
st.error('Error message comes here ')
st.info('General info displayed here ')

st.snow()
st.balloons()
import streamlit as st
import time
st.set_page_config(page_title='Cool App',
                   page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state='expanded',
                   menu_items={
                       'Get Help' :  'https://www.site.com/help',
                       'Report a bug' : "https://www.site.com/bug",
                       'About' : 'This is a header. This is an extremely cool app!'
                   }
)

st.sidebar.title('Page Configuration')
st.title('Working with layouts and page configuration')
st.sidebar.title('Working with sidebar')

st.write('## Columns')
col1,col2 = st.columns(2)
col1.write('This is column1')
col2.write('This is column2')

col1,col2 = st.columns([1,3])
col1.write('This is column1')
col2.write('This is column2')
col1.button('Click me')
col2.button('Click me too')

st.write('## Container')
container = st.container(border=True,height=200)
container.write('This content is inside a container')
st.write('This is outside the container')
container.write('Containers are useful for grouping content together.')

container.button('This is inside the container')

#Form 
st.write('## Form')
with st.form('my_form'):
    name = st.text_input('Enter your name')
    submit_button = st.form_submit_button('Submit')
if submit_button:
    st.write('Hello',name,'!')

st.write('## Tabs')
tab1,tab2,tab3 = st.tabs(['Cat','Dog','Owl'])

with tab1 : 
    st.header('A Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg',width=200)
with tab2:
    st.header('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg',width=200)
with tab3:
    st.header('An Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg',width=200)
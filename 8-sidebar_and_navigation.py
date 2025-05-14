import streamlit as st 

st.title('Streamlit Sidebar and navigation :rocket:')

st.sidebar.title('Welcoem to sidebar :smile:')
radio= st.sidebar.radio('Go to',['Home','About','Contact'])

if radio == 'Home':
    st.write('Welcome to home page')
    st.markdown('[Learn more about streamlit here](https://docs.streamlit.io/)')
    st.write("Here, you can explore various features of Streamlit.")

    with st.expander('Click here to learn more about streamlit') :
        st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.")
    with st.popover('Open popover'):
        st.markdown('hello world :smile:')
        name = st.text_input('Enter your name here')
    st.write('Hello ',name)
elif radio == 'About':
    st.write('This is about page')
    st.write('you can find more detailsi n this about page.')
elif radio == 'Contact':
    st.write('Feel free to contact us!')
    st.write('You can reach out to us via email or social media.')
import streamlit  as st 
st.title('Streamlit Text Display Examples')
st.header('This is a header')
st.subheader('This is a subheader')

st.text('This is a simple text')
st.write('This is a written   using st.write()')

st.markdown('# This is a Markdown heading')
st.markdown('## This is a markdown heading two')
st.markdown('[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)')
st.markdown('This is a Markdown paragraph with **bold** and *Italiac* text')
st.markdown('This is a markdown with **bold** and *Italic* text')

st.markdown("""
            -- Ordered List  
            1. First
            2. Second 
            Unordered List 
            - First 
            - Second            
""")

#Emojis 
st.markdown('### Emojis')
st.markdown('[Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)')
st.markdown('Here are some emojis')
st.markdown(":thumbsup: :heart: :rocket: :smile:")
st.markdown('### HTML')
html_code = """ 
            <h1 style='color: blue;'> This is a blue heading</h1>
            <p style='color : green;'> This is a green paragraph</p>'           
"""
st.markdown(html_code , unsafe_allow_html=True)

st.markdown('''---''')
#or 
st.divider()

#latext 

st.latex(r'e^{i\pi}+1 =0')
st.latex(r'f(x)=x^2+zX+1')
st.latex(r'g(x)=\frac{1}{x+y}')
st.latex(r'h(x)= sqrt(x)')
st.latex(r'y=mx+c')
st.latex(r'a^2 +b^2 =c^2')
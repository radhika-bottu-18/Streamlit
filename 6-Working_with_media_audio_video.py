import streamlit as st
st.title('Streamlt Media and file examples. :rocket:')
img = st.file_uploader('upload an image',type= ['jpg','jpeg','png'])

if img: 
    st.image(img,width = 500)

st.markdown('[click the image line here](https://images.pexels.com/photos/1996333/pexels-photo-1996333.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)')
st.image(image='https://images.pexels.com/photos/1996333/pexels-photo-1996333.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

st.markdown("[click to view image](https://images.pexels.com/photos/1996333/pexels-photo-1996333.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)")

audio = 'birthday-song-337887.mp3'
st.audio(audio,format='audio/mp3')

audio = st.file_uploader('upload a audio file',type= ['mp3','wav'])
if audio : 
    st.audio(audio,format='audio/mp3')

st.video("https://www.youtube.com/watch?v=D0D4Pa22iG0")

# To upload multiple file together.
uploaded_files = st.file_uploader('chooes files: ',accept_multiple_files=True)
for f in uploaded_files:
    st.write(f)
    # you will do the processing here.

# to download a file . 
text_file = 'This is a text file.'
st.download_button('Download Here',text_file,file_name = 'example.txt')
st.download_button('Download Image',img,file_name = 'example.jpg')
st.download_button('Download Audio',audio,file_name='example.mp3')
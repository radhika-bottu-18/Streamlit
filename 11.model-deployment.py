import streamlit as st 
from io import BytesIO
from PIL import Image
from rembg import remove
from cartooner import cartoonize
import cv2

st.set_page_config(layout='wide',page_title='Image Background Remover')
st.write('## Remove background from your image')

st.write(':dog: Try uploading an image to watch the background magically removed.')


st.sidebar.write('## Upload and download :gear:')
my_upload = st.sidebar.file_uploader('Upload an image',type =['png','jpg','jpeg'])

alpha_matting =st.sidebar.checkbox('Use Alpha Matting',value=True)
threshold = st.sidebar.slider('Background Threshold',0,255,value=50,step=5)

#Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf,format='PNG')
    byte_im = buf.getvalue()
    return byte_im

#package the transform into a function 
def remove_bg(upload,threshold,alpha_matting):
    image = Image.open(upload)
    col1,col2=st.columns(2)
    col1.write('Original Image :camera:')
    col1.image(image)

    st.write("## Cartoonized Image")
    cartoon = cartoonize(image)
    img = Image.fromarray(cartoon)
    st.image(img)

    fixed = remove(image,alpha_matting=alpha_matting,alpha_matting_foreground_threshold=threshold)

    col2.write('Fixed Image :wrench:')
    col2.image(fixed)
    st.sidebar.markdown('---')

    st.sidebar.download_button('Download fixed image',convert_image(fixed),'fixed.png','image/png')
    st.sidebar.download_button("Download cartoonize image",convert_image(img),'cartoon.png','image/png')


if my_upload is not None:
    remove_bg(upload=my_upload,threshold=threshold,alpha_matting=alpha_matting)
else:
    remove_bg('whitehorse.jpg', threshold=threshold, alpha_matting=alpha_matting)
import streamlit as st

from PIL import Image
# Import libraries
from urllib.request import urlopen, Request
import os
import requests
import io



#display image
image = Image.open('./Images/app_home_pic.png')
st.image(image, width = 700)
#image_2 = Image.open('./Images/neural_style_transfer_example.jpg')
#st.image(image_2, width = 700)

st.title ('Image Neural Style Transfer App')

st.markdown('\n')
st.markdown('\n')

#About
expander_bar = st.beta_expander('About this App')
expander_bar.markdown("""
**Description**: This app allows you to apply styl transfer from one image to another.\n
**Audience**: Art related\n 
**Data Sources**: Image upload\n 
**Methods**: Neural Style Transfer.\n 
**Python Libraries**: Streamlit, Pytorch \n
**Authors**: Alena Kalodzitsa, Ronald Nhondova,\n """)

st.markdown('\n')
st.markdown('\n')

model_endpoint = 'https:\\'

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

def post_image(URL,img_file):
    """ post image and return the response """
    #print(img_file)
    buf = io.BytesIO()
    img_file.save(buf, format='PNG')
    buf.seek(0)

    #img = open(img_file, 'rb').read()
    response = requests.post(URL, files={'file': ('image.png', buf, 'image/png')})
    return response 

image_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'])
if image_file is not None:
    #file_details = {"FileName":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
    #st.write(file_details)

    img = load_image(image_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    try:
        response = post_image(model_endpoint,img)
        image_bytes = io.BytesIO(response.content)

        img = load_image(image_bytes)
        st.image(img, caption='Style Transfered Image.', use_column_width=True)
    except ValueError:
        st.image(img, caption='Could not apply style transfer to Image.', use_column_width=True)
    

    

st.markdown('\n')
st.markdown('\n')
st.markdown('\n')
st.markdown('**Disclaimer**: Current content is for informational purpose only. Any images used in the app are')
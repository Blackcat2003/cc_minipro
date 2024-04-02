import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

# Title
st.title("Easy OCR - Extract Text from Images")

# Subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

st.markdown("")

# Image uploader
image = st.file_uploader(label="Upload your image here", type=['png', 'jpg', 'jpeg'])

@st.cache_data
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader

reader = load_model()  # Load model

if image is not None:
    input_image = Image.open(image)  # Read image
    st.image(input_image)  # Display image

    with st.spinner("🤖 AI is at Work! "):
        result = reader.readtext(np.array(input_image))
        
        # Join all the text results into a single string
        result_text = ' '.join([text[1] for text in result])
        
        st.write(result_text)
        st.balloons()
else:
    st.write("Upload an Image")

# Credits
# # st.caption("Made with ❤️ by @1littlecoder")



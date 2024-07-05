from dotenv import load_dotenv
load_dotenv()  # loads all the env variables from .env
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("google_api_key"))

# func to load gemini pro model
model = genai.GenerativeModel('gemini-pro-vision')


def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    if response.parts:
        return response.parts[0].text
    else:
        return "The response was blocked due to safety reasons."

def input_image_details(uploaded_pic):
    if uploaded_pic is not None:
        # converting file into bytes
        bytes_data = uploaded_pic.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_pic.type,  # get the mime type of the uploaded pic
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# initializing the streamlit app
st.set_page_config(page_title='gemini application')
st.header('Multilanguage Invoice Extractor')
input = st.text_area("Input prompt:", key="input")
uploaded_pic = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_pic is not None:
    image = Image.open(uploaded_pic)
    st.image(image, caption="Uploaded image", use_column_width=True)

# submit button
submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice and you will have to answer any
questions based on the uploaded invoice image.
"""

# if submit button is clicked
if submit:
    if uploaded_pic is not None:
        image_data = input_image_details(uploaded_pic)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload an image to get a response.")

import streamlit as st
from PIL import Image, ImageEnhance
from businesslogi import stablediffusionmodel
import requests

def main_method():
    st.title("Stable Diffusion Demo")

    url = st.text_input("Enter the url")
    prompt = st.text_input("Enter textual prompt")

    if st.button("Generate Image"):
        with st.spinner(text = "Analysing your query"):
            # data = {"prompt": "A diamond ring"}
            # r = requests.post(url, json=data)
            # print(r.text)
            # st.markdown(r.text) 
            st.image(stablediffusionmodel().generate_image("Generate an image of a flying bat"))

if __name__ == "__main__":
    main_method()


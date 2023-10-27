import torch
from diffusers import StableDiffusionPipeline
from torch import autocast
import streamlit as st

class stablediffusionmodel:
    @st.cache
    def generate_image(self,prompt):
        model_path = "/content/pytorch_lora_weights (1).safetensors"

        pipe = StableDiffusionPipeline.from_pretrained(
                "CompVis/stable-diffusion-v1-4", 
                revision="fp16", 
                use_auth_token='False'
                )
        pipe = pipe.to('cpu')
        with autocast('cpu'):
            image = pipe(prompt)[0][0]
        image.save(r"img\diffusionimage.png")

        return "img\diffusionimage.png"   

# if __name__ =="__main__":
#      stablediffusionmodel().generate_image("Generate an image of a flying bat")

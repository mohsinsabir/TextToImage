# Install required libraries (if not installed already)
# !pip install streamlit transformers diffusers torch

import streamlit as st
from transformers import pipeline

# Load the pre-trained image generation model from Hugging Face
# You can change the model to other image generation models from Hugging Face
model_name = "CompVis/stable-diffusion-v1-4"  # Stable Diffusion model
image_generator = pipeline("text-to-image", model=model_name)

# Streamlit app title
st.title("Text to Image Generation using Hugging Face")

# Text input from the user for image generation
text = st.text_input("Enter a description for image generation", "")

# When the user clicks the button, generate the image based on the input text
if st.button("Generate Image"):
    if text:
        with st.spinner("Generating image..."):
            images = image_generator(text, num_images_per_prompt=1)
            # Display generated image
            st.image(images[0], caption="Generated Image")
    else:
        st.write("Please enter a description for image generation.")

# To run the Streamlit app, save this script and run: streamlit run <script_name>.py

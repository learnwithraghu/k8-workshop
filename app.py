import streamlit as st
from PIL import Image

# Load and rotate the image to be vertical
img = Image.open("raghu.jpg")
img = img.rotate(250, expand=True)  # Rotate 90 degrees counter-clockwise

st.image(img, caption="Raghu in Action!")

reaction_level = st.slider("Rate Raghu's awesomeness!", 1, 10, 5)

if reaction_level == 10:
    st.write("💯 Agreed! Raghu's the absolute best!")
elif reaction_level >= 5:
    st.write("👍 He's pretty cool, but there's always room to grow!")
else:
    st.write("🤔 Hmm, maybe next time he'll impress you more.") 

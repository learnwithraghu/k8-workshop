import streamlit as st
from PIL import Image

# Load and rotate the image to be vertical
img = Image.open("raghu.jpg")
img = img.rotate(250, expand=True)  # Rotate 90 degrees counter-clockwise

# --- New Interactive Slider ---

st.markdown(
    """
    <style>
        .stSlider > div > div > div > div {
            background-color: #FFA500;  /* Orange for more visual appeal */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

reaction_level = st.slider("**Rate Raghu's Awesomeness!** 🤯", 1, 10, 5)

# --- Conditional Reactions ---
if reaction_level == 10:
    confirm_best = st.checkbox("Whoa! Are you *absolutely sure* Raghu's the best?")
    if confirm_best:
        st.image(img, caption="Raghu in Action! 😎")
        st.write("💯 Alright, alright! We get it, Raghu's your hero! 🥳")
    else:
        st.write("🤔 Maybe dial it back a notch? 😉")
elif reaction_level >= 5:
    st.write("👍 Raghu's got some moves, but can he moonwalk? 🤔")
else:
    st.write("😂 Did Raghu trip over his shoelaces again? 🤪")

import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Rate Raghu's Awesomeness!",
    page_icon="🤯",
    layout="centered"
)

# Title
st.title("Rate Raghu's Awesomeness! 🤯")

# Display the image
image_path = "static/raghu.jpg"
if os.path.exists(image_path):
    st.image(image_path, caption="Raghu in Action!", use_column_width=True)
else:
    st.error("Image not found! Please make sure raghu.jpg is in the static folder.")

# Rating slider
rating = st.slider("How awesome is Raghu?", min_value=0, max_value=10, value=5)

# Submit button
if st.button("Submit Rating!", type="primary"):
    # Generate funny messages based on rating
    if rating == 10:
        st.success("🎉 Wow thanks a lot! Raghu is absolutely amazing! 🌟")
        st.balloons()
    elif rating == 9:
        st.success("😍 Almost perfect! Raghu is fantastic! ⭐")
    elif rating == 8:
        st.success("👏 Great job Raghu! You're doing awesome! 🎊")
    elif rating == 7:
        st.info("👍 Pretty good! Raghu's got some solid skills! 💪")
    elif rating == 6:
        st.info("😊 Not bad at all! Raghu's on the right track! 🚀")
    elif rating == 5:
        st.warning("🤔 Right in the middle! Raghu's got potential! 📈")
    elif rating == 4:
        st.warning("😅 Room for improvement! Keep going Raghu! 💪")
    elif rating == 3:
        st.warning("🤷‍♂️ Could be better! What can Raghu work on? 🔧")
    elif rating == 2:
        st.error("😬 Ouch! Raghu might need some practice! 📚")
    elif rating == 1:
        st.error("😱 Yikes! Time for Raghu to level up! 🎮")
    else:  # rating == 0
        st.error("🤔 Hey what can Raghu do better? Everyone starts somewhere! 🌱")

# Add some fun info
st.markdown("---")
st.markdown("### 📊 Your Rating: " + "⭐" * rating + "☆" * (10 - rating))
st.markdown(f"**Score: {rating}/10**")

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ using Streamlit*")

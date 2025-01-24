import streamlit as st

from my_components import footer


def say_hi(name, emoji):
    """A function that prints a friendly message"""
    st.write(f"Hi, {name}! {emoji}")


st.title("Streamlit: Basic elements")

st.markdown(
    """
    ## What is this?

    This is a :streamlit: Streamlit web application that showcases some
    basic elements of Streamlit!
    """
)

st.divider()

st.markdown(
    """
    There is great support for :rainbow[GitHub-flavored] Markdown.

    You can also use [LaTeX expressions](https://katex.org/docs/supported.html), which is great for formulas:

    $$\\sqrt{-1} \\cdot 2^3 \\sum \\pi = \\text{delicious}$$

    You can use [emojis](https://share.streamlit.io/streamlit/emoji-shortcodes), which is :100: % :sunglasses:.

    You can even use [Google Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded)
    like :material/search: :material/home: :material/delete:
    """
)

st.divider()

st.markdown("## Input elements")

user_name = st.text_input(label="What's your name?", placeholder="Type your name here!")

emoji = st.radio(
    label="Choose your style", options=[":wave:", ":sunglasses:", ":heart:"]
)

do_say_hi = st.button(label="Say hi!", use_container_width=True, type="primary")

if not user_name and do_say_hi:
    st.warning("Tell me your name first!")

if user_name and do_say_hi:
    say_hi(user_name, emoji)

st.divider()

confusion_level = st.slider(
    label="Current confusion level", min_value=0, max_value=1_000_000
)

current_confusion = "Current confusion: "
if confusion_level < 100_000:
    current_confusion += ":sunglasses:"
elif confusion_level < 500_000:
    current_confusion += ":thinking_face:"
else:
    current_confusion += ":face_with_spiral_eyes:"

current_confusion

st.divider()

streamlit_day = st.date_input(label="The day I learned about Streamlit")

pic = st.camera_input(label="What I looked like learning about Streamlit!")


if pic:
    st.download_button(
        label="Save pic", data=pic, file_name=f"{streamlit_day}-streamlit.jpg"
    )

footer()

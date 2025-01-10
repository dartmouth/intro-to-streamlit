import streamlit as st


def say_hi(name):
    st.write(f"Hi, {name}! 👋")


def say_whatsup(name):
    st.write(f"What's up, {name}? 😎")


st.title("Streamlit: Basic elements")

user_name = st.text_input(label="What's your name?")

col1, col2 = st.columns(2)

with col1:
    do_say_hi = st.button(label="Say hi!", use_container_width=True, type="primary")

with col2:
    do_say_whatsup = st.button(
        label="Say what's up!", use_container_width=True, type="secondary"
    )

if user_name and do_say_hi:
    say_hi(user_name)

if user_name and do_say_whatsup:
    say_whatsup(user_name)

import streamlit as st

st.write("# Session State in Streamlit")

# Basic pattern of interaction with session state:
if "example_key" not in st.session_state:
    st.session_state["example_key"] = ":star: My God, it's full of state! :star:"

st.write(st.session_state.example_key)

st.divider()

# Why state is needed - stateless example
col1, col2 = st.columns(2)
with col1:
    button1 = st.button(label="Button 1")
with col2:
    button2 = st.button(label="Button 2")

if button1:
    st.write("Button :one: was just clicked!")

if button2:
    st.write("Button :two: was just clicked!")

# Stateful version
with col1:
    button3 = st.button(label="Button 3")

if button3:
    st.session_state.button3_was_clicked = True

if "button3_was_clicked" in st.session_state and st.session_state.button3_was_clicked:
    st.write("Button :three: was clicked at least once!")


# on_click event
def on_button4():
    st.session_state["button4_was_clicked"] = True


with col2:
    st.button(label="Button 4", on_click=on_button4)

if "button4_was_clicked" in st.session_state and st.session_state.button4_was_clicked:
    st.write("Button :four: was clicked at least once!")

st.divider()

st.text_input("Say something interesting!", key="name")

# This exists now:
st.write(st.session_state.name)

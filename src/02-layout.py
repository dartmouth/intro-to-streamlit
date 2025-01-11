import streamlit as st

st.title("Customizing the layout of a Streamlit app")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Here is column 1")

with col2:
    st.button("column 2", use_container_width=True)

with col3:
    with st.container(border=True):
        st.radio(label="letters", options=["a", "b", "c"], horizontal=True)

with st.expander(label="Additional options"):
    st.slider(label="Number", min_value=0, max_value=10)

import streamlit as st
st.title("Welcome to Streamlit")
st.text_input("Enter your name:", key="name_input")
st.button("Greet Me", on_click=lambda: st.session_state.update(greeted=True))
if st.session_state.get("greeted"):
    st.write(f"Hello, {st.session_state.name_input}!")
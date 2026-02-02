import streamlit as st

discounted_price = 0.0
st.number_input("Enter product price:", min_value=0.0, key="price_input")
st.slider("Enter discount percentage:", value=25, min_value=0, max_value=100, key="discount_input")
st.button("Calculate Discounted Price", on_click=lambda: st.session_state.update(calculated=True))
if st.session_state.get("calculated"):
    discounted_price = st.session_state.price_input * (1 - st.session_state.discount_input / 100)
    st.success(f"Discounted Price: Rs{discounted_price:.2f}")

st.table({
    "Original Price": [st.session_state.price_input],
    "Discount Percentage": [st.session_state.discount_input],
    "Discounted Price": [discounted_price]})
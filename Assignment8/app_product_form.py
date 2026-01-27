import streamlit as st

st.sidebar.title("Product Entry Form")
st.text_input("Enter product name:", key="product_name_input")
st.selectbox("Enter product category:", options=["Electronics", "Clothing", "Books", "Home & Kitchen"], key="product_category_input")
st.number_input("Enter product price:", min_value=0.0, key="product_price_input")
st.sidebar.button("Submit Product", on_click=lambda: st.session_state.update(submitted=True))
if st.session_state.get("submitted"):
    st.success(f"Product '{st.session_state.product_name_input}' in category '{st.session_state.product_category_input}' with price Rs{st.session_state.product_price_input:.2f} submitted successfully!")

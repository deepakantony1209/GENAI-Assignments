import streamlit as st
st.title("Simple Sales Dashboard")
st.text("Welcome to the Sales Dashboard. Use the sidebar to navigate between different functionalities.")
selected_month = st.selectbox("Select Month:", options=["January", "February", "March", "April"])

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

st.write(f"Sales Data for {selected_month}: Rs {sales[selected_month]}")
st.metric(label="Total Sales", value=f"Rs {sales[selected_month]}")

# Displaying sales as barchart
st.bar_chart(list(sales.values()))
import streamlit as st
st.set_page_config(page_title="portfolio" )
st.header("🌱K-Mart")
st.subheader("Pick Fresh, Live Vibrant!!")
st.sidebar.title("Available")
menu = st.sidebar.radio("Go to", ["Vegetables","Fruits","Contact"])
if menu == "Vegetables":
    st.title("Available Vegies")
    st.subheader("Potato")
    st.subheader("Carrot")
    st.subheader("Beans")
    st.subheader("Brinjal")
    st.text_input("Enter Vegetable:")
    if st.button("Enter"):
        st.success("Farm to Table")
        st.success("Thank You")

elif menu == "Fruits":
    st.title("Available Fruits")
    st.subheader("Apple")
    st.subheader("Grapes")
    st.subheader("Mango")
    if st.button("Enter"):
        st.success("Farm to Table")
        st.success("Thank You")
elif menu == "Contact":
    st.header("Contact Me")
    st.write("email:keerthi@gmail.com")
    st.write("Mobile no:9876543322")
    st.header("Free Door Delivery..")
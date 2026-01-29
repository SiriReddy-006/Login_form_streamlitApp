import streamlit as st

#Header of the application
st.header("Registration form")
#horizontal line
st.markdown("--------------------------------------------------------")

#text method to display information 
st.text("This application allows you to perform CRUD operations on student records using a MySQL database.")

name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
password = st.text_input("Enter your password:")
st.divider()
if st.button("register"):
    st.success("registration successful")
    
    

with st.form("my_form"):
    name=st.text_input("name")
    age=st.number_input("age",0,100)
    submit=st.form_submit_button("submit")
if submit:
    st.write(name,age)
st.divider()
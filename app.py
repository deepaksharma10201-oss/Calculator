import streamlit as st
st.title("Basic Calculator")

num1 = st.number_input("Enter the First Number: ")
num2 = st.number_input("Enter the Second Number: ")

operation = st.selectbox("Select operation: ",["Add" , "Subtract" , "Multiply" , "Divide"])

if st.button("calculate"):
    if operation == "Add":
        st.write(num1 + num2)
    elif operation == "Subtract":
        st.write(num1- num2) 
    elif operation == "Multiply":
        st.write(num1*num2)
    elif operation == "Divide":
        if num2 == 0:
            st.error("Division by zero is not allowed")
        else:
            st.write(num1/num2)
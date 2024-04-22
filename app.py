import streamlit as st
from langchain_module import get_product_description  

def main():
    st.title("Product Description Generator")
    st.header("Enter a Product Name")

    product_name = st.text_input("Product Name:")

    if st.button("Generate Description"):
        description = get_product_description(product_name)
        st.write(description)

if __name__ == "__main__":
    main()

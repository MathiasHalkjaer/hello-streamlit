import streamlit as st
import pandas as pd

# Streamlit app
def main():
    st.write("# :balloon: Welcome to Streamlit! 👋")
    conn = st.connection("sql")
    pet_owners = conn.query('select top 10 * from Sales.Customer')
    st.write("Test")
    st.dataframe(pet_owners)
    st.write(pet_owners)
if __name__ == "__main__":
    main()
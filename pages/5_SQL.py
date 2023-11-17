import streamlit as st
import pandas as pd

# Streamlit app
def main():
    conn = st.connection("sql")
    pet_owners = conn.query('select top 10 * from Sales.Customer')
    st.dataframe(pet_owners)
if __name__ == "__main__":
    main()
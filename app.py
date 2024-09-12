import streamlit as st
import pandas as pd
from data import insert_data_in_bulk


def extract_excels_data(excel_file):
    try:
        
        df = pd.read_excel(excel_file)
        return df
    except Exception as e:
        
        st.error(f"Error reading the Excel file: {e}")
        return None


st.title("Upload company and employees files")


uploaded_files = st.file_uploader("Upload Excel files", type=["xls", "xlsx"], accept_multiple_files=True)

if uploaded_files and len(uploaded_files) >= 2:
    
    df1 = extract_excels_data(uploaded_files[0])
    df2 = extract_excels_data(uploaded_files[1])

    if df1 is not None and df2 is not None:
        
        st.write("DataFrame file 1:")
        st.dataframe(df1)

        st.write("DataFrame file 2:")
        st.dataframe(df2)

        
        if st.button("Merge DataFrames"):
            
            merged_df = pd.merge(df1, df2, on='Cod_Empleado', how='inner')

            st.write("Merged DataFrame")
            st.dataframe(merged_df)
            
            
            insert_data_in_bulk(merged_df)
            
            st.write("Data frame merged successfully.")
    else:
        
        st.error("Error: One or both files could not be read.")




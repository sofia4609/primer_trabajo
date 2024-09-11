import streamlit as st
import pandas as pd
from data import insert_data_in_bulk

# Función para leer datos de un archivo Excel
def extract_excels_data(excel_file):
    try:
        # Leer el archivo Excel y devolver un DataFrame de pandas
        df = pd.read_excel(excel_file)
        return df
    except Exception as e:
        # Mostrar un mensaje de error si ocurre un problema al leer el archivo
        st.error(f"Error reading the Excel file: {e}")
        return None

# Título de la aplicación
st.title("Upload company and employees files")

# Permitir al usuario subir múltiples archivos Excel
uploaded_files = st.file_uploader("Upload Excel files", type=["xls", "xlsx"], accept_multiple_files=True)

if uploaded_files and len(uploaded_files) >= 2:
    # Leer los archivos subidos
    df1 = extract_excels_data(uploaded_files[0])
    df2 = extract_excels_data(uploaded_files[1])

    if df1 is not None and df2 is not None:
        # Mostrar ambos DataFrames en la aplicación
        st.write("DataFrame file 1:")
        st.dataframe(df1)

        st.write("DataFrame file 2:")
        st.dataframe(df2)

        # Botón para unir los DataFrames
        if st.button("Merge DataFrames"):
            # Unir DataFrames usando 'Cod_Empleado' como clave
            merged_df = pd.merge(df1, df2, on='Cod_Empleado', how='inner')

            st.write("Merged DataFrame")
            st.dataframe(merged_df)
            
            # Insertar los datos combinados en la base de datos
            insert_data_in_bulk(merged_df)
            
            st.write("Data frame merged successfully.")
    else:
        # Mostrar un mensaje de error si alguno de los archivos no se pudo leer
        st.error("Error: One or both files could not be read.")

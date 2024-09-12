import mysql.connector
import os
import streamlit as st


def insert_data_in_bulk(df, table_name='empleados'):
    connection = None
    cursor = None

    try:
        
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            st.write("Connected to the database successfully.")
            cursor = connection.cursor()

            # 
            
            insert_query = f"""
                INSERT INTO {table_name} (Cod_Empleado, Empleado, Email, Area, Horario)
                VALUES (%s, %s, %s, %s, %s)
                """

            
            data = df[['Cod_Empleado', 'Empleado', 'Email', 'Area', 'Horario']].to_records(index=False).tolist()

            
            cursor.executemany(insert_query, data)
            
            
            connection.commit()

            st.write(f"{cursor.rowcount} rows inserted successfully.")

    except mysql.connector.Error as e:
        st.write(f"Error: {e}")
        if connection:
            connection.rollback()


    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

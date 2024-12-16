import streamlit as st
import mysql.connector
import pandas as pd

# Database connection details
db_config = {
    "host": "82.197.82.122",
    "port": 3306,
    "database": "u692129437_db",
    "user": "u692129437_user",
    "password": "SpicyBrown73!fml483"
}

# Establish the connection
def get_db_connection():
    conn = mysql.connector.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"]
    )
    return conn

# Fetch data from the table
def fetch_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Get results as dictionaries
    cursor.execute("SELECT age FROM test_table")  # Replace 'your_table_name' with the actual table name
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Streamlit UI
st.title("MySQL Database Viewer")

# Fetch and display the data
try:
    data = fetch_data()
    if data:
        df = pd.DataFrame(data)  # Convert to DataFrame for better display
        st.write(df)
    else:
        st.write("No data found in the table.")
except Exception as e:
    st.error(f"Error: {e}")

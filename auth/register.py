import streamlit as st
from db.server import get_db_connection

def add_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO tbl_user1 (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    
def register():
    st.subheader("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    button = st.button("Register")

    if button:
        try:
            add_user(username, password)
            st.success("User registered successfully")
        except Exception as e:
            st.error(f"Error: {e}")
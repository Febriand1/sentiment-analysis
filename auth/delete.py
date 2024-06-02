import streamlit as st
from db.server import get_db_connection

def delete_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM tbl_user1 WHERE username = %s"
    val = (username)
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()

def delete():
    st.subheader("Delete User")

    username = st.text_input("Username", key="delete_username")
    button = st.button("Delete", key="delete_button")

    if button:
        delete_user(username)
        st.success("User deleted successfully")
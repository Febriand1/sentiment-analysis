import streamlit as st
from db.server import get_db_connection

def validate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM tbl_user1 WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def login():
    st.subheader("Login")

    st.session_state['username'] = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    button = st.button("Login", key="login_button")

    if button:
        user = validate_user(st.session_state['username'], password)
        if user:
            st.session_state['authentication_status'] = True
            st.session_state['username'] = user['username']
        else:
            st.error('Username/password is incorrect')
            st.session_state['authentication_status'] = False

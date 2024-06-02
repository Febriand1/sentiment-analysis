import streamlit as st
from db.server import get_db_connection

def update_user(username, password, new_username, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_check = "SELECT * FROM tbl_user1 WHERE username =%s AND password = %s"
    val_check = (username, password)
    cursor.execute(sql_check, val_check)
    result = cursor.fetchone()

    if result:
        sql_update = "UPDATE tbl_user1 SET username = %s, password = %s WHERE username =%s AND password = %s"
        val_update = (new_username, new_password, username, password)
        cursor.execute(sql_update, val_update)
        conn.commit()
        st.success("Data TerUpdate")
    else :
        st.error("Username atau password lama tidak cocok")
    cursor.close()
    conn.close()

def update():
    st.subheader("Update User")

    username = st.text_input("Username Lama", key="update_username")
    password = st.text_input("Password Lama", type="password", key="update_password")
    new_username = st.text_input("Username Baru", key="update_new_username")
    new_password = st.text_input("Password Baru", type="password", key="update_new_password")
    button = st.button("Update", key="update_button")

    if button:
        update_user(username, password, new_username, new_password)
    

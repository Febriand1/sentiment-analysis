import streamlit as st
from scripts.data_loading import load_dataframe
from scripts.plotting import create_pie_chart

def show_1000_data():
    st.subheader("Dataframe komentar 1000 Data:")
    df2_final = load_dataframe('dt2_final.csv')
    st.dataframe(df2_final)

    st.subheader("Pie Chart Hasil Sentiment 1000 Data:")
    fig2 = create_pie_chart(df2_final, "Sentiment Distribution for 1000 Data")
    st.plotly_chart(fig2)

import streamlit as st
from scripts.data_loading import load_dataframe
from scripts.plotting import create_pie_chart

def show_500_data():
    st.subheader("Dataframe komentar 500 Data :")
    df1_final = load_dataframe('dt1_final.csv')
    st.dataframe(df1_final)

    st.subheader("Pie Chart Hasil Sentiment 500 Data:")
    fig1 = create_pie_chart(df1_final, "Sentiment Distribution for 500 Data")
    st.plotly_chart(fig1)

import streamlit as st
import pandas as pd

st.title("Better Ranking European Football Teams")

data = pd.read_csv("data_clean.csv")
data.drop("Unnamed: 0", inplace=True, axis = 1)
results = pd.read_csv("data_ranked.csv")
results.drop("Unnamed: 0", inplace=True, axis = 1)


def color_champ(val):
    if val == "ESP":
        color = '#ffed75'
    elif val == "FRA":
        color = "#78c8eb"
    elif val == "ITA":
        color = "#6bcf96"
    elif val == "ANG":
        color = "#f27278"
    else :
        color = ""
    return f'background-color: {color}'

st.write("Initial Data after Scraping")
st.dataframe(data)

st.write("Data with calculated ranks and adjusted ratings")
st.dataframe(results)

st.dataframe(results.style.applymap(color_champ, subset=['Championnat']))

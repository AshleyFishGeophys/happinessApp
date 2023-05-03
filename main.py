import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

option_x = st.selectbox("Select the data for the x-axis ",
                        ("country", "happiness", "gdp", "social_support",
                         "life_expectancy", "freedom_to_make_life_choices",
                         "generosity", "corruption"))

option_y = st.selectbox("Select the data for the y-axis ",
                        ("country", "happiness", "gdp", "social_support",
                         "life_expectancy", "freedom_to_make_life_choices",
                         "generosity", "corruption"))

st.subheader(f"{option_x} and {option_y}")

df = pd.read_csv("happy.csv")


def get_data(x, y):
    return df[x], df[y]


data_x, data_y = get_data(option_x, option_y)

figure = px.scatter(x=data_x, y=data_y, labels={"x": option_x, "y": option_y})

st.plotly_chart(figure)

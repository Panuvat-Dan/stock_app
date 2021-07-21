import streamlit as st
import datetime as dt
import pandas as pd
from datetime import date
import yfinance as yf
from plotly import graph_objs as go
import numpy as np
from PIL import Image

st.title("Welcome to FANG stock detail Webapp")
image = Image.open('fang.jpg')
st.image(image, width=500, caption='Stock')

stocks = ("FB", "AMZN", "NFLX", "GOOGL")
selected_stocks = st.sidebar.selectbox("Select dataset for prediction", stocks)

start = st.sidebar.date_input("Please select start date:")
end = st.sidebar.date_input("Please select end date")


def load_data(ticker):
    data = yf.download(ticker, start, end)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text("Please wait for loading ...")
data = load_data(selected_stocks)
data_load_state.text("Data loading ... done!")

st.subheader('Quick overview Raw datafrmae')
st.write(data.tail(10))


def plot_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Open'], name="Stock opening volume"))
    fig.add_trace(go.Scatter(
        x=data['Date'], y=data['Close'], name="Stock closing volume"))
    fig.layout.update(title_text="Time Series Data",
                      xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    st.text("Please hold slider to see dynamic timeline of stock")


plot_data()

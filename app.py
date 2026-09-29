import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# 1. Initialize the Layout Structure
st.set_page_config(page_title="FinTrack Dashboard", layout="wide")
st.title("📈 FinTrack Analytics Dashboard")

# 2. Build the Control Inputs in the Left Sidebar
st.sidebar.header("Controls")
ticker_input = st.sidebar.text_input("Ticker Symbol (e.g., AAPL, BTC-USD)", value="BTC-USD").upper()
time_period = st.sidebar.selectbox("Time Horizon", options=["1mo", "3mo", "6mo", "1y"])

# 3. Pull Data and Process Calculations
if ticker_input:
    try:
        ticker_data = yf.Ticker(ticker_input)
        df = ticker_data.history(period=time_period)
        
        if df.empty:
            st.error("Ticker symbol not found. Try 'AAPL' or 'BTC-USD'.")
        else:
            # Algorithmic variables extracting data points
            latest_price = df['Close'].iloc[-1]
            previous_price = df['Close'].iloc[0]
            percent_change = ((latest_price - previous_price) / previous_price) * 100
            
            # Display numbers cleanly in columns
            col1, col2 = st.columns(2)
            col1.metric("Current Price", f"${latest_price:,.2f}", f"{percent_change:+.2f}%")
            col2.metric("Period High", f"${df['High'].max():,.2f}")

            # Plot interactive time-series curve
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Price'))
            fig.update_layout(template="plotly_dark", xaxis_title="Date", yaxis_title="Price (USD)")
            st.plotly_chart(fig, use_container_width=True)
            
    except Exception as e:
        st.error("Network connection error. Try again.")

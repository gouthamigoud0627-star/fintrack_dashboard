# 📈 FinTrack: Live Market Analytics Dashboard

A responsive, single-page data analytics application designed to extract, compute, and visualize live equity and cryptocurrency market data in real-time.

## 🔗 Live Application
👉 **[Launch Live Dashboard on Streamlit Cloud](https://streamlit.app)** *(Replace with your exact link)*

## 🛠️ Technical Architecture & Ecosystem
- **Core Engine:** Python 3.14
- **Data Engineering Framework:** Pandas (for array processing, data alignment, and tracking calculations)
- **Data Source Integrations:** Yahoo Finance API (`yfinance`) for streaming historical price intervals
- **Data Visualization UI:** Plotly Graph Objects (for responsive vector time-series curves)
- **Deployment Tier:** Streamlit Community Cloud with continuous integration workflows

## 🔍 Core Programmatic Mechanics
1. **API Validation:** The application calls the Yahoo Finance server to validate user-input ticker strings (e.g., `AAPL`, `TSLA`, `BTC-USD`, `RELIANCE.NS`), dynamically handling data-empty queries gracefully.
2. **Algorithmic Analytics:** Implements array indexing math (`.iloc`) via **Pandas** to isolate precise closing boundaries, programmatically calculating period-bounded performance deltas and historical peaks.
3. **Interactive Rendering:** Translates raw numerical data points into vector graphics, allowing users to hover dynamically over coordinates for data extraction.

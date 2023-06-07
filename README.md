# Cryptocurrency-Trading-Signal-Generator-with-Interactive-Visualization

This project leverages Python libraries including yfinance, pandas, and plotly to create a powerful, yet user-friendly, trading signal generator for cryptocurrency markets. 

The application downloads historical price data for a specific cryptocurrency, calculates short-term and long-term simple moving averages (SMA), and uses these metrics to generate trading signals. 

The signals produced by the system include 'Buy', 'Sell', and 'Hold', which are determined by comparing the 20-day and 100-day SMAs. 

A 'Buy' signal is issued when the short-term SMA crosses above the long-term SMA, and a 'Sell' signal is issued when the short-term SMA crosses below the long-term SMA. 

'Hold' signals are issued when no significant change is detected. An interactive visualization of the price data and trading signals is also created using plotly, allowing users to intuitively explore the data and signals. 

Key points of buying and selling are highlighted on the chart, along with the close price and moving averages. Additionally, the project exports the data and trading signals to a CSV file, facilitating further analysis and record-keeping. 

This combination of analytical capabilities and intuitive visualization makes the Cryptocurrency Trading Signal Generator a valuable tool for both novice and experienced cryptocurrency traders.

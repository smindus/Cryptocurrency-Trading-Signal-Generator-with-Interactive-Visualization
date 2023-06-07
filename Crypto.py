import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py

# Download historical data for desired crypto currency
data = yf.download('BTC-USD', start='2020-01-01', end='2022-12-31')

# Calculate short/simple moving average over the last 20 days
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Calculate long/simple moving average over the last 100 days
data['SMA_100'] = data['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if 20-day SMA is greater than 100-day SMA then Signal is 1 else it's 0
data['Signal'] = 0.0  
data['Signal'][data['SMA_20'] > data['SMA_100']] = 1.0

# Generate trading orders using the 'Signal' column. If Signal shifts from 0 to 1 then it's a 'Buy', if it shifts from 1 to 0 then it's a 'Sell'
data['Position'] = data['Signal'].diff()

# Create a new column 'Trading_Signal' to store 'Buy', 'Sell', 'Hold' signals
data['Trading_Signal'] = ''
data.loc[data['Position'] == 1, 'Trading_Signal'] = 'Buy'
data.loc[data['Position'] == -1, 'Trading_Signal'] = 'Sell'
data.loc[data['Position'] == 0, 'Trading_Signal'] = 'Hold'

# Write data to a CSV file
data.to_csv('output.csv')

# Plotting data using plotly.graph_objs
trace1 = {
    'x': data.index,
    'open': data.Open,
    'close': data.Close,
    'high': data.High,
    'low': data.Low,
    'type': 'candlestick',
    'name': 'BTC-USD',
    'showlegend': False
}

# Moving averages
trace2 = {
    'x': data.index,
    'y': data['SMA_20'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'SMA of 20 days'
}

trace3 = {
    'x': data.index,
    'y': data['SMA_100'],
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
    },
    'name': 'SMA of 100 days'
}

# Buying points
trace4 = {
    'x': data[data['Position'] == 1].index,
    'y': data[data['Position'] == 1]['Close'],
    'mode': 'markers',
    'marker': {
        'color': 'green',
        'size': 10,
        'line': {
            'width': 2,
            'color': 'black'
        },
        'symbol': 'triangle-up'
    },
    'name': 'Buy'
}

# Selling points
trace5 = {
    'x': data[data['Position'] == -1].index,
    'y': data[data['Position'] == -1]['Close'],
    'mode': 'markers',
    'marker': {
        'color': 'red',
        'size': 10,
        'line': {
            'width': 2,
            'color': 'black'
        },
        'symbol': 'triangle-down'
    },
    'name': 'Sell'
}

data = [trace1, trace2, trace3, trace4, trace5]

layout = go.Layout({
    'title': {
        'text': 'BTC-USD Trading Signals',
        'font': {
            'size': 15
        }
    }
})

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='simple_candlestick')
# filename: plot_stocks.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols
symbols = ['NVDA', 'TSLA']

# Fetch the stock data for the year to date
data = yf.download(symbols, start='2023-01-01', end='2023-12-31')['Close']

# Plot the data
plt.figure(figsize=(10, 5))
for symbol in symbols:
    plt.plot(data.index, data[symbol], label=symbol)

plt.title('YTD Stock Price Change for NVDA and TESLA')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
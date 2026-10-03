# Activity 21: Import Data from Yahoo Finance

**Topic 06: Modules & Packages**  ·  Focus: download live market data and plot it

Use the yfinance package to download Singtel (Z74.SI) stock data from Yahoo Finance for a date range, then plot the closing price.

**You'll build:** A live Yahoo Finance download and a closing-price chart.

**Tools:** yfinance, pandas, matplotlib

## Steps

1. Import yfinance and download one year of Singtel data.

   ```python
   import yfinance as yf
   stock = yf.download('Z74.SI', start='2024-01-01', end='2024-12-31')
   print(stock.tail())
   ```

2. Select the closing price.

   ```python
   stock_close = stock[['Close']]
   ```

3. Plot it, with title and axis labels.

   ```python
   import matplotlib.pyplot as plt
   plt.figure(figsize=(14, 5))
   plt.plot(stock_close, 'b')
   plt.plot(stock_close, 'ro')
   plt.title('Singtel Close Price Representation')
   plt.xlabel('Trading Days')
   plt.ylabel('Close Price')
   plt.show()
   ```

4. Try another ticker — e.g. D05.SI (DBS) or AAPL — and rerun.

   ```python
   stock = yf.download('D05.SI', start='2024-01-01', end='2024-12-31')
   ```


## Check your result

tail() shows recent trading rows and the chart plots a year of closing prices; swapping the ticker redraws the chart for the new stock.

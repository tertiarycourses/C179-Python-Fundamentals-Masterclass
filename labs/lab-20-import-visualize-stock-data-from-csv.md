# Activity 20: Import & Visualize Stock Data from CSV

**Topic 06: Modules & Packages**  ·  Focus: load a CSV with pandas and chart it with matplotlib

Import historical stock data from a CSV file with pandas, select the closing price and visualize the price history with matplotlib.

**You'll build:** A line chart of the Singtel closing-price history from a CSV file.

**Tools:** pandas, matplotlib, CSV (labs/data/singtel.csv)

## Steps

1. Import pandas and load the CSV (upload labs/data/singtel.csv to Colab, or use its path in your IDE).

   ```python
   import pandas as pd
   stock = pd.read_csv('singtel.csv')
   print(stock.head())
   ```

2. Select the closing-price column.

   ```python
   stock_close = stock[['Close']]
   ```

3. Plot the price history with matplotlib — line plus point markers.

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

4. Read the chart: where were the highest and lowest closes?

## Check your result

head() shows the CSV columns (Date, Open, High, Low, Close) and a blue line chart with red markers appears, titled 'Singtel Close Price Representation'.

Data file: [data/singtel.csv](data/singtel.csv)

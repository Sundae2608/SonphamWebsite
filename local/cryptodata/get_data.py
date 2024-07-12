import cryptocompare
import pandas as pd

# Fetch historical price data for Bitcoin and Ethereum
btc_data = cryptocompare.get_historical_price_day('BTC', currency='USD', limit=365)
eth_data = cryptocompare.get_historical_price_day('ETH', currency='USD', limit=365)

# Convert data to DataFrame
btc_df = pd.DataFrame(btc_data)
eth_df = pd.DataFrame(eth_data)

# Ensure the data has a consistent datetime format
btc_df['time'] = pd.to_datetime(btc_df['time'], unit='s')
eth_df['time'] = pd.to_datetime(eth_df['time'], unit='s')

# Merge dataframes on the 'time' column
merged_df = pd.merge(btc_df, eth_df, on='time', suffixes=('_BTC', '_ETH'))

# Save to CSV
merged_df.to_csv('crypto_prices.csv', index=False)
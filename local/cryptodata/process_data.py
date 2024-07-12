import pandas as pd
import numpy as np

# Load the data
crypto_df = pd.read_csv('crypto_prices.csv')

# Calculate daily returns
crypto_df['return_BTC'] = pd.to_numeric(crypto_df['close_BTC']).pct_change()
crypto_df['return_ETH'] = pd.to_numeric(crypto_df['close_ETH']).pct_change()
print(crypto_df)

# Drop the first row with NaN values
crypto_df = crypto_df.dropna()

# Ensure the 'Close_BTC' column is in the correct forma
# Drop the first row with NaN values
crypto_df = crypto_df.dropna()

# Calculate expected returns (mean of daily returns)
expected_return = crypto_df[['return_BTC', 'return_ETH']].mean()
print(expected_return)

# Calculate volatility (standard deviation of daily returns)
volatility = crypto_df[['return_BTC', 'return_ETH']].std()

# Calculate covariance matrix
cov_matrix = crypto_df[['return_BTC', 'return_ETH']].cov()
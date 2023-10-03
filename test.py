from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()

# Fetch the current exchange rate from ILS to USD
ils_to_usd_rate = c.get_rate('ILS', 'USD')

# Calculate the conversion rate from USD to ILS
usd_to_ils_rate = 1 / ils_to_usd_rate

# Define the fixed amount in ILS to convert
ils_amount = 1.0

# Perform the conversion from ILS to USD
usd_amount = ils_amount * ils_to_usd_rate

# Print the initial result
print(f"{ils_amount:.2f} ILS is equal to {usd_amount:.2f} USD")

# Print the conversion rate from USD to ILS
print(f"1 USD is equal to {usd_to_ils_rate:.6f} ILS")

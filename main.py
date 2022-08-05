import pandas as pd

melbourne_file_path = '~/Projects/data_science-ml-dl/data/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
print(melbourne_data.describe())

# What is the average price (rounded to nearest integer)?
avg_price_amount = round(melbourne_data["Price"].mean())

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = pd.Timestamp('today').year - melbourne_data["YearBuilt"].max()

print(avg_price_amount)
print(newest_home_age)

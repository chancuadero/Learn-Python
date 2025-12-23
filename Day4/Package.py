import pandas as pd


#Sales dictionary
sales = {"user_id": ["KM37","PR19","YU88"],
         "order_value": [197.75,208.21,134.99]}

#Convert to a pandas DataFrame
sales_df = pd.DataFrame(sales)
print(sales_df)

#reading a csv file
sales_data = pd.read_csv("Day4/sales_data_sample.csv")
print(sales_data.head())
print(sales_data.info())
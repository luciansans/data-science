import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('consumer_reviews.csv')

# Display the 'name', 'brand', 'reviews', and 'rating' columns
selected_columns = data[['name', 'brand', 'reviews', 'rating']]
print(selected_columns)

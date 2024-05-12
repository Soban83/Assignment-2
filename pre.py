import pandas as pd

# Read the dataset into a DataFrame
df = pd.read_csv('dataset.txt', header=None, names=['Date', 'Title', 'Sentiment'])

# Remove any rows with missing values (if any)
df.dropna(inplace=True)

# Drop duplicate rows (if any)
df.drop_duplicates(inplace=True)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Sentiment' column to float format
df['Sentiment'] = df['Sentiment'].astype(float)

# Remove any leading or trailing whitespace from the 'Title' column
df['Title'] = df['Title'].str.strip()

# Reset index
df.reset_index(drop=True, inplace=True)

# Save the preprocessed dataset to a new file
df.to_csv('preprocessed_dataset.csv', index=False)

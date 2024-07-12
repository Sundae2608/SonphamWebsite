import pandas as pd

# Load the Excel file
file_path = "ie_data.xls"
xls = pd.ExcelFile(file_path)

# Load the sheet named 'Data' into a DataFrame, skipping the first 7 rows
df = xls.parse('Data', skiprows=7, dtype={'Date': str})


# Drop the last row
df = df[:-1]

# Select only the necessary columns
df = df[['Date', 'P', 'D', 'CPI']]


# Function to process the date column
def process_date(date_str):
    # Check if the date ends with ".1"
    if date_str.endswith('.1'):
        # Replace ".1" with ".10"
        return date_str.replace('.1', '.10')
    return date_str


# Apply the function to the 'Date' column
df['Date'] = df['Date'].apply(process_date)

# Convert to date time
df["Date"] = pd.to_datetime(df["Date"], format="%Y.%m")
df["Date"] = df["Date"].dt.strftime("%Y-%m")

# Convert the DataFrame to JSON format
json_data = df.to_json(orient='records')

# Save the JSON data to a file
json_file_path = "../../spdata.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json_data)

print("Data saved to spdata.json")
import pandas as pd
df = pd.read_csv(r"C:\Users\Saujanya Gadge\OneDrive\Desktop\internship\sales_data.csv")
print(df.head())

# 1. remove duplicates
df = df.drop_duplicates()

# 2. handling missing values 
df["Invoice ID"] = df["Invoice ID"].fillna("Unknown")
df["Customer Name"] = df["Customer Name"].fillna("Unknown")
df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df)

# 3. Customer Name format 
df["Customer Name"] = df["Customer Name"].str.title()
df["Product"] = df["Product"].str.title()

# 4. Date format standard (dd-mm-yyyy)
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")


# 5. Rename column headers to lowercase and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 6. Check and fix data types
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")


# Save back to new CSV
df.to_csv("aligned_dates_sales_data.csv", index=False)
print("File saved with aligned date format as 'aligned_dates_sales_data.csv'")


# Convert column names to uppercase
df.columns = df.columns.str.upper()

# 7. Save cleaned data to a new file
df.to_csv("cleaned_sales_data task 1.csv", index=False)
print("\n Cleaned data saved as 'cleaned_sales_data.csv'")

#by Sanyukta Gadge
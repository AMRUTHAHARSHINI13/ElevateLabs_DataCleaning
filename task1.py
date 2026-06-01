import pandas as pd

# Load CSV file
df = pd.read_csv("marketing_campaign.csv")

# Dataset info
print("Original Shape:", df.shape)

# Missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with mean
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing text values with "Unknown"
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned file saved as cleaned_marketing_campaign.csv")
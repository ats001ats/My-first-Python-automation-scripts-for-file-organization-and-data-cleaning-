import pandas as pd

# 1. CSV file ko load karo
file_path = "data.csv"
df = pd.read_csv(file_path)

print("--- Original Data ---")
print(df)

# 2. Columns ke naam aur text ke andar ki extra spaces khatam karna
df.columns = df.columns.str.strip()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.strip()

# 3. Duplicate rows ko remove karna
df = df.drop_duplicates()

# 4. Clean ki hui file ko nayi file mein save karna
output_path = "cleaned_data.csv"
df.to_csv(output_path, index=False)

print("\n--- Cleaned Data ---")
print(df)
print(f"\nSuccess! Cleaned file yahan save ho gayi hai: {output_path}")
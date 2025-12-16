import pandas as pd

data = {
    "Name": ["Ali", None, "Leyla", "Orxan", None],
    "Age": [25, 30, None, 22, 28],
    "Salary": [500, 600, None, 450, 700]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Boş olan sətirləri silirik
cleaned_df = df.dropna()

print("\nCleaned Data:")
print(cleaned_df)

# Yaşın orta dəyərini tapırıq
average_age = cleaned_df["Age"].mean()
print(f"\nAverage Age: {average_age:.2f}")

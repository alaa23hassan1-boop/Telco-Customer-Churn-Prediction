import pandas as pd

# 1. مسار ملف الأكسل
excel_path = r'C:\Users\allaa\OneDrive\Desktop\New folder\Telco_Customer_Churn.xlsx'

# 2. قراءة البيانات
df = pd.read_excel(excel_path)

print("="*50)
print(" 1. Preview First 5 Rows (df.head()):")
print("="*50)
print(df.head())

print("\n" + "="*50)
print(" 2. Dataset Information (df.info()):")
print("="*50)
print(df.info())

print("\n" + "="*50)
print(" 3. Target Variable Distribution (Churn):")
print("="*50)
print(df['Churn'].value_counts())
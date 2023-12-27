import pandas as pd
df=pd.read_excel('C:\Users\SAHYADRI\Downloads\data.xlsx')

print("first few rows")
print(df.head())

print("\n  summary statistics ")
print(df.describe())

filtered_data=df[df['Age']>30]
print("\n filtered data (Age>30):")
print("filtered_data")

sorted_data=df.sort_values(by='salary ',ascending=False)
print("\n Sorted data (by salary):")
print(sorted_data)

df['Bonus']=df['salary']*0.1
print("\n data with new column (Bonus):")
print(df)

df.to_excel('output_xlsx',index=False)
print("\n data written to output.xlsx")

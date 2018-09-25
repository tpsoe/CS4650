from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# 1. Read in the dataset
df = pd.read_csv("Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv")
# 2. Display the first 50 data entries/rows as well as last 50 entries/rows.
print("The first 50 data entries")
print("")
print(df.head(50))
print("")
print("The last 50 data entries")
print("")
print(df.tail(50))
print("")

# 3. Display a quick statistical information on all numerical columns such as count, mean, std, min, max, etc.
print("Display for quick Statistical information")
print (df.describe())
print("")

print("Select a subset of rows")
# 4. Select a subset of rows (you decide which subset to select or which criteria to use for selection.) Display the first 10 data entries selected.
print(df.loc[50 : 60, ['Provider Id', 'Provider Name', 'Provider Street Address']])
print("")
# 5. Similar to 4, but select a subset of columns (from original data). Display the first 10 data entries with selected columns.
df_subcolumn = df[" Total Discharges "]
print(df_subcolumn.head(10))
print("")
# 6. From original data, filter out some data, for example, filter out those salary lower than certain amount. After filtering out the data, display the first 50 data entries.
df_subrow = df[ df[" Total Discharges "] > 20]
print(df_subrow.head(50))
print("")
# 7. From original data, find out all entries with missing values. Display the first 10 entries.
print("Display for missing values")
flights = pd.read_csv("flights.csv")
print(flights[flights.isnull().any(axis=1)].head(10))
print("")
# 8. Manipulate the original data by changing numerical values of specific column(s) (for example, give everyone 10% raise!) Display the first 10 entries before update and after update.
print("Before 10 percent raise for Total Discharges")
print(df.head(10))
print("")
var = (df.head(10)[' Total Discharges '] * 0.1) + df.head(10)[' Total Discharges ']
df[" Total Discharges "] = var
print("After 10 percent raise for Total Discharges")
print(df.head(10))
print("")
# 9.	Sort the data set resulted from step 8 in certain way (e.g.  descending order of salaries)
print("Ascending order of Total Discharges")
df_sorted = df.sort_values( by = [' Total Discharges '] , ascending = [True])
print(df_sorted.head(10))
print("")
# 10.	Group the data set from step 9 based on certain category (e.g. group based on rank of Professor, Assoc Professor, etc.)
df_region = df_sorted.groupby('Hospital Referral Region Description') [[' Total Discharges ']].mean()
print(df_region.head())
print("")
# 11.	Plot data (or subset of data) in at least three different ways such as vertical bar graph, horizontal bar graph, curve,
df_sorted = pd.read_csv('Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv', index_col = 8)
df_sorted.head(10).boxplot()
df_sorted.head(10).plot(kind= 'bar', stacked = True)

ax = df_sorted.head(10).plot(xticks = range(4), legend=False, style=['r+-','gx-','b*-'], title='My Chart')
ax.set_xlabel('Index')
ax.set_ylabel('Columns')

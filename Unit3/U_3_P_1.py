# Write a Python script to read the data in an Excel file named
# movies.xlsx and save this data in a data frame called mov. Perform
# the following steps:

# 1. Read the contents of the second sheet that is named 2000s in
# the Excel file (movies.xlsx)and store this content in a data frame
# called Second_sheet.

import pandas as pd

# Read the Excel file
excel_file = 'moives1.xls'

# Read the second sheet named "2000s" into a DataFrame
Second_sheet = pd.read_excel(excel_file, sheet_name='2000s')

# Display the DataFrame
print(Second_sheet)

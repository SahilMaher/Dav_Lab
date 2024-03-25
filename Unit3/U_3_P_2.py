# 2. Write the code needed to show the first seven rows from the
# data frame Second_sheet usingan appropriate method.
import pandas as pd


# Read the Excel file
excel_file = 'moives1.xls'

# Read the second sheet named "2000s" into a DataFrame
Second_sheet = pd.read_excel(excel_file, sheet_name='2000s')



first_seven_rows = Second_sheet.head(7)

print(first_seven_rows)

# 5. Use a suitable command to show the total rows in the first sheet
# that is called 2000s.
import pandas as pd


# Read the Excel file
excel_file = 'moives1.xls'

first_sheet_2000s = pd.read_excel(excel_file, '2000s')

# Get the total number of rows
total_rows = first_sheet_2000s.shape[0]

print("Total rows in the '2000s' sheet:", total_rows)
# Write the code needed to show the last five rows using an
# appropriate method.
import pandas as pd


# Read the Excel file
excel_file = 'moives1.xls'

# Read the second sheet named "2000s" into a DataFrame
Second_sheet = pd.read_excel(excel_file,sheet_name='2000s').tail(5)
last_five_rows = Second_sheet.tail(5)

print(last_five_rows)
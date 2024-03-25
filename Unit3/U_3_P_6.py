# 6. Use a suitable command to show the maximum value stored in
# the Budget column.

import pandas as pd


# Read the Excel file
excel_file = 'moives1.xls'

# Read the second sheet named "2000s" into a DataFrame
Second_sheet = pd.read_excel(excel_file,sheet_name='2000s')
budget_column = Second_sheet['Budget'].max()
print(budget_column)


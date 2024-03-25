# 10. Using a suitable command, create a calculated column named
# Avg Reviews in Second_sheetby adding Reviews by Users and
# Reviews by Critics and divide it by 2. Display the first fiverows of
# the Second_sheet after creating the previous calculated column.



# Assuming you're using pandas to handle your data
import pandas as pd

# Assuming Second_sheet is your DataFrame
# Replace Second_sheet with the name of your DataFrame if it's different

# Create the calculated column Avg Reviews
excel_file = 'moives1.xls'
Second_sheet = pd.read_excel(excel_file,sheet_name='2000s')
Second_sheet['Avg Reviews'] = (Second_sheet['Reviews by Users'] + Second_sheet['Reviews by Crtiics']) / 2

# Display the first five rows of the updated dataframe
print(Second_sheet.head())

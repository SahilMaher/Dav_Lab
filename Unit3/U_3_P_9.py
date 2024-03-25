# 9. Use a suitable conditional statement that stores the rows in
# which the country name isUSA and the Duration value is less than
# 50 in a data frame named USA50. Show the values indata frame
# USA50
import pandas as pd


# Read the Excel file
excel_file = 'moives1.xls'
Second_sheet = pd.read_excel(excel_file,sheet_name='2000s')
USA50 = Second_sheet[(Second_sheet['Country'] == 'USA') & (Second_sheet['Duration'] < 50)]

print(USA50)

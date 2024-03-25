# 11. Using a suitable command, sort the Country values in
# ascending order (smallest to largest)and Avg_reviews in
# descending order (largest to smallest).




# Assuming you're using pandas to handle your data
import pandas as pd

# Assuming Second_sheet is your DataFrame
# Replace Second_sheet with the name of your DataFrame if it's different

# Create the calculated column Avg Reviews
excel_file = 'moives1.xls'
Second_sheet = pd.read_excel(excel_file,sheet_name='2000s')
Second_sheet['Avg_reviews'] = (Second_sheet['Reviews by Users'] + Second_sheet['Reviews by Crtiics']) / 2

Second_sheet_sorted = Second_sheet.sort_values(by=['Country', 'Avg_reviews'], ascending=[True, False])

# Display the sorted DataFrame
print(Second_sheet_sorted)


'''4. Write a program to create a series to maintain three students’
names and SPI values.'''


import pandas as pd

def main():
    # Create a dictionary with students' names and SPI values
    data = {'Student': ['ram', 'shyam', 'laxman'],
            'SPI': [3.5, 3.8, 3.2]}

    # Create a pandas Series
    student_series = pd.Series(data['SPI'], index=data['Student'])

    # Display the series
    print("Student Series:")
    print(student_series)

if __name__ == "__main__":
    main()
#out put 
'''ram       3.5
shyam     3.8
laxman    3.2
dtype: float64'''
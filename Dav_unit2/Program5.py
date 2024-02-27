'''5. Write a program to create a data frame to maintain three
students’ names associated with their grades in three courses and
then add a new column named Mean to maintain the calculated
mean mark per course. Display the final data frame.'''

import pandas as pd

def main():
    # Create a dictionary with students' names and their grades in three courses
    data = {'Student': ['Alice', 'Bob', 'Charlie'],
            'Math': [85, 90, 88],
            'Science': [78, 85, 80],
            'English': [92, 88, 90]}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Add a new column "Mean" to calculate the mean mark per course
    df['Mean'] = df.mean(axis=1)

    # Display the final DataFrame
    print("Final DataFrame:")
    print(df)

if __name__ == "__main__":
    main()

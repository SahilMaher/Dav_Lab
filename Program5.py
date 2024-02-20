# 5. Write a program to prompt users to enter their working hours 
# and rate per hour to calculate gross pay. The program should 
# give the employee 1.5 times the hours worked above 30 hours. If 
# Enter Hours is 50 and Enter Rate is 10, then the calculated 
# payment is Pay: 550.0.


hour=int(input("Enter Total hours"))
salary=int(input("Enter Salary"))
if hour <=30:
    print("Total is :-",salary*hour)
else:
    print("Total is :-",30*salary+())
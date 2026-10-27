First_Number=eval (input("Enter the first number:"))
Second_Number=eval(input("Enter the second number:"))
Third_Number=eval (input("Enter the third number:"))
Total_bill=First_Number+Second_Number+Third_Number
print("The total payable bill is :", Total_bill)
Person=eval(input("Enter the number of people among which you want the bill to be distributed"))
Each_Pay=Total_bill / Person
print(f"Total payable amount by everyone is : {Each_Pay:.3f}")
#code ends here

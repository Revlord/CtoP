#formula for simple interest is Total amount  = principle ( 1+ (rate*time))
#defining variables and using mathematical operators to perform the calculation and print the output
principle = int(input("Enter the principle: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Please enter the time to find the simple interest: "))
interest = (principle * (1 + (rate * time)))
print(f"Simple interest is: {interest:.2f}")

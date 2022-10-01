number = int(input("Enter the number: "))
reverse = 0
while number > 0:
    l = number % 10
    reverse = (reverse * 10) + l
    number = number//10
print("The reverse of the number is",  reverse)




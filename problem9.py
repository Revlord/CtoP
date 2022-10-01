number = int(input("Please enter the number of whose table you want to know: "))
x = int(input("Enter the number of tables you want to know (up until which table): "))
for y in range (1,x+1):
    print(f"{number} * {y} = {number * y}")

    


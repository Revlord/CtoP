#Program to find the greatest in 3 numbers
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
elif c > a and c > b:
    print("c is the greatest")



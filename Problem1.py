# a = float(input("Enter 2 numbers: "))
# b = float(input())
# c = a + b
# print(f"Your sum: {c:.2f}")
#the code above is a general code
#here sum of 2 numbers can be anything: intergers or decimals(floats). so assuming my domain is all the real numbers, I use :.2f to round off the output by 2 decimal places to make it look clean.
#I used f string so I can avoid type conversions and concatinate strings and integers all together.

#We have to write a program to calculate the sum of two numbers
#for this its best to define a function because we can simply use the function to get the sum in various other area of the code(if we have a large code)
#if we dont define a function we'll have to keep writing the code again and again.

def main():
    x = float(input("Enter 2 numbers: "))
    y =float(input())
    print(sum(x, y))
def sum(a , b):
    c = a + b
    return c
main()


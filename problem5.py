#problem to calculate the sum of 5 subjects and find their percentage
s1 = int(input("Enter marks of 5 subjects: "))
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
sum = (s1+s2+s3+s4+s5)
print("Sum:", sum)
total = int(input("What the total possible score?: "))
percentage = ((sum/total))*100
print(f"Percenatge = {percentage}%")
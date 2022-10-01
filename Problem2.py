#We have to calculate the area and circumference of the circle
#Im going to import a math module which includes the accurate value of pi 
import math
radius = int(input("Enter the radius: "))
area = (math.pi * (radius**2))
circumference = (2 * math.pi * radius)
print(f"Area of the circle is: {area:.2f} \nThe Circumference of the circle is: {circumference:.2f}" )






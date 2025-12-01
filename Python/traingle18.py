# Input three sides of a triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if it forms a valid triangle using the triangle inequality rule
if (a + b > c) and (a + c > b) and (b + c > a):
    # Now classify the type of triangle
    if a == b and b == c:
        print("Equilateral triangle")
    else:
        if a == b or b == c or a == c:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
else:
    print("Not a valid triangle")

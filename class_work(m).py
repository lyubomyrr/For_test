# 1.  Написати програму, яка обчислює площу прямокутника, трикутника та кола 
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

def rectangle(a,b):
    area_rectangle=a*b
    print("Area of rectangle is equal {}".format(area_rectangle))

def triangle(a,h):
    area_triangle=1/2*a*h
    print("Area of triangle is equal {}".format(area_triangle))

def circle(r):
    area_circle=3.14*r**2
    print("Area of circle is equal {}".format(area_circle))


s=input("Select the object whose area you want to count:\n1-rectangle\n2-triangle\n3-circle\n")


if s=='1':
    a=float(input("Enter the length of the side a= "))
    b=float(input("Enter the length of the side b= "))
    rectangle(a,b)

elif s=='2':
    a=float(input("Enter the length of the triangle side a="))
    h=float(input("Enter the height of the triangle h="))
    triangle(a,h)
elif s=='3':
    r=float(input("Enter the radius of the circle r="))
    circle(r)
else:
    print("Wrong number!")
# 2.  Написати функцію, яка обчислює суму цифр введеного числа.
def sum_numbers(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    return sum
n=int(input("Enter a number to calculate its sum of numbers: "))
print("The sum of the numbers {} entered is equal to {}".format(n,sum_numbers(n)))
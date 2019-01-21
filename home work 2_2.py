num = str(input("Enter 4 digit number:"))
multiplic = 1
for i in num:
  multiplic *= int(i)
print("Multiplication  {}!" .format(multiplic))
c = str(num)
print("Number in reverse  ", c[::-1])
s = str(num)
print("Sorted out number  ", sorted(s))
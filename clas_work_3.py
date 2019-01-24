# my_list = [int(input("Enter int {}: ".format(i+1))) for i in range(10)]
# print("  Max number is:", max(num_list))
# print("  Min number is:", min(num_list))
# print(my_list)
#or
# amount_of_numbers=int(input('Input amount of numbers\n'))
# list_of_numbers=[int(input('input number\n')) for i in range(amount_of_numbers)]
# print('max number in input list is {}\nmin number in input list is {}'. format(max(list_of_numbers),min(list_of_numbers)))
#Розширено
# nums = []
# k=int(input("Please enter the count of the elements of sequence: "))
# for i in range(k):
#      n = int(input("Please enter the element: "))
#      nums.append(n)
# print(nums)
# max = nums[0]
# min = nums[0]
# for i in range(k):
#     if nums[i] > max:
#         max = nums[i]
#     if nums[i] < min:
#         min = nums[i]
# #print("Maximum number = %d. Minimum number = %d." %(max, min))
# print("Maximum number = {}. Minimum number = {}.".format(max, min))

# for x in range(1, 11):
    # if x % 2==0:
        # print(X, 'is even ,ultiple of 2')
    # elif x % 3==0:
        # print (x, 'is an odd multiple of 3') 
    # else:
        # print(x, 'not divisible by 2 and 3')   

#number=int(input("Введіть ціле додатнє число:   "))
#factorial=1
#for i in range(1,number+1):
 #   factorial*=i  
#print("Факторіал числа",number,"дорівнює",factorial)

user_name = input('enter your login: ')
while  user_name!='first':
    print("eror:wrong")
    user_name=input('Username')
    print (user_name)
print ("welcome")
.



#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
def summation(num):
    sum_num=0
    for i in range(1,num+1):
        sum_num+=i
    return sum_num
# Author: Faith Elledge
# Github username: Elledgef
# Date: 4/13
# Description: This code can find the min and max in a set of integers
Num = int(input("How many integers would you like to enter?"))
print("Please Enter "+ str(Num)+ " integers")
minval = int(input())
#Enter zero so the code will stop and compile after desired number of integers are inputted
maxval = 0
#used a loop to run through each number
for i in range ( 0, Num-1):
    x= int(input())
    if x<minval:
       minval=x;
    if x>maxval:
          maxval =x;
#Print min and max from the set of numbers given
print("min:",minval)
print("max:",maxval)




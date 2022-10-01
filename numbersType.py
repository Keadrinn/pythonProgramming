"""
Programmer: Keadrin Allen
Program: numbersType
Program Version: 3.10.2
Created On: 9/26/2022 08:11:00
Last Modified: 9/30/2022 08:11:00

"""
print("Welcome to Mathmatical Operations")
print("1 Odd Numbers \n "
      "2 Even Numbers \n "
      "3 Prime Numbers \n "
      "4 Perfect Numbers \n "
      "5 Palindrome \n")
choice = int(input("Select an Operation by Entering a Number:\t"))
if choice == 1:
    print("Printing Odd numbers from the First 100 Natural numbers")
    for i in range(0,101):
        if (i%2 != 0):
            print(i,end=" ")
elif choice ==2:
    print("Printing Even numbers from the First 100 Natural numbers")
    for i in range(2,101):
        if (i%2 == 0):
            print(i,end=" ")

elif choice ==3:
    print("Printing Prime numbers from the First 100 Natural numbers")
    for i in range(1, 101): #iterating for numbers between 1 t0 101
        counter=0
        for k in range(2,int(i/2)+1):
            if i%k==0:
                counter = counter+1
        if counter == 0:
            print(i, end=" ")


elif choice ==4:
    print("Printing Perfect numbers from the First 100 Natural numbers")
    for n in range(1,101):
        sum =0
        for i in range (1,n):
            if n%i ==0:
                sum+= i
        if sum == n:
            print(n,end=" ")

elif choice == 5:
    print("Palindrome Numbers")
    number=int(input("Enter your number"))
    reverse=0
    originalNumber = number
    while number>0:
        remainder = int(number % 10)
        reverse = int(reverse*10+ remainder)
        number= int(number/10)
    if originalNumber == reverse:
        print(originalNumber, "is a Palindrome Number")
    else:
        print(originalNumber, "is not a Palindrome Number")
else:
    print("Invalid option")

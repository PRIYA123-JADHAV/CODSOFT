print(" 1 Addition")
print(" 2 Substraction")
print(" 3 Multiplication")
print(" 4 Division")

operation= int(input())

if operation == 1:
    num1= int (input("enter the 1st number: "))
    num2=int(input("enter the 2nd number:"))
    num3= num1+num2
    print("Addition is:" ,num3)

elif operation == 2:
    num1= int (input("enter the 1st number: "))
    num2=int(input("enter the 2nd number:"))
    num3= num1-num2
    print("Substration is:" ,num3)

elif operation == 3:
    num1= int (input("enter the 1st number: "))
    num2=int(input("enter the 2nd number:"))
    num3= num1*num2
    print("Multiplication  is:" ,num3)


elif operation == 4:
    num1= int (input("enter the 1st number: "))
    num2=int(input("enter the 2nd number:"))
    num3= num1/num2
    print("Division  is:" ,num3)
else:
    print("invalid entry")
    

    

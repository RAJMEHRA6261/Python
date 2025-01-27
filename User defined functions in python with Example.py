#Program to find Greatest of three numbers by user defined functions

# 1.Program to find Greatest of three numbers With No arguments and return type.

"""

def Greatest_three():
    print("Enter the three numbers:")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if(num1 > num2 and num1 > num3):
        print(f"The greatest value is {num1}")
    elif(num2 > num1 and num2 > num3):
        print(f"The greatest value is {num2}")
    else:
        print(f"The greatest value is {num3}")
        

print("The program Starts from here")
Greatest_three()

"""


# 2.Program to find Greatest of three numbers With arguments and No return type.

"""

def Greatest_three(num1,num2,num3):
    if(num1 > num2 and num1 > num3):
        print(f"The greatest value is {num1}")
    elif(num2 > num1 and num2 > num3):
        print(f"The greatest value is {num2}")
    else:
        print(f"The greatest value is {num3}")


print("The program Starts from here")   
print("Enter the three numbers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
Greatest_three(num1,num2,num3)
print("The program Ends here.")

"""


# 3.Program to find Greatest of three numbers With No arguments and return type.

"""

def Greatest_three():
    print("Enter the three numbers:")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    
    if(num1 > num2 and num1 > num3):
        print("The greatest value is:",end="")
        return num1
    elif(num2 > num1 and num2 > num3):
        print("The greatest value is:",end="")
        return num2
    else:
        print("The greatest value is:",end="")
        return num3

print("The program Starts from here")
result = Greatest_three()
print(result)
print("The program Ends here.")

"""


# 4.Program to find Greatest of three numbers With arguments and return type.

"""

def Greatest_three(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        print("The greatest value is:",end="")
        return num1
    elif(num2 > num1 and num2 > num3):
        print("The greatest value is:",end="")
        return num2
    else:
        print("The greatest value is:",end="")
        return num3

print("The program Starts from here:")   
print("Enter the three numbers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
result = Greatest_three(num1, num2, num3)
print(result)
print("The program Ends here.")

"""





    

#calculator

# #Functios
# #addition
def add(num1,num2):
    return num1+num2

#subtraction
def sub(num1,num2):
    return num1-num2

#multiplication
def mul(num1,num2):
    return num1*num2

#division
def div(num1,num2):
    return num1/num2

#input from user
num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))

#operation's
print("Select Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

select = int(input("Select a operation from 1,2,3,4:"))

if select == 1:
    print(num1, "+", num2,"=" , add(num1,num2))

elif select ==2:
    print(num1, "-", num2,"=" , sub(num1,num2))

elif select ==3:
    print(num1, "*", num2,"=" , mul(num1,num2))

elif select ==4:
    print(num1, "/", num2,"=" , div(num1,num2)) 

else:
    print("Invalid Input")               
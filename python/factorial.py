#using loop functions
num=int(input('enter the input:'))
fact=1
if num<0:
    print('Factorial does not exist for negetive number')
elif num==0:
    print('factorial of 0 is 1')
else:
    for i in range (1,num+1):
        fact=fact*i
    print('factorial of',num,'is',fact)
    
# using recursion

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)
    
    
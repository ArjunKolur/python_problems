import random
x=range(1,10)
print('4 non repeating numbers are',random.sample(x,4))

#genarate the randam string of ascii-lowercase
import random
import string

def Get_randomString(length):
    latter=string.ascii_lowercase
    reasult_latter=''.join(random.choice(latter) for i in range(length))
    print('random string of length',length,'is',reasult_latter)

Get_randomString(8)

#genarate the randam string of ascii-uppercase
import random
import string

def Get_randomString(length):
    latter=string.ascii_uppercase
    reasult_latter=''.join(random.choice(latter) for i in range(length))
    print('random string of length',length,'is',reasult_latter)

Get_randomString(8)

def Get_randomstring(length):
    result_string=''.join(random.choice(string.ascii_letters)for i in range(length))
    print('random laters of password:',result_string)

Get_randomstring(8)



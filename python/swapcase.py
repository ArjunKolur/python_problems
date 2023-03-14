x=int(input('enter the values1:'))
y=int(input('enter the values2:'))
temp=x
x=y
y=temp
print('the values of x aftyer fist swaping :{}'.format(x))
print('the values of y after swaping:{}'.format(y))

#witout using the temp variable

x=5
y=2
x,y=y,x
print('x=',x)
print('y=',y)



#program for take 3 digit input from user and print addition of its digits

a=int(input('Enter a 3 digit number'))
b=a//100
print(b)
c=a%100
d=c//10
print(d)
e=c%10
print(e)
z=b+e+d
print('Addition of the three digits is ',z)
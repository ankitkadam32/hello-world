#program for take 3 digit input from user and print reverse of its digits
a=int(input('Enter a three digit number'))

h=a//100
print(h)
t=a%100

b=t//10
print(b)

u=t%10
print(u)

print('Reverse of three digit number is',u,b,h)


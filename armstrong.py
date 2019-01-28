#Name;Ranveer Ghorpade 
#Div:P
'''Write a program to find whether the user entered number is a armstrong number'''
x=int(input('enter a number'))
x1=x//100
r1=x%100
x2=r1//10
r2=r1%10
z=(x1)**3+(x2)**3+(r2)**3
if x==z: 
   print('armstrong number')
else:
	print('not a armstrong number ')  


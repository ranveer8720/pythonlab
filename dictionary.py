#Name:Ranveer 
#Div:P

d={}
x=int(input('number of students'))
for i in range(x):
  print('profile of student ',i+1)
  n=input('name:')
  g=int(input('gr.number:'))
  b=input('branch:')
  d[g]=(n,b)
print(d)


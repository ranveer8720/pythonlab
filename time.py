#Nam:;Ranveer 
#Div:P'
x=int(input('time in seconds')) 
d1=x//86400
r1=x%86400
d2=r1//3600
r2=r1%3600 
d3=r2//60
r3=r2%60
print(x,' seconds equals to' ,d1,'days' ,d2,'hrs' ,d3,'minutes')
  

#Q1/write a method that remove any given character from a string
str1="fadhil_Mohammed"
print ("string="+str1)

str2= str1[:5] +str1[6:]  #removing char (l) using slice and concatenation
print ("string after removal=" +str2)

#Q2/write a program to find all prime numbers up to given range of numbers
x=int(input("lowest value= "))
y=int(input("upper value= "))
print ('prime number between ',x,
       'and',y,'is')
for val in range(x, y):   # loop through all the elements in the given range
  if val > 1:
    for i in range(2, val):  
      if (val % i) == 0:  # check for each number if it has any factor between 1 and itself
        break
    else:
      print(val, end=" ")


#Q3/write a function that count how many the given character repeated in a given string 

count = 0
string ="fundemental Engineering"
char ="e"
for i in string :
    if i==char:
        count+=1
print(count)

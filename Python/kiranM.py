#Simple If:
#1. Wap to print the square of a number only if it is even.
'''n=int(input("enter the value of n: "))
if n%2==0:
    print(n**2)'''
#2. Wap to check whether the character is vowel or not.
'''c=input("enter c character: ")
if c in 'aeiouAEIOU':
    print("vowel")'''
#3. Wap to print Ascii value of a character only if it is upper case.
'''s=input("enter the character: ")
if s.isupper():
    print(ord(s))'''
#4. Wap to print the cube of a number only if it is divisible by 9 or 6.
'''n=int(input("enter the n value"))
if n%9==0 or n%6==0:
    print(n**3)'''
#5. Wap to check whether the given integer is 3 Digit number.
'''n=int(input("enter the value n"))
if n>99 and n<1000:
    print("yes it is three digit number")'''
#6. Wap to check whether the last digit of a given number is 5.
'''n=int(input("enter the value of n "))
if n%10==5:
    print("yes it ends with 5")'''
#7. Wap to check whether the given data is float.
'''n=eval(input("enter n value "))
if type(n)==float:
    print("yes its float")
'''
#8. Wap to check whether the data is single value data.
'''n=eval(input("enter the n value : "))
if type(n) in (int,float,complex,bool):
    print("it is a single value datatype")'''
#9. Wap to check whether the given character is digit or not.
'''n=input("enter the n values")
if n>='0' and n<='9':
    print("digit ")'''
    
#10.Wap to check whether the given integer is multiple of 3
'''n=int(input("enter the number: "))
if n%3==0:
    print("yes , i am multiple of 3")'''

#if else
#11.Wap to check whether the data is mutable or not.
'''n=eval(input())
if type(n) in (list,str,set,dict):
    print("mutable")
else:
    print("not mutable")'''
    
#12.Wap to check whether the given character is digit or not.
'''n=input()
if n>='0' and n<='9':
    print("yes i am digit")
else:
    print("not digit")'''

#13.Wap to check whether the given character is special or not.
'''n=input()
if 'A'<=n>='Z' or 'a'<=n>='z' or '0'<=n>='9':
    print("it is not a special character")
else:
    print("it is  a special character")
'''
#14.Wap to check whether a list consists of middle value or not.
'''n=eval(input())
if (len(n))%2==0:
    print("dont have mid value")
else:
    print("have a middle value ")'''
#15.Wap to check whether the number is even or odd.
'''n=int(input())
if n%2==0:
    print("even")
else:
    print("odd ")'''
#16.Wap to check whether the given data is mutable or immutable.
'''n=eval(input())
if type(n) in (list,str,set,dict):
    print("mutable")
else:
    print("not mutable") '''   
#17.Wap to check whether 2 values are pointing to the same memory or not.
'''a=eval(input("enter the value of a"))
b=eval(input("enter the value of  b "))
if id(a)==id(b):
    print("same address")
else:
    print("different address")'''
    
#18.Consider a tuple of length 2 and check whether the tuple is homogenous or not.
'''n=eval(input())
if type(n[0])==type(n[1]):
    print("homogenous")
else:
    print("not homogenous")'''
#19.Wap to check whether the string is palindrome or not.
'''str=input()
rstr=str[::-1]
if str==rstr:
    print("palindrome")
else:
    print("not a palindrome")'''
    
#20.Wap to check whether the number is positive or negative.
'''n=int(input())
if n>0:
    print("positive")
else:
    print("negative")'''

#---------------------------------
#ELIF->all done once 

#21. Wap to check whether the char is uppercase, lowercase, digit or special char. 
ch = input()
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

#22. Wap to check whether the given integer is single digit or two digits or three  
#digits or more than three digits. 
n = int(input())
l = len(str(abs(n)))
if l == 1:
    print("Single digit")
elif l == 2:
    print("Two digits")
elif l == 3:
    print("Three digits")
else:
    print("More than three digits")

#23.Wap to check the given points are lying in which quadrant. 
x = int(input())
y = int(input())
if x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x>0 and y<0:
    print("4th Quadrant")
else:
    print("On Axis")

#24. Wap to find the greatest of 3 numbers. 
a=int(input()); b=int(input()); c=int(input())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

#25. Wap to find the smallest of 3 numbers. 
a=int(input()); b=int(input()); c=int(input())
if a<b and a<c:
    print(a)
elif b<c:
    print(b)
else:
    print(c)

#26.Wap to check the relation between two integer numbers. 
a=int(input()); b=int(input())
if a>b:
    print("a is greater")
elif a<b:
    print("b is greater")
else:
    print("Both are equal")

#27. Consider a character input if it is uppercase convert it into lowercase, if it is         
#lowercase convert it into uppercase, if it is digit print the reminder when  it is 
#divided by 3 else if it is special character print it’s ASCII value. 
ch=input()
if ch.isupper():
    print(ch.lower())
elif ch.islower():
    print(ch.upper())
elif ch.isdigit():
    print(int(ch)%3)
else:
    print(ord(ch))

#28.Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the    
#given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of  
#both 3 and 5.
n=int(input())
if n%3==0 and n%5==0:
    print("Fizzbuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")

#---------------------------------
#nested if

#29.Wap to login into the Instagram with valid username and password.(enter password only if the user name is valid) 
user=input()
if user=="admin":
    pwd=input()
    if pwd=="1234":
        print("Login Success")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

#30. Wap to print the middle value of a list only if it is string. 
L=[1,"hello",3]
mid=L[len(L)//2]
if type(mid)==str:
    print(mid)

#31.Wap to check whether the character is vowel or consonant. 
ch=input()
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

#32.Wap to find the greatest of 4 numbers.
a=int(input()); b=int(input()); c=int(input()); d=int(input())
max=a
if b>max:
    max=b
if c>max:
    max=c
if d>max:
    max=d
print(max)
#32.Wap to find the greatest of 4 numbers.
'''n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
if n1>n2 and n1>n3 and n1>n4 :
    print( "n1 is greater")
else :
    if n2>n3 and n2>n4:
        print("n2 is greater ")
    elif n3>n4:
        print("n3 is greater")
    else:
        print("n4 is greater")'''
'''elif n2>n3 and n2>n4:
    print("n2 is greater ")
elif n3>n4:
    print("n3 is greater ")
else:
    print("n4 is greater")'''
        
#33. Wap to print the value as it is only if the length of the value is even. 
#34.Wap to print the last value of a list only if it is palindrome string starting with vowel. 
'''n=eval(input())
if type(n[-1])==str:
    h=n[-1]
    h[::-1]
    if h==n:
        if n in 'aeiouAEIOU':
            print(n[-1])
        else:
            print("not starting with vowel")
    else:
        print("it is not a pallindrome")
else:
    print("last value is not a string")'''
#35.Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value. 
'''n=input()
if (n[0] not in 'aeiouAEIOU') and (n[-1] not in 'aeiouAEIOU') and (len(n)%2!=0):
    print(n[::-1])
else:
    print("does not satisfy condition")'''
#36.Wap to find the second greatest of 4 values.
'''n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
if n1>n2 and n1>n3 and n1>n4 :
    if n2>n3 and n2>n4:
        print( "n2 is second greater")
    elif n3>n2 and n3>n4:
        print( "n3 is second greater")
    else:
        print( "n4 is second greater")
elif n2>n3 and n2>n4:
    if n3>n4 and n3>n1:
        print( "n3 is second greater")
    elif n1>n4 and n1>n2:
        print("n1 is second greater")
    else:
        print("n4 is second greater")
            
elif n3>n4:
    if n4>n1 and n4>n2:
        print( "n4 is second greater")
    elif n2>n1 and n2>n4 :
        print("n2 is second greater")
    else :
        print("n1 is second greater")
else:
    if n3>n1 and n3>n2:
        print( "n3 is second greater")
    elif n2>n3 and n2>n1 :
        print("n2 is second greater")
    else:
        print("n1 is second greater")'''
#37.Wap to find the smallest of 4 numbers. 
#38. Write a program to print middle Character of the given string only if it is upper Case Character.
'''n=input()
if (len(n))%2!=0:
    mid=int(float((len(n))/2)-0.5)
    if n[mid].isupper():
        print(n[mid])'''

#WHILE
#39.Wap to print python for 5 times.
'''i=1
while i<=5:
    print("python")
    i+=1'''
#40.Wap to print n natural numbers.
'''n=int(input())
i=1
while i < n:
    print(i)
    i+=1'''
#41.Wap to print multiplication table for n.
'''n=int(input())
i=1
while i<=10:
    print(n ,'*', i,'=',n*i)
    i+=1'''
#42.Wap to find the sum of n natural numbers.
'''n=int(input())
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(sum)'''
#43. Wap to find the product of n natural numbers or factorial of a number.
'''n=int(input("enter the value to get factorial"))
product=1
i=0
while i<=n:
    product=product*i
    i+=1
print(product)'''
#44.Wap to print all the characters of a string.
'''string=input()
i=0
while i<len(string):
    print(string[i])
    i+=1'''
#45.Wap to print all the characters present at even index of a string.
'''string=input()
i=0
while i<len(string):
    if i%2==0:
        print(string[i])
    i+=1'''
#46.Wap to extract all the lowercase characters present in a string.
'''string=input()
i=0
while i<len(string):
    if string[i].islower():
        print(string[i])
    i+=1'''
#47.Wap to extract all the vowels present in a string.
'''string=input()
i=0
while i<len(string):
    if string[i] in 'aeiouAEIOU':
        print(string[i])
    i+=1'''
#48.Wap to print factors of a integer number.
'''n=int(input())
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1'''
#49.Wap to toggle a string.
'''n=input()
i=0
while i<len(n):
    if n[i].isupper():
        print(chr(ord(n[i])+32))
    elif n[i].islower():
        print(chr(ord(n[i])-32))
    i+=1'''

#50.Wap to reverse the given number.
'''num=int(input())
sum=0
i=0
while num!=0:
    last=num%10
    sum=(sum*10)+last
    num//=10
    i+=1
print(sum)'''
    
#51.Wap to find the sum of individual digits of a number.
'''num=int(input())
sum=0
i=0
while num!=0:
    last=num%10
    sum=sum+last
    num//=10
    i+=1
print(sum)'''
#52. Wap to check whether the number is perfect or not.
'''num=int(input())
summ=0
i=1
while i<num:
    if num%i==0:
        summ=summ+i
    i+=1
if summ==num:
    print("perfect")
else:
    print("not perfect")'''
#53.Wap to login to phonepe by entering correct otp.
'''otp=1234
while True:
    n=int(input("enter the otp"))
    if otp==n:
        print("successfull login")
        break
    else :
        print("try again")'''
#54.Wap to run infinite loop until user enters the correct password.
'''password=1234
while True:
    n=int(input("enter the password"))
    if password==n:
        print("successfull login")
        break
    else :
        print("try again")'''
#55.Wap to extaract all the even integers present in a tuple at odd index.
'''n=eval(input())
i=0
while i<len(n):
    if n[i]%2==0 and i%2!=0:
        print(n[i])
    i+=1'''
#56.Wap to remove duplicates from a list without converting into set.
'''n=eval(input())
h=[]
i=0
while i<len(n):
    if n[i] not in h:
        h+=[n[i]]
    i+=1
print(h)'''
#57.Wap to find the sum of all the odd numbers between the given range.
'''n=int(input())
i=0
sum=0
while i<=n:
    if i%2!=0:
        sum+=i
    i+=1
print(sum)'''
#58.Wap to find the greatest number in a given list of integers.
'''n=eval(input())
i=1
max=n[0]
while i<len(n):
    if n[i]>max:
        max=n[i]
    i+=1
print(max)'''
#59.Wap to find the sum of cube of a number in a string.
'''n=input()
i=0
sum=0
while i<len(n):
    if n[i].isdigit():
        h=int(n[i])
        sum=(h**3)+sum
    i+=1
print(sum)'''
#60.Wap to check whether the number is Armstrong or not.
#61.Wap to get the following output. 
#A=’10011100’   B=’00110101’    out=4(count of positions having same values)
'''A='10011100'
B='00110101'
i=0
count=0
while i<len(A):
    if A[i]==B[i]:
        count+=1
    i+=1
print(count)'''
# 62.Wap to check the given number is prime or not.
'''n=int(input())
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("prime number")
else:
    print("not prime")'''
#63.Wap  to check whether the number is palindrome or not.
'''num=int(input())
temp=num
sum=0
i=0
while num!=0:
    last=num%10
    sum=(sum*10)+last
    num//=10
    i+=1
if sum==temp:
    print("palindrome")
else:
    print("not palindrome")
    '''
#64.Wap to find the HCF of two numbers.
'''
n1=int(input())
n2=int(input())
HCF=1
for i in range(min(n1,n2), 0,-1):
    if n1%i==0 and n2%i==0:
        HCF=i
        break
print(HCF)
'''
#65.Wap to convert binary to decinaml.
'''bi=input()
sum=0
i=(len(bi)-1)
power=0
while i>=0:
    if bi[i]=='1':
        n=2**power
        sum+=n
    power+=1
    i-=1
print(sum)'''
    
#66. Wap to convert decimal to binary.
'''n=int(input())
bi=''
while n!=0:
        last=n%2
        bi=str(last)+bi
        n//=2
print(bi)'''
# 67.Wap to count the number of words in a string.
'''string=input()
string2=string.split()
h=len(string2)
print(h)'''
# 68.Wap to guess the number.
'''num=123
while True:
    user=int(input())
    if user==num:
        print("correct")
        break
    else:
        print("try again")'''
#69.Wap to find the common elements in two sets
'''set1={1,2,3,4,5}
set2={2,3,78,9}
list1=list(set1)
i=0
while i<len(list1):
    if list1[i] in set2:
        print(list1[i])
    i+=1'''
#70.Wap to find the product of all the digits present in a number.
'''num=int(input())
prod=1
i=0
while num!=0:
    last=num%10
    prod=prod*last
    num//=10
print(prod)'''
#for loop
#71.Wap to print all the integers present in a list.
'''L=[1,2,3,4]
for i in L:
    if type(i) == int:
        print(i)'''
#72.Wap to find the length of homogenous tuple without len().
'''t=(1,2,3,4)
count=0
for i in t:
    count+=1
print(count)'''
#73.Wap to extract all the even numbers present in a list.
'''L=[1,2,3,4,5,6]
for i in L:
    if i%2==0:
        print(i)'''
#74.Wap to remove duplicates from list
L=[1,2,2,3,4,4]
res=[]
for i in L:
    if i not in res:
        res.append(i)
print(res)
#75.Wap to reverse a string without using slicing.
s="hello"
rev=""
for i in s:
    rev=i+rev
print(rev)
#76.wap to extract all the lowercase characters in a string only if the ascii value is  even.
s="abcde"
for i in s:
    if i.islower() and ord(i)%2==0:
        print(i)
#77.Wap to check whether the last digit of an integer is even or not.
n=1234
if (n%10)%2==0:
    print("Even")
else:
    print("not even ")
#78.Wap to extract all the key value pairs from the dictionary only if the keys are of   string datatype and values are integers.
d={"a":1,2:"b","c":3}
for k,v in d.items():
    if type(k)==str and type(v)==int:
        print(k,v)
#79.Wap to extract key value pairs from the dictionary only if both keys and values are exactly same. 
d={1:1,"a":"a",2:"b"}
for k,v in d.items():
    if k==v:
        print(k,v)
#80.Wap to get the following output using len function. S=’power star’ Out={‘power’:5,’star’:4} 
s="power star"
res={}
for i in s.split():
    res[i]=len(i)
print(res)
#81.Wap to get the following output. S=’power star’ Out={‘power’:’rewop’,’star’:’rats’}
s="power star"
res={}
for i in s.split():
    rev=""
    for j in i:
        rev=j+rev
    res[i]=rev
print(res)
#82. wap to extract all the non default  values from a list.
L=[0,1,2,"",3]
for i in L:
    if i:
        print(i)
#83.Wap to check whether the list is homogenous or not.
L=[1,2,3]
t=type(L[0])
flag=True
for i in L:
    if type(i)!=t:
        flag=False
print(flag)
#84.Wap to replace the space by * present in a string
s="hello world"
res=""
for i in s:
    if i==" ":
        res+="*"
    else:
        res+=i
print(res)
#85.Wap to count the number of occurrence of a specified character.
s="hello"
ch="l"
count=0
for i in s:
    if i==ch:
        count+=1
print(count)
#86. Wap to get the following output. S=’always keep smiling’ Out-‘syawla peek gnilims’
s="always keep smiling"
res=""
for w in s.split():
    temp=""
    for c in w:
        temp=c+temp
    res+=temp+" "
print(res)
#87. Wap to get the following output. In=’push maadi kushi padi’ Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’} 
s="push maadi kushi padi"
res={}
for w in s.split():
    res[w]=w[0]+w[-1]
print(res)
#88.Wap to toggle a string.
s="AbC"
res=""
for i in s:
    if i.islower():
        res+=i.upper()
    else:
        res+=i.lower()
print(res)
#89.Wap extract upper, lower, digit and special characters present in a string to different. output variable 
s="Ab1@c"
u=l=d=sp=""
for i in s:
    if i.isupper(): u+=i
    elif i.islower(): l+=i
    elif i.isdigit(): d+=i
    else: sp+=i
print(u,l,d,sp)
#90. Wap to get the following output. S=’hai hello ‘ Out={‘hai’:’ai’,’hello:’eo’} 
s="hai hello"
res={}
for w in s.split():
    temp=""
    for i in w:
        if i not in "aeiou":
            temp+=i
    res[w]=temp
print(res)
#91. Wap to get the following output. S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’] Out=[‘com’,’py’,’html’,’org’] 
L=['a.com','b.py','c.html']
res=[]
for i in L:
    res.append(i.split(".")[1])
print(res)
#92. Wap to get the following output. S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’] Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’], ’org’:[‘www’]} 
L=['a.com','b.py','c.html']
res={}
for i in L:
    name,ext=i.split(".")
    if ext not in res:
        res[ext]=[]
    res[ext].append(name)
print(res)
#93.Wap to get the following output. L=[‘hai’,34,3.4,’hello’,90,’byebye’] Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’} 
L=['hai',34,'hello']
res={}
for i in L:
    if type(i)==str:
        res[i]=i[0]+i[-1]
print(res)
#94.wap to get the following output. In=’hello’ Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’} 
s="hello"
res={}
for i in range(len(s)):
    res[i]=s[i]
print(res)
#95.Wap to extract all the string values present in list only if the string is palindrome. 
L=["madam","hi","level"]
for i in L:
    if i==i[::-1]:
        print(i)
#96.Wap to return the positions of vowels present in the given string.
s="hello"
for i in range(len(s)):
    if s[i] in "aeiou":
        print(i)
#97.Wap to check whether the given collection is having nested collection or not.
L=[1,[2,3],4]
for i in L:
    if type(i) in [list,tuple,set,dict]:
        print("Nested")
#98.Wap to count the number of words in a string.
s="hello world"
print(len(s.split()))
#99.Wap to check whether the number is neon number or not. N=9→9**2=81→8+1=9
n=9
sq=n*n
sum=0
for i in str(sq):
    sum+=int(i)
print(sum==n)
#100.Wap to find the longest word in a string.
s="hello world python"
maxw=""
for w in s.split():
    if len(w)>len(maxw):
        maxw=w
print(maxw)
#101.Wap to replace the special character present in a string by space.
s="a@b#c"
res=""
for i in s:
    if not i.isalnum():
        res+=" "
    else:
        res+=i
print(res)
#102.wap to print the square of all the integers present in a list.
L=[1,2,3]
for i in L:
    print(i*i)
#103.Wap to extract all the odd number present at even index from a list.
L=[1,2,3,4,5]
for i in range(len(L)):
    if i%2==0 and L[i]%2!=0:
        print(L[i])
#104.Wap to extract all the mutable values present in a tuple.
t=(1,[2],{3:4})
for i in t:
    if type(i) in [list,dict,set]:
        print(i)
#105.Wap to get the following output. In=’10100011231’ Out=’010111000’    ( 0→1 and 1→0 if it is other than 0 &1 ignore) 
s="10100011231"
res=""
for i in s:
    if i=="0": res+="1"
    elif i=="1": res+="0"
print(res)
#106.Wap to get the following output. In=’abacbaacc’ Out={‘a’:4,’b’:2,’c’:3} 
s="abacbaacc"
res={}
for i in s:
    res[i]=res.get(i,0)+1
print(res)
#107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype. 
d={True:1,False:2,1:3}
for k,v in d.items():
    if type(k)==bool:
        print(k,v)
#108.Wap to get the following output. In=’127342’ Out=’242173’  (extract even and odd digits separately and concatenate both) 
s="127342"
even=odd=""
for i in s:
    if int(i)%2==0:
        even+=i
    else:
        odd+=i
print(even+odd)
#109.Wap to checek whether the string is having only lowercase or not using continue. 
s="hello"
flag=True
for i in s:
    if not i.islower():
        flag=False
        continue
print(flag)
#110.Wap to find the sum  square of individual digits of a string. 
s="123"
sum=0
for i in s:
    sum+=int(i)**2
print(sum)

#nested for loop
#111. Wap to get the following output. without length function. 
#S=’power star’ 
#Out={‘power’:5,’star’:4} 

s="power star"
res={}
for w in s.split():
    count=0
    for i in w:
        count+=1
    res[w]=count
print(res)


#112. Wap to get the following output. 
#S=’power star’ 
#Out={‘power’:2,’star’:1}   (no of vowels is key) 

s="power star"
res={}
for w in s.split():
    count=0
    for i in w:
        for v in "aeiou":
            if i==v:
                count+=1
    res[w]=count
print(res)


#113. Wap to get the following output. 
#S=’kabab is love’ 
#Out={‘kabab’:[‘babak’,2,’kbb’],’is’:[‘si’,1,’i’],’love’:[‘evol’,2,’lv’]} 

s="kabab is love"
res={}
for w in s.split():
    rev=""
    vowel=0
    even=""
    for i in range(len(w)):
        rev=w[i]+rev
        for v in "aeiou":
            if w[i]==v:
                vowel+=1
        if i%2==0:
            even+=w[i]
    res[w]=[rev,vowel,even]
print(res)


#114. Wap to get the following output. 
#S=’kabab is love’ 
#Out={‘kb’:(‘kbb’,3,’bbk’),’is’:(‘s’,1,’s’),’le’:(‘lv’,2,’vl’)} 

s="kabab is love"
res={}
for w in s.split():
    key=w[0]+w[-1]
    cons=""
    for i in w:
        flag=True
        for v in "aeiou":
            if i==v:
                flag=False
        if flag:
            cons+=i
    rev=""
    for i in cons:
        rev=i+rev
    res[key]=(cons,len(cons),rev)
print(res)


#115.Wap to get the following output. 
#In=[100,200,35,40,60] 
#Out=[335,235,400,395,375] (total sum-value) 

L=[100,200,35,40,60]
total=0
for i in L:
    total+=i

res=[]
for i in L:
    res.append(total-i)
print(res)


#116. Wap to get the following output. 
#In=’bacbcaabbaa’ 
#Out=’b4a5c2’ 

s="bacbcaabbaa"
res=""
visited=""
for i in s:
    if i not in visited:
        count=0
        for j in s:
            if i==j:
                count+=1
        res+=i+str(count)
        visited+=i
print(res)


#117. Wap to get the following output 
#In=[100,200,50,400,300] 
#N=300 
#Out=[[100,200],[300]] 

L=[100,200,50,400,300]
N=300
res=[]
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]+L[j]==N:
            res.append([L[i],L[j]])
for i in L:
    if i==N:
        res.append([i])
print(res)


#118.Wap to check whether the number is strong or not. 

n=145
temp=n
sum=0
for i in str(n):
    fact=1
    for j in range(1,int(i)+1):
        fact*=j
    sum+=fact
print(sum==temp)


#119.Wap to get the following output. 
#In={10:’star’,20:’bye’,30:’moon’,40:’apple’} 
#Out={10:’a’,20:’e’,30:’oo’,40:’ae’} 

d={10:'star',20:'bye',30:'moon',40:'apple'}
res={}
for k,v in d.items():
    temp=""
    for i in v:
        for j in "aeiou":
            if i==j:
                temp+=i
    res[k]=temp
print(res)


#120. Wap to get the following output. 
#In=[‘hello’,227,3.4,’last’,189,34] 
#Out=[722,981,43]

L=['hello',227,3.4,'last',189,34]
res=[]
for i in L:
    if type(i)==int:
        rev=""
        for j in str(i):
            rev=j+rev
        res.append(int(rev))
print(res)

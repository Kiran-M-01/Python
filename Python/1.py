
#29
# def login():
#     inst = {"username" : "tejas" , "password" : "0001"}
# # user_name = "tejas"
# # password = "0001"
#     un = input("enter username: ")
#     if un == inst["username"] :
#         pw = input("enter password : ")
#         if pw == inst["password"] :
#             print(" welcome to Instagram ")
#         else:
#             print("wrong Password")
#             login()
#     else:
#         print("wrong Username")
#         login()

# login()
#02
# val = input("enter a value :")

# if len(val) % 2 == 0:
#     print(val)
# else:
#     print("value is not even")
           
#34
# str1 = list(input("enter a value : "))
# str2 = str1[::-1]
# first = str1[0]
# last = len(str1) - 1
# if str1 == str2:
#     if first in "aeiouAEIOU":
#         print(str1[last])
#     else:
#         print("not starting with Vowel")
# else:
#     print("not a Palindrome")

# 35
# str1 = input("enter a value : ")
# str2 = str1[::-1]
# first = str1[0]
# last = str1[len(str1) - 1]
# # mid = str1[len(str1) // 2]

# if first in "aeiouAEIOU":
#     if last not in "aeiouAEIOU" :
#         if len(str1) % 2 != 0:
#             print(str2)
#         else:
#             print("do not contain middle value")
#     else:
#         print("not ending with consonent")
# else:
#     print("not starting with Vowel")

# GREATEST OF 4 NUMBERS

# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# c = int(input("enter third number : "))
# d = int(input("enter fourth number : "))

# if a > b:
#     if a > c:
#         if a > d:
#             print(a,"is grateest")
#         else:
#             print(d,"is gratest")
#     else:
#         if c > d:
#             print(c,"is grateest")
#         else:
#             print(d,'is greatest')
# else:
#     if b > c:
#         if b > d:
#             print(b,"is greatest")
#         else:
#             print(d,'is greatest')
#     else:
#         if c > d:
#             print(c,"is greatest")
#         else:
#             print(d,"is greatest")


# SAMLLEST OF 4 NUMBERS
# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# c = int(input("enter third number : "))
# d = int(input("enter fourth number : "))

# if a == b == c == d :
#     print(" all are equal ")
# else:
#     if a < b:
#         if a < c:
#             if a < d:
#                 print(a,"is smallest")
#             else:
#                 print(d)
#         else:
#             if c < d :
#                 print(c)
#             else:
#                 print(d)
#     else:
#         if b < c:
#             if b < d:
#                 print(b)
#             else:
#                 print(d)
#         else:
#             if c < d:
#                 print(c)
#             else:
#                 print(d)

# 46  EXTRACT LOWERCASE
# str = input("enter a string : ")
# i = 0
# while i < len(str):
#     if 'a' <= str[i] <= 'z':
#         print(str[i])
#     i += 1

#EXTRACT VOWEL
# str = input("enter a string : ")
# i = 0
# while i < len(str):
#     if str[i] in 'aeiouAEIOU':
#         print(str[i])
#     i += 1

# s= 'royal challengers bengaluru'
# out = ' '
# i = 0
# while i < len(s):
#     if s[i] == ' ':
#         out += s[i]+'*'
#     else:
#         out += s[i]
#     i += 1
# print(out)

# l = [12,3,4,5,6,7,8,9,44]
# odd = []
# even = []
# for i in l:
#     if i % 2 == 0 and i not in even:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# s = 'aababcabca'
# count1 = 0
# count2 = 0
# count3 = 0
# for i in range(len(s)):
#     if s[i] not in s:
#         count1.append(s[i])
        
#     elif s[i] in count1:
#         count += 1
#     elif s[i] not in count1;
#         co
        
# str = 'hello'
# for s in str:
#     if  not ('a'<= s <= 'z'):
#         print(" upper case is there ")
#         break
# else:
#     print('lowercase')

# s1 = input('enter a string : ')
# ch = 's'
# for i in range(len(s1)):
#     if s1[i] == ch:
#         print('foun at index : ' ,i)
#         break
# else: 
#     print("not found ")

# LIST IS HOMOGENEOUS OR NOT
# l = eval(input("enter a List : "))
# T = type(l[0])
# for i in l:
#     if type(i) != T:
#         print("not homogeneous ",i)
#         break
# else:    
#     print("homogeneous ",l)    

# ENTER CORRECT PASSWORD
# import time
# pwd = "123"
# c = 0
# while True:
#     user_pwd = input("Enter password : ")
#     if user_pwd == pwd:
#         print("correct ")
#         break
#     else :
#         c += 1
#         print("wrong")
#         if c == 5:
#             print("enterd wrong password multiple times, try after 10 seconds")
#             time.sleep(10)
#             c = 0

#  CONTINUE
# for i in range(15,1,-1):
#     print(i, end = " ")
#     print(i + 5)
#     continue

# s = 'ababacbcbaaabbbaba'
# s1 ='bacacacabccababacc'
# i = 0
# count = 0
# if len(s) != len(s1):
#     print('both strings have didfferent length')
# else:
#     while i < len(s):
#         if s[i] != s1[i]:
#             i += 1
#             continue
#         else:
#             count += 1
#             i += 1
#     print(count)

# GROOMING
# li = [50,100,200,50]
# amt = 300
# res = set()
# i = 0
# while i < len(li):
#     diff =  amt - li[i]
#     if diff in res:
#         print(li[i],diff)
#     else:
#         res.add(li[i])
#     i += 1

# NESTED LOOP
# s = input("enter a string : ")
# out = {}
# for i in s.split():
#     l = 0
#     for j in i:
#         l+=1
#     out[i[::-1]] = l
# print(out)

# s = "hello Everyone How"
# out = {}
# for i in s.split():
#     con = ''
#     for j in i:
#         if j not in "AEIOUaeiou":
#             con += j
#     out[i[0]+i[-1]] = [con,len(con)]
            
# print(out)   

# inp = [100,200,90,80,300,10,20]

# out = []
# for i in inp:
#     summ = 0
#     for j in inp:
#         summ += j    
#     out.append(summ - i)
# print(out)

# WRONG CODE
# l = [90000,80000,10000,120000,25000]
# n = input("enter ")
# s = 0
# for i in range(len(l)):
#     if l[i] < l[i + 1]:
#         print(l[i])
#     else:
#         print(l[i + 1])
# if n == '0':
#     print(s)
# elif n == '1':
#     print(s[::-1])
# else:
#     print(l)

l = ['hello',745,79.5,63,119,'bye']
out = []
for i in l:
    if type(i) == int:
        rev = 0
        while i!=0:
            a = i % 10
            rev = (rev*10) + a
            i // 10
        out.append(rev)
    else:
        out.append(i)
print(out)

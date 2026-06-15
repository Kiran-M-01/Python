# FILE HANDLING

# -------WRITE ----------- 
# f = open("sam.txt", 'w')
# f.write('hello everyone')   # for writing single line
# f.close()

# f = open("sam.txt", 'w')
# f.writelines('hello everyone \nhow are you all \nI am good\n')   #for writing multiple line
# f.close()

# --------READ----
# f = open("sam.txt", 'r')
# data = f.read()      # COMPLETE FILE
# print(data)
# f.close()

# f = open("sam.txt", 'r')
# data = f.readline()  # ONE LINE AT A TIME
# print(data)
# f.close()

# f = open("sam.txt", 'r')
# data = f.readlines()  # IN THE FORM OF LIST
# print(data)
# f.close()

# ----APPEND----
# f = open("sam.txt", 'a')
# f.write('today is 13th jun')
# f.close()

# f = open("sam.txt", 'a+')
# f.seek(5)
# data = f.read()
# print(f.tell())   
# print(data)
# f.close()

# --------------------------------------------------------------------------------

# f = open("sam.txt", 'w')
# f.write('hi\n')
# f.writelines('poorvaj \nbharath \nkushal \nkiran\n')   #for writing multiple line
# f.close()

f = open("sam.txt", 'r')
data = f.read()
print(data)
f.close()
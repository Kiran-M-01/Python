# FILE HANDLING

# -------WRITE ----------- 
# f = open("sam.txt", 'w')
# f.write('hello everyone')
# f.close()

f = open("sam.txt", 'w')
f.writelines('good morning everyone \nhow are you \nI am fine\n')
f.close()

# --------READ----
# f = open("sam.txt", 'r')
# data = f.read()      # COMPLETE FILE
# print(data)
# f.close()

# f = open("sam.txt", 'r')
# data = f.readline()  # FIRST LINE
# print(data)
# f.close()

# f = open("sam.txt", 'r')
# data = f.readlines()  # IN THE FORM OF LIST
# print(data)
# f.close()

# ----APPEND----
f = open("sam.txt", 'a')
f.write('today is 12th jun')
f.close()

f = open("sam.txt", 'a+')
f.seek(5)
data = f.read()
print(f.tell())   
print(data)
f.close()



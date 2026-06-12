# FILE HANDLING
# WRITE 
# f = open("sam.txt", 'w')
# f.write('hello everyone')
# f.close()

# f = open("sam.txt", 'w')
# f.writelines('good morning everyone \nhow are you \nI am fine')
# f.close()

# READ
# f = open("sam.txt", 'r')
# data = f.read()
# print(data)
# f.close()

f = open("sam.txt", 'r')
data = f.read()
print(data)
f.close()
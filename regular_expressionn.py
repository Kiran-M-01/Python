import re
# s = 'sangamesh is working in google his dob id 13-6-2004 and his contact number is 9876543219 and email is sang123@gmail.com'

# # pat = r'[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{4}'

# # pat = r'[6-9][0-9]{9}'
# pat = r'\w*\@\w*\.?\w*'
# data = re.findall(pat,s)
# print(data)

s = 'this is the last class of python'
# result = re.match('this',s)
# print(result.span())
# print(result.start())
# print(result.end())


s = re.sub('class','java',s,count=1)
print(s)

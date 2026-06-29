import re
s = 'sangamesh is working in google his dob id 13-6-2004 and his contact number is 9876543219 and email is sang@gmail.com'

# pat = r'[0-9]{1,2}\-[0-9]{1,2}\-[0-9]{4}'

# pat = r'[6-9][0-9]{9}'
pat = r'\d*\@\w*\.?\w*'
data = re.findall(pat,s)
print(data)
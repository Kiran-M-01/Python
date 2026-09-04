class school:
    Sname = 'st.ritas primary school'
    loc = 'Mysuru'
    principal = 'Rita'
    def __init__(self,name,rollno,age,addr):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.addr = addr

s1 = school('Tejas',101,21,'Mysuru')
s2 = school('Rahul',102,22,'K.R Nagar')
s3 = school('Sanjay',103,23,'Blr')
print(s2.addr)
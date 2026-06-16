import csv
# CREATING / WRITING CSV FILE
# f = open("file.csv",'w')
# a = csv.writer(f)
# a.writerow(['name',"age","ph_no",'marks'])
# a.writerows([['darshan',"22","998877",'100'],['harsha',"21","998866",'99'],['sang',"23","998855",'98'],])
# f.close()

# READING CSV FILE
f = open("file.csv",'r')
data = csv.reader(f)
# print(list(data))
print([i for i in data if i!= []])
f.close()
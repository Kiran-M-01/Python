import csv
f = open("file.csv",'w')
a = csv.writer(f)
a.writerow(['name',"age","ph_no",'marks'])
a.writerows([['darshan',"22","998877",'100'],['harsha',"21","998866",'99'],['sang',"23","998855",'98'],])
f.close()
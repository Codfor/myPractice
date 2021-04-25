# import csv
# 
# with open('Me_FAB.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
# 
#     for line in csv_reader:
#         print(line)

ofile = open('Me_FAB.txt')

rfile = ofile.read()

print(rfile)


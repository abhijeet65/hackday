import csv
import matplotlib.pyplot as plt
import operator
x = []
y = []

with open("jeans.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    sortedlist = sorted(csv_reader, key=operator.itemgetter(3),reverse=True)
    for row in sortedlist:
    	if(line_count<=11 and line_count>0):
    		print(row[0]+ " "+row[1] +" "+ row[2] +" "+row[3])
    	line_count += 1
        		


  
'''    for row in csv_reader:
        if line_count == 0:
            print('Column names are {", ".join(row)}')
            line_count += 1
        else:
            if (line_count <= 10) :
            	#print(row[0]+ " "+row[1] +" "+ row[2] +" "+row[3])
            line_count += 1
            x.append((row[2]))
            y.append((row[3]))
    print(a)
'''    
    

    
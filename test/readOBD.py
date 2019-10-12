import time
import os
import csv

#delete files in directory
mydir = 'test_data/'
filelist = [ f for f in os.listdir(mydir) if f.endswith(".csv") ]
for f in filelist:
    os.remove(os.path.join(mydir, f))

#write dummy files
x = 1
while True:
    time.sleep(5)
    l = [x for x in range(2)]
    with open(mydir+'file'+str(x)+'.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerow(l)
    x += 1
    n_files = len(os.listdir(mydir))
    print(f'number of files: {n_files}')

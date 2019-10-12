import pandas as pd 
import time
import os

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
    pd.Series(l).to_csv('test_data/file' + str(x) + '.csv', header=True)
    x += 1
    n_files = len(os.listdir(mydir))
    print(f'number of files {n_files}')

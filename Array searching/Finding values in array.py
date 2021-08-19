import numpy as np

first = np.loadtxt("first_simple.txt")

first = first[first[:,3]>100][:,:2] # Condition >100 in column 4 then take remain ing rows take first 2 columns

decsort = np.sort(first[:,1]) # Take 2nd column then sort it

decdiffs = decsort[1:] - decsort[:-1] # Cut out first and last one

decdiffs = abs(decdiffs) # Absolute (non-negative) values

mindiff = decdiffs.min() # Searching for the smallest value in the array

mindiff = np.argmin(decdiffs) # Tells us where min dec is

#decsort[3266]
#decsort[3267]

dec0,dec1 = decsort[mindiff+1],decsort[mindiff]

#dec0, dec1

print(first[first[:,1]==dec0])

import numpy as np
import time

start_time = time.time()

a = np.loadtxt("first_simple.txt")
#ra = a[:,0]; dec = a[:,1]; peakflux = a[:,2]; totalflux = a[:,3]; minor = a[:,5]

strong = a[a[:,2]>100] # sources > 100mJy
strong_resolved = strong[strong[:,5]>0] # Searching the 6th column where a source is resolved
strong_unresolved = strong[strong[:,5]==0] # unresolved sources in 6th column
        
print(time.time() - start_time) # prints the time for code to run (useful for checking "for" loops against array indexing to see how much time is saved with different methods)

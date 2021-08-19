import numpy as np
import time

start_time = time.time()

a = np.loadtxt("first_simple.txt")
#ra = a[:,0]; dec = a[:,1]; peakflux = a[:,2]; totalflux = a[:,3]; minor = a[:,5]

strong = a[a[:,2]>100] # sources > 100mJy
strong_resolved = strong[strong[:,5]>0]
strong_unresolved = strong[strong[:,5]==0]
        
print(time.time() - start_time)

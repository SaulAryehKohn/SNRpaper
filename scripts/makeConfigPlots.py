import pylab
import numpy as np

y,x=np.loadtxt('../data/psa64_positions.dat',unpack=True)

pylab.plot(x,y,'ks')

pylab.xlabel('E-W (m)',size=15)
pylab.ylabel('N-S (m)',size=15)

pylab.show()
pylab.close()

XX,YY=[],[]

for i in range(x.shape[0]):
    for j in range(x.shape[0]):
        XX.append(x[i]-x[j])
        YY.append(y[i]-y[j])

M = []
for k in range(len(XX)):
    M.append(np.sqrt(XX[k]**2. + YY[k]**2.))
M = np.array(M)
mask = (M<301.)*(M>20.)
XX=np.array(XX)
YY=np.array(YY)

pylab.plot(XX[mask],YY[mask],'ks')

#pylab.hexbin(XX[mask],YY[mask])
#pylab.colorbar()

pylab.xlabel('u (m)',size=15)
pylab.ylabel('v (m)',size=15)
pylab.show()
pylab.close()

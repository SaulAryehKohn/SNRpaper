import pyfits
import pylab
import numpy as np
from scipy.optimize import curve_fit

hdu = pyfits.open('../catalogs_plain/AllPaladiniFluxes.fits')
PalFlux = hdu[1].data

S1_4,S2_7,S4_8,S5 = [],[],[],[]
eS1_4,eS2_7,eS4_8,eS5 = [],[],[],[]

for i in range(PalFlux['Gname'].shape[0]):
    S1_4.append(np.average([PalFlux['S1_4GHz1'][i],PalFlux['S1_4GHz2'][i]]))
    eS1_4.append(np.std([PalFlux['S1_4GHz1'][i],PalFlux['S1_4GHz2'][i]]))

    tS2_7 = np.average([PalFlux['S2_7GHz1'][i],PalFlux['S2_7GHz2'][i],
    PalFlux['S2_7GHz3'][i],PalFlux['S2_7GHz4'][i],
    PalFlux['S2_7GHz5'][i],PalFlux['S2_7GHz6'][i],
    PalFlux['S2_7GHz7'][i],PalFlux['S2_7GHz8'][i],
    PalFlux['S2_7GHz9'][i],PalFlux['S2_7GHz10'][i],
    PalFlux['S2_7GHz11'][i],PalFlux['S2_7GHz12'][i]])
    S2_7.append(tS2_7)

    tS2_7 = np.std([PalFlux['S2_7GHz1'][i],PalFlux['S2_7GHz2'][i],
    PalFlux['S2_7GHz3'][i],PalFlux['S2_7GHz4'][i],
    PalFlux['S2_7GHz5'][i],PalFlux['S2_7GHz6'][i],
    PalFlux['S2_7GHz7'][i],PalFlux['S2_7GHz8'][i],
    PalFlux['S2_7GHz9'][i],PalFlux['S2_7GHz10'][i],
    PalFlux['S2_7GHz11'][i],PalFlux['S2_7GHz12'][i]])
    eS2_7.append(tS2_7)


    S4_8.append(np.average([PalFlux['S4_8GHz1'][i],PalFlux['S4_8GHz2'][i]]))
    eS4_8.append(np.std([PalFlux['S4_8GHz1'][i],PalFlux['S4_8GHz2'][i]]))

    tS5 = np.average([PalFlux['S5GHz1'][i],PalFlux['S5GHz2'][i],
    PalFlux['S5GHz3'][i],PalFlux['S5GHz4'][i],PalFlux['S5GHz5'][i],
    PalFlux['S5GHz6'][i],PalFlux['S5GHz7'][i],PalFlux['S5GHz8'][i]])
    S5.append(tS5)

    tS5 = np.std([PalFlux['S5GHz1'][i],PalFlux['S5GHz2'][i],
    PalFlux['S5GHz3'][i],PalFlux['S5GHz4'][i],PalFlux['S5GHz5'][i],
    PalFlux['S5GHz6'][i],PalFlux['S5GHz7'][i],PalFlux['S5GHz8'][i]])
    eS5.append(tS5)

print 'COMPLETE: readthrough and stats from flux catalog'

S1_4 = np.ma.masked_less_equal(S1_4,0)
S2_7 = np.ma.masked_less_equal(S2_7,0)
S4_8 = np.ma.masked_less_equal(S4_8,0)
S5 = np.ma.masked_less_equal(S5,0)

eS1_4 = np.ma.masked_less_equal(eS1_4,0)
eS2_7 = np.ma.masked_less_equal(eS2_7,0)
eS4_8 = np.ma.masked_less_equal(eS4_8,0)
eS5 = np.ma.masked_less_equal(eS5,0)

f1_4 = np.ones(S1_4.shape)*1.4
f2_7 = np.ones(S2_7.shape)*2.7
f4_8 = np.ones(S4_8.shape)*4.8
f5 = np.ones(S5.shape)*5
"""
print 'BEGIN: plotting points'
pylab.errorbar(f1_4,S1_4,yerr=eS1_4,alpha=0.1)
pylab.errorbar(f2_7,S2_7,yerr=eS2_7,alpha=0.1)
pylab.errorbar(f4_8,S4_8,yerr=eS4_8,alpha=0.1)
pylab.errorbar(f5,S5,yerr=eS5,alpha=0.1)
"""
def fitFunc(x,m,c):
    return m*x + c

freqs = np.log10(np.array([1.4,2.7,4.8,5.]))
A,eA,C = [],[],[]

print 'BEGIN: fitting'
for i in range(PalFlux['Gname'].shape[0]):
    S = np.log10(np.array([S1_4[i],S2_7[i],S4_8[i],S5[i]]))
    fitParams,fitCovariances = curve_fit(fitFunc,freqs,S)
    #fitParams,fitCovariances = curve_fit(fitFunc,S,freqs)
    A.append(fitParams[0])
    eA.append(np.sqrt(fitCovariances[0,0]))
    C.append(fitParams[1])
    #pylab.plot(freqs,S,'k.',alpha=0.1)

    line = []
    for j in range(4):
        line.append( fitFunc(S[j],fitParams[0],fitParams[1]) )
    pylab.plot(freqs,line,alpha=0.1,'k-',alpha=0.1)
pylab.show()
pylab.close()
#pylab.plot(A,'bo')
#pylab.hist(A,bins=100,range=(-5,5))
pylab.show()

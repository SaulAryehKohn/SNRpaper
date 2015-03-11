import pyfits
import numpy as np
import pylab

hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
GreenVus = hdulist[1].data
expected = []
measured = []
c=0
for i in range(GreenVus['SNR'].shape[0]):

    Green_name = GreenVus['SNR'][i]
    ra = GreenVus['_RAJ2000'][i]
    dec= GreenVus['_DEJ2000'][i]
    maj= GreenVus['MajDiam'][i]
    S_1GHz = GreenVus['S_1GHz_'][i]
    u_S_1GHz=GreenVus['u_S_1GHz_'][i]
    SpIndex =GreenVus['Sp-Index'][i]
    u_SpIndex=GreenVus['u_Sp-Index'][i]

    #if u_S_1GHz=='?' or u_SpIndex=='?' or maj>5.: continue #i.e. throw out uncertain or diffuse data
    if u_S_1GHz=='?' or u_SpIndex=='?': continue
    expected.append(S_1GHz*(1.E9/145.E6)**(-1*SpIndex))
    measured.append(GreenVus['Total_flux'][i])


    #log(F_1GHz/F_145MHz) = -alpha*log(1E9/145E6)
    #log_stuff = -1*SpIndex*np.log10(1.E9/145.E6)
    #log1G_145M.append(log_stuff)
    c+=1
print c


expected = np.array(expected)
measured = np.array(measured)

n, bins, patches = pylab.hist(expected/measured, 20, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.xlabel(r'Expected S$_{145\,\rm{MHz}}$ / Measured S$_{145\,\rm{MHz}}$',size=15)
pylab.ylabel('Count',size=15)

pylab.show()

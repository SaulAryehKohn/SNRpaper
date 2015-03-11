import pyfits
import numpy as np
#import pylab

hdulist0=pyfits.open('../catalogs_plain/PyBDSM_catalog.fits')
Us = hdulist0[1].data

hdulist_GvU=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
GreenVus = hdulist_GvU[1].data

hdulist_PvU = pyfits.open('../catalogs_matched/Paladini_vs_PyBDSM.fits')
PaladiniVus = hdulist_PvU[1].data

print '#ID In_Green? In_Paladini?'
for i in range(Us['Gaus_id'].shape[0]):
    ID = Us['Gaus_id'][i]
    tempstring = str(ID)
    if ID in GreenVus['Gaus_id']: tempstring+=' Y'
    else: tempstring+=' N'
    if ID in PaladiniVus['Gaus_id']: tempstring+=' Y'
    else: tempstring+=' N'
    print tempstring
    if 'N Y' in tempstring: print 'interesting'

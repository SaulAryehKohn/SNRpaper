import pyfits
import numpy as np
#import pylab

hdulist0=pyfits.open('../catalogs_plain/newPyBDSM_catalog.fits')
Us = hdulist0[1].data

hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
GreenVus = hdulist[1].data

hdulist_G = pyfits.open('../catalogs_plain/Green2014.fits')
Green = hdulist_G[1].data

print 'GREEN SEES IT, WE DO NOT'
print '#Name RA DEC Maj'# S_1GHz flag_1GHz SpIndex flag_SpIndex'
c = 0
for i in range(Green['SNR'].shape[0]):
    Green_name = Green['SNR'][i]
    ra = Green['_RAJ2000'][i]
    dec= Green['_DEJ2000'][i]
    maj= Green['MajDiam'][i]
    #S_1GHz = Green['S_1GHz_'][i]
    u_S_1GHz=Green['u_S_1GHz_'][i]
    #SpIndex =Green['Sp-Index'][i]
    #u_SpIndex=Green['u_Sp-Index'][i]

    if Green_name in GreenVus['SNR']: continue
    else:
        if u_S_1GHz!='?':
            c+=1
            print Green_name,ra,dec,maj,u_S_1GHz#,S_1GHz,u_S_1GHz,SpIndex,u_SpIndex
print c

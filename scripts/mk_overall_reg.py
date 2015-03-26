import pyfits
import numpy as np
import os

hdulist0=pyfits.open('PyBDSM_catalog.fits')
Us = hdulist0[1].data

hdulist=pyfits.open('Matches/PyBDSM_vs_Green14.fits')
Green = hdulist[1].data

hdulist2=pyfits.open('Matches/PyBDSM_vs_Jacobs.fits')
Jacobs = hdulist2[1].data

hdulist3 = pyfits.open('Matches/PyBDSM_vs_MOSTSNRCAT.fits')
MSCAT = hdulist3[1].data

hdulist4 = pyfits.open('Matches/PyBDSM_vs_Paladini03.fits')
Paladini = hdulist4[1].data

hdulist5 = pyfits.open('Matches/PyBDSM_vs_MGPS.fits')
MGPS = hdulist5[1].data


test=False

"""
BLUE = PyBDSM
GREEN = D. A. GREEN (2014)
YELLOW= MOSTSNRCAT
RED = PALADINI+ (2013)
CYAN= JACOBS+ (2011)
"""

if test==False:
    os.system('rm ForDs9.reg')
    F = open('ForDs9.reg','w')

if test==False: print >> F, '# Region file format: DS9 version 4.1 \nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nfk5'
else: print '# Region file format: DS9 version 4.1 \nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nfk5'

if test==False: print >> F, 'global color=blue'
else: print 'global color=blue'

for i in range(Us.shape[0]):#Us: no ellipse -- just give 20arcmin circle
    if test==False: print >> F, 'circle('+str(Us['XY2RA'][i])+','+str(Us['XY2DEC'][i])+',600") # text={'+str(Us['Gaus_id'][i])+'}'
    else:print 'circle('+str(Us['XY2RA'][i])+','+str(Us['XY2DEC'][i])+',600") # text={'+str(Us['Gaus_id'][i])+'}'

if test==False:
    print >> F, 'global color=green'
    for i in range(Green.shape[0]):#Green et al. 2014
        print >> F, 'circle('+str(Green['XY2RA'][i])+','+str(Green['XY2DEC'][i])+','+str(int(Green['Dmaj'][i]*60))+'") # text={'+Green['SNR'][i]+'}'


    print >> F, 'global color=yellow'
    for i in range(MSCAT.shape[0]):#MOSTSNRCAT
        majax = str(int(MSCAT['major_axis'][i]*60))
        if majax > 0: print >> F, 'circle('+str(MSCAT['XY2RA'][i])+','+str(MSCAT['XY2DEC'][i])+','+majax+'")'

    print >> F, 'global color=red'
    for i in range(Paladini.shape[0]):#Paladini et al. 2003
        print >> F, 'box('+str(Paladini['XY2RA'][i])+','+str(Paladini['XY2DEC'][i])+',1000",1000") # text={'+Paladini['Gname'][i]+'}'

    print >> F, 'global color=cyan'
    for i in range(Jacobs.shape[0]):#Paladini et al. 2003
        print >> F, 'box('+str(Jacobs['XY2RA'][i])+','+str(Jacobs['XY2DEC'][i])+',1000",1000") # text={'+Jacobs['Cul'][i]+'}'




F.close()
"""
print >> F, 'global color=red'

for i in range(tbdata3.shape[0]):#MOSTSNRCAT

	boxw = 60*2*np.sqrt(tbdata3[i][33]/2)
	print i, tbdata3[i][33], boxw
	try: print >> F, 'box('+str(tbdata3[i][28])+','+str(tbdata3[i][29])+','+str(int(boxw))+'",'+str(int(boxw))+'",'+str(45)+') # text={'+str(tbdata3[i][27])+'}'
	except ValueError: print >> F, 'box('+str(tbdata3[i][28])+','+str(tbdata3[i][29])+',1000",1000",'+str(45)+') # text={'+str(tbdata3[i][27])+'}'
F.close()
"""

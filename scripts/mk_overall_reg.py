import pyfits
import numpy as np
import os

hdulist0=pyfits.open('../catalogs_plain/newPyBDSM_catalog.fits')
Us = hdulist0[1].data

hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
Green = hdulist[1].data

hdulist2=pyfits.open('../catalogs_matched/Jacobs_vs_PyBDSM.fits')
Jacobs = hdulist2[1].data

hdulist3 = pyfits.open('../catalogs_matched/MOSTSNRCAT_vs_PyBDSM.fits')
MSCAT = hdulist3[1].data

hdulist4 = pyfits.open('../catalogs_matched/Paladini_vs_PyBDSM.fits')
Paladini = hdulist4[1].data

hdulist5 = pyfits.open('../catalogs_matched/MGPS_vs_PyBDSM.fits')
MGPS = hdulist5[1].data

hdulist6 = pyfits.open('../catalogs_matched/MGPS-Green_vs_PyBDSM.fits')
AliceGreen = hdulist6[1].data

test=False
TEXT=True
"""
BLUE CIRCLE = PyBDSM
GREEN CIRCLE = D. A. GREEN (2014) #(name has 'D')
RED CIRCLE = MOSTSNRCAT
YELLOW CIRCLE = PALADINI+ (2013)
CYAN (/GREEN? WEIRD.) BOX = JACOBS+ (2011)
MAGENTA A. J. GREEN+ (2014) #(name has 'A')
"""

if test==False:
    os.system('rm MEGAREG.reg')
    F = open('MEGAREG.reg','w')

if test==False: print >> F, '# Region file format: DS9 version 4.1 \nglobal dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nfk5'
else: print '# Region file format: DS9 version 4.1 \nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1 \nfk5'

if test==False: print >> F, 'global color=blue'
else: print 'global color=blue'

for i in range(Us.shape[0]):#Us: no ellipse -- just give 20arcmin circle
	if TEXT:
		if test==False: print >> F, 'circle('+str(Us['PyRA'][i])+','+str(Us['PyDEC'][i])+','+str(Us['Maj'][i]*3600.)+'") # text={'+str(Us['Source_id'][i])+'}'
		else:print 'circle('+str(Us['PyRA'][i])+','+str(Us['PyDEC'][i])+','+str(Us['Maj'][i]*3600.)+'") # text={'+str(Us['Source_id'][i])+'}'

		if test==False:
			print >> F, 'global color=green'
			for i in range(Green.shape[0]):#Green et al. 2014
				print >> F, 'circle('+str(Green['_RAJ2000'][i])+','+str(Green['_DEJ2000'][i])+','+str(Green['MajDiam'][i]*60.)+'") # text={D'+Green['SNR'][i]+'}'

			print >> F, 'global color=red'
			for i in range(MSCAT.shape[0]):#MOSTSNRCAT
				majax = str(MSCAT['DMaj'][i]*60.)
				if majax > 0: print >> F, 'circle('+str(MSCAT['_RAJ2000'][i])+','+str(MSCAT['_DEJ2000'][i])+','+majax+'")'

			print >> F, 'global color=yellow'
			for i in range(Paladini.shape[0]):#Paladini et al. 2003
				print >> F, 'circle('+str(Paladini['_RAJ2000'][i])+','+str(Paladini['_DEJ2000'][i])+','+str(Paladini['theta'][i]*30.)+'") # text={'+Paladini['Gname'][i]+'}'

			print >> F, 'global color=cyan'
			for i in range(Jacobs.shape[0]):#Jacobs et al. 2011
				print >> F, 'box('+str(Jacobs['_RAJ2000'][i])+','+str(Jacobs['_DEJ2000'][i])+',900",900") # text={MRC '+Jacobs['MRC'][i]+'}'

			print >> F, 'global color=green'
			for i in range(AliceGreen.shape[0]):
				print >> F, 'circle('+str(AliceGreen['RA_deg'][i])+','+str(AliceGreen['DEC_deg'][i])+','+str(AliceGreen['Size_1'][i]*60.)+'") # text={A'+AliceGreen['#Source'][i]+'}'
	else:
		if test==False: print >> F, 'circle('+str(Us['PyRA'][i])+','+str(Us['PyDEC'][i])+','+str(Us['Maj'][i]*3600.)+'")'
		else:print 'circle('+str(Us['PyRA'][i])+','+str(Us['PyDEC'][i])+','+str(Us['Maj'][i]*3600.)+'")'

		if test==False:
			print >> F, 'global color=green'
			for i in range(Green.shape[0]):#Green et al. 2014
				print >> F, 'circle('+str(Green['_RAJ2000'][i])+','+str(Green['_DEJ2000'][i])+','+str(Green['MajDiam'][i]*60.)+'")'

			print >> F, 'global color=red'
			for i in range(MSCAT.shape[0]):#MOSTSNRCAT
				majax = str(MSCAT['DMaj'][i]*60.)
				if majax > 0: print >> F, 'circle('+str(MSCAT['_RAJ2000'][i])+','+str(MSCAT['_DEJ2000'][i])+','+majax+'")'

			print >> F, 'global color=yellow'
			for i in range(Paladini.shape[0]):#Paladini et al. 2003
				print >> F, 'circle('+str(Paladini['_RAJ2000'][i])+','+str(Paladini['_DEJ2000'][i])+','+str(Paladini['theta'][i]*30.)+'")'

			print >> F, 'global color=cyan'
			for i in range(Jacobs.shape[0]):#Jacobs et al. 2011
				print >> F, 'box('+str(Jacobs['_RAJ2000'][i])+','+str(Jacobs['_DEJ2000'][i])+',900",900")'

			print >> F, 'global color=green'
			for i in range(AliceGreen.shape[0]):
				print >> F, 'circle('+str(AliceGreen['RA_deg'][i])+','+str(AliceGreen['DEC_deg'][i])+','+str(AliceGreen['Major'][i]*60.)+'")'

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

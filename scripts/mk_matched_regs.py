import numpy as np
import pyfits

#SNRs
DG = False
AG = False
MS = False

#HIIs
PA = True

#Others
DJ = True



"""
SUPERNOVA REMNANTS
"""


if DG:
	print 'Matches D. Green vs PyBDSM'
	hdu=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
	DGvPy = hdu[1].data

	F = open('../data/DGvPy.reg','w')

	print >> F, '# Region file format: DS9 version 4.1'
	print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
	print >> F, 'fk5'
	print >> F, 'global color=green'

	for i in range(DGvPy['PyRA'].shape[0]):
		print >> F, 'circle(%f,%f,%f") # text={%s}'%(DGvPy['PyRA'][i],DGvPy['PyDEC'][i],DGvPy['Maj'][i]*3600,DGvPy['SNR'][i])

	F.close()


if AG:
	print 'Matches A. Green vs PyBDSM'
	hdu=pyfits.open('../catalogs_matched/MGPS-Green_vs_PyBDSM.fits')
	AGvPy = hdu[1].data

	F = open('../data/AGvPy.reg','w')

	print >> F, '# Region file format: DS9 version 4.1'
	print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
	print >> F, 'fk5'
	print >> F, 'global color=green'

	for i in range(AGvPy['PyRA'].shape[0]):
		print >> F, 'box(%f,%f,%f",%f") # text={%s}'%(AGvPy['PyRA'][i],AGvPy['PyDEC'][i],AGvPy['Maj'][i]*3600,AGvPy['Maj'][i]*3600,AGvPy['#Source'][i])

	F.close()

if MS:
	print 'Matches MOSTSNRCAT vs PyBDSM'
	hdu=pyfits.open('../catalogs_matched/MOSTSNRCAT_vs_PyBDSM.fits')
	MSvPy = hdu[1].data

	F = open('../data/MSvPy.reg','w')

	print >> F, '# Region file format: DS9 version 4.1'
	print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
	print >> F, 'fk5'
	print >> F, 'global color=red'

	for i in range(AGvPy['PyRA'].shape[0]):
		print >> F, 'circle(%f,%f,%f") # text={%s}'%(MSvPy['PyRA'][i],MSvPy['PyDEC'][i],MSvPy['Maj'][i]*3600,MSvPy['MSC'][i])

	F.close()


"""
HII REGIONS
"""


if PA:
	print 'Matches Paladini vs PyBDSM'
	hdu=pyfits.open('../catalogs_matched/Paladini_vs_PyBDSM.fits')
	PalvPy = hdu[1].data

	F = open('../data/PalvPy.reg','w')

	print >> F, '# Region file format: DS9 version 4.1'
	print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
	print >> F, 'fk5'
	print >> F, 'global color=yellow'

	for i in range(PalvPy['PyRA'].shape[0]):
		print >> F, 'circle(%f,%f,%f") # text={%s}'%(PalvPy['PyRA'][i],PalvPy['PyDEC'][i],PalvPy['Maj'][i]*3600,PalvPy['Gname'][i])

	F.close()

"""
EXTRAGALACTIC SOURCES
"""


if DJ:
	print 'Matches Jacobs vs PyBDSM'
	hdu=pyfits.open('../catalogs_matched/Jacobs_vs_PyBDSM.fits')
	JacvPy = hdu[1].data

	F = open('../data/JacvPy.reg','w')

	print >> F, '# Region file format: DS9 version 4.1'
	print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
	print >> F, 'fk5'
	print >> F, 'global color=cyan'

	for i in range(JacvPy['PyRA'].shape[0]):
		print >> F, 'circle(%f,%f,%f") # text={%s}'%(JacvPy['PyRA'][i],JacvPy['PyDEC'][i],JacvPy['Maj'][i]*3600,JacvPy['MRC'][i])

	F.close()
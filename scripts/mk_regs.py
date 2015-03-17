import numpy as np
import pyfits

igno = False #in green not ours
hii= False #HII regions
other = True #unmatched
if igno:
    hdu=pyfits.open('../data/InGreenNotOurs.fits')
    IGNO = hdu[1].data

    F = open('../data/IGNO.reg','w')

    print >> F, '# Region file format: DS9 version 4.1'
    print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
    print >> F, 'fk5'
    print >> F, 'global color=green'

    for i in range(IGNO['Name'].shape[0]):
        print >> F, 'circle(%f,%f,%f") # text={%s}'%(IGNO['RA'][i],IGNO['DEC'][i],IGNO['Maj'][i]*60,IGNO['Name'][i])

    F.close()

if hii:
    F = open('../data/HII.reg','w')
    ID,RA,DEC,Maj=np.loadtxt('../data/HIIregions.txt',unpack=True)

    print >> F, '# Region file format: DS9 version 4.1'
    print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
    print >> F, 'fk5'
    print >> F, 'global color=yellow'

    for i in range(ID.shape[0]):
        print >> F, 'circle(%f,%f,%f") # text={%i}'%(RA[i],DEC[i],Maj[i]*3600,ID[i])

    F.close()

if other:
    F = open('../data/MIA.reg','w')
    ID,RA,DEC,Maj = np.loadtxt("../data/Wills_listylisty.txt",unpack=True)
    print >> F, '# Region file format: DS9 version 4.1'
    print >> F, 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'
    print >> F, 'fk5'
    print >> F, 'global color=red'

    for i in range(ID.shape[0]):
        print >> F, 'circle(%f,%f,%f") # text={%i}'%(RA[i],DEC[i],Maj[i]*3600,ID[i])

    F.close()

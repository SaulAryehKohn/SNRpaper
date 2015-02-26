import pyfits
import numpy as np
#import pylab

hdulist0=pyfits.open('PyBDSM_catalog.fits')
Us = hdulist0[1].data

hdulist=pyfits.open('catalogs_matched/Green_vs_PyBDSM.fits')
Green = hdulist[1].data

hdulist2=pyfits.open('catalogs_matched/Jacobs_vs_PyBDSM.fits')
Jacobs = hdulist2[1].data

hdulist3 = pyfits.open('catalogs_matched/MOSTSNRCAT_vs_PyBDSM.fits')
MSCAT = hdulist3[1].data

hdulist4 = pyfits.open('catalogs_matched/Paladini_vs_PyBDSM.fits')
Paladini = hdulist4[1].data

hdulist5 = pyfits.open('catalogs_matched/MGPS_vs_PyBDSM.fits')
MGPS = hdulist5[1].data
#MASK MGPS to compact sources only (<5') and flux > X mJy
MASK = (MGPS['MajAxis']<=300.)*(MGPS['St'] >= 5)

MGPS = MGPS[MASK]

hdulist6 = pyfits.open('catalogs_matched/MGPS-Green_vs_PyBDSM.fits')
A_Green = hdulist6[1].data

hdulist7 = pyfits.open('catalogs_matched/MSX_vs_PyBDSM.fits')
MSX_vs_PyBDSM = hdulist7[1].data


"""
#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---
Also worth thinking about: all the different SGPS surveys

HI clouds in Southern Galactic Plane Survey (Kavars+, 2005) = http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/ApJ/626/887/table2&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa
H2O Southern Galactic Plane Survey (HOPS) (Walsh+, 2011) = http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/MNRAS/416/1764&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa
H2O Southern Galactic Plane Survey, HOPS. II (Purcell+, 2012) = http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/MNRAS/426/1972&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa
Atlas of HI absorption toward HII regions in SGPS I (Brown+, 2014) = http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/ApJS/211/29&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa
HI clouds in Southern Galactic Plane Survey (Kavars+, 2005) = http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/ApJ/626/887&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa
#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---
"""

#first-order stuff -- which catalog are they in? Not looking for doubles yet.
print '#PyBDSMID	IN_GREEN?	IN_MOSTSNRCAT?   IN_A_Green?   IN_JACOBS?  IN_MGPS_compact?    IN_PALADINI?'

toWill_list = []
for ID in Us['Gaus_id']:
    toWill = True
    tempstring = ''
    tempstring=tempstring+str(ID)

    if ID in Green['Gaus_id']:
        tempstring +=' Y'
        toWill*=False
    else: tempstring +=' N'

    if ID in MSCAT['Gaus_id']:
        tempstring +=' Y'
        toWill*=False
    else: tempstring +=' N'

    if ID in A_Green['Gaus_id']:
        tempstring +=' Y'
        toWill*=False
    else: tempstring +=' N'

    if ID in Jacobs['Gaus_id']:
        tempstring +=' Y'
        toWill*=False
    else: tempstring +=' N'

    if ID in MGPS['Gaus_id']:
        tempstring +=' Y'
        toWill*=False
    else: tempstring +=' N'

    if ID in Paladini['Gaus_id']:
        tempstring +=' Y'
        toWill*=False
    else: tempstring +=' N'

print tempstring
if toWill == True: toWill_list.append(ID)

print "These need to go to Will:"
print toWill_list
print 'Num:',len(toWill_list)

print '#ID  RA_deg  DEC_deg FLUX_Jy    SEMI-MAJOR-AXIS_deg '
for i in range(Us['Gaus_id'].shape[0]):
    if Us['Gaus_id'][i] in toWill_list:
        print Us['Gaus_id'][i],Us['XY2RA'][i],Us['XY2DEC'][i],Us['Total_flux'][i],Us['Maj'][i]

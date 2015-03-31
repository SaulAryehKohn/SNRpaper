import pyfits
import numpy as np
import pylab
import sys

hdulist0=pyfits.open('../catalogs_plain/PyBDSM_catalog.fits')
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
#MASK MGPS to compact sources only (<5') and flux > 300(?) mJy
MASK = (MGPS['MajAxis']<=300.)*(MGPS['St'] >= 5.)

MGPS = MGPS[MASK]

hdulist6 = pyfits.open('../catalogs_matched/MGPS-Green_vs_PyBDSM.fits')
A_Green = hdulist6[1].data

hdulist7 = pyfits.open('../catalogs_matched/MSX_vs_PyBDSM.fits')
MSX_vs_PyBDSM = hdulist7[1].data



"""
#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---

Also worth thinking about: all the different SGPS surveys

HI clouds in Southern Galactic Plane Survey (Kavars+, 2005) =
http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/ApJ/626/887/table2&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa

H2O Southern Galactic Plane Survey (HOPS) (Walsh+, 2011) =
http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/MNRAS/416/1764&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa

H2O Southern Galactic Plane Survey, HOPS. II (Purcell+, 2012) =
http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/MNRAS/426/1972&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa

Atlas of HI absorption toward HII regions in SGPS I (Brown+, 2014) =
http://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/ApJS/211/29&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa

#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---#---
"""

#first-order stuff -- which catalog are they in? Not looking for doubles yet.
print '#PyBDSMID	IN_GREEN?	IN_MOSTSNRCAT?   IN_A_Green?   IN_JACOBS?  IN_MGPS_compact?    IN_PALADINI?'

toWill_list = []

exgal_list = [] #only identified as a Danny source

DGSNR_list,AGSNR_list,MSSNR_list=[],[],[] #only identified as an SNR from those 3 surveys

multSNRlist_list = [] #detected by more than one of the 3 SNR surveys

hii_list=[] #only detected as an hii region
mgps_list=[] #only detected as an MGPS object

hii_in_SNR = [] #an HII region inside an SNR a la W28 and W30

other_mult_lists = [] #A.O.B.

strings = []

for ID in Us['Gaus_id']:
    toWill = True
    tempstring = ''
    tempstring=tempstring+str(ID)

    if ID in Green['Gaus_id']:
        tempstring +=' Y'
    else: tempstring +=' N'

    if ID in MSCAT['Gaus_id']:
        tempstring +=' Y'
    else: tempstring +=' N'

    if ID in A_Green['Gaus_id']:
        tempstring +=' Y'
    else: tempstring +=' N'

    if ID in Jacobs['Gaus_id']:
        tempstring +=' Y'
    else: tempstring +=' N'

    if ID in MGPS['Gaus_id']:
        tempstring +=' Y'
    else: tempstring +=' N'

    if ID in Paladini['Gaus_id']:
        tempstring +=' Y'
    else: tempstring +=' N'

    print tempstring
    strings.append([ID,tempstring])
    
    # HACKHACKHACK
    #
    # Letting it identify if it's in an SNR catalog OR SNR catalog + MGPS 
    # 
    # This leads to DGSNR+17
    # 				MSSNR+2
    #				AGSNR+2
    #
    if 'N N N N N N' in tempstring: toWill_list.append(ID)
    elif 'Y N N N N N' in tempstring or 'Y N N N Y N' in tempstring: DGSNR_list.append(ID)
    elif 'N Y N N N N' in tempstring or 'N Y N N Y N' in tempstring: MSSNR_list.append(ID)
    elif 'N N Y N N N' in tempstring or 'N N Y N Y N' in tempstring: AGSNR_list.append(ID)
    elif 'N N N Y N N' in tempstring: exgal_list.append(ID)
    elif 'N N N N Y N' in tempstring: mgps_list.append(ID)
    elif 'N N N N N Y' in tempstring: hii_list.append(ID)
    elif 'Y Y N N N N' in tempstring or 'Y N Y N N N' in tempstring or 'N Y Y N N N' in tempstring or 'Y Y Y N N N' in tempstring: multSNRlist_list.append(ID)
    elif 'Y N N N N Y' in tempstring or 'N Y N N N Y' in tempstring or 'Y Y N N N Y' in tempstring or 'N N Y N N Y' in tempstring or 'Y N Y N N Y' in tempstring or 'N Y Y N N Y' in tempstring or 'Y Y Y N N Y' in tempstring: hii_in_SNR.append(ID)
    else: other_mult_lists.append(ID)
	
list_of_lists = [toWill_list,DGSNR_list,MSSNR_list,AGSNR_list,exgal_list,mgps_list,hii_list,multSNRlist_list,hii_in_SNR,other_mult_lists]

name_of_lists = ['toWill_list','DGSNR_list','MSSNR_list','AGSNR_list','exgal_list','mgps_list','hii_list','multSNRlist_list','hii_in_SNR','other_mult_lists']

#to first order, what catalog contains their info (ie neglecting double+ matches)
nada = np.array([])
source_cats = [nada,Green,MSCAT,A_Green,Jacobs,MGPS,Paladini,nada,nada,nada]

print ''

for k in range(len(list_of_lists)): #for each list
	listname = name_of_lists[k]
	list = list_of_lists[k]
	sourceCat = source_cats[k]
	print '\n',listname,len(list),'\n'
	
	print 'ID RA DEC Maj EMaj Flux EFlux'
	for m in range(len(list)): #for each entry in each list
		ID = list[m]
		for p in range(Us['Gaus_id'].shape[0]): #for each ID in the master list
			IDcat = Us['Gaus_id'][p]
			if IDcat == ID: #if the master ID matches with the ID in the list in question
				if sourceCat.shape[0]== 0: #if it does NOT come from a single catalog
					continue 
					#print ID,Us['PyRA'][m],Us['PyDEC'][m],Us['Maj'][m],Us['E_Maj'][m],Us['Total_flux'][m],Us['E_Total_flux'][m]
				else: #if it DOES
					if k == 1: #D. Green 2014
						print 'Green info + ours'
					if k == 2: #MOSTSNRCAT
						print 'MSCAT info + ours'
					if k == 3: #A. Green et al.
						print 'A. Green info + ours'
					if k ==4: #Jacobs et al. 2011
						print 'hi Danny!'
					if k == 5: #MGPS
						print 'MGPS info + ours'
					if k == 6: #Paladini et al. 2003
						print 'Paladini info +ours'
					

####################################################

sys.exit('\nNot printing LaTeX tables right now\n')

####################################################

# MIA sources
print "These need to go to Will:"
print toWill_list
print 'Num:',len(toWill_list)
print '#ID  RA_deg  DEC_deg SEMI-MAJOR-AXIS_deg '
for i in range(Us['Gaus_id'].shape[0]):
    if Us['Gaus_id'][i] in toWill_list:
        print Us['Gaus_id'][i],Us['PyRA'][i],Us['PyDEC'][i],Us['Maj'][i]


#HII regions
print 'These are HII regions that we appear to detect:'
print hii_list
print 'Num:',len(hii_list)

####################################################


latex = False

if latex: 
	print '#PalName RA_deg  DEC_deg PAPER_Maj_arcmin Pal_Maj_arcmin Total_flux_Jy e_Total_flux_Jy Flux_2.7GHz e_Flux_2.7GHz'
	for i in range(Paladini['Gaus_id'].shape[0]):
		if Paladini['Gaus_id'][i] in interest_list:
			print Paladini['Gname'][i],'&',Paladini['XY2RA'][i],'&',Paladini['XY2DEC'][i],'&',round(Paladini['Maj'][i]*60.,0),'$\pm$',round(Paladini['E_Maj'][i]*60.,0),'&',round(Paladini['theta'][i]/2.,1),'$\pm$',round(Paladini['e_theta'][i]/2.,1),'&',round(Paladini['Total_flux'][i],1),'$\pm$',round(Paladini['E_Total_flux'][i],1),'&',Paladini['S2_7GHz'][i],'$\pm$',Paladini['e_S2_7GHz'][i],'\\\\'

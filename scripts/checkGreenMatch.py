import pyfits
import numpy as np

hdulist0=pyfits.open('../catalogs_plain/newPyBDSM_catalog.fits')
Us = hdulist0[1].data

hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
GreenVus = hdulist[1].data

#hdulist_G = pyfits.open('../catalogs_plain/Green2014.fits')
hdulist_G = pyfits.open('../Green2014_TEST.fits')
G = hdulist_G[1].data

print G['S']

print 'GREEN SEES IT, WE DO NOT'
print '#Name RA DEC Maj ExpectedFlux Should_we_see_it?'
c = 0
ycount = 0
for i in range(G['SNR'].shape[0]):
    Green_name = G['SNR'][i]
    ra = G['_RAJ2000'][i]
    dec= G['_DEJ2000'][i]
    maj= G['MajDiam'][i]
    #S_1GHz = G['S_1GHz_'][i]
    S_1GHz = G['S'][i]
    u_S_1GHz=G['u_S_1GHz_'][i]
    SpIndex =G['Sp-Index'][i]
    u_SpIndex=G['u_Sp-Index'][i]

    if Green_name in GreenVus['SNR']: continue
    else:
        if u_S_1GHz!='?' and u_SpIndex!='?':
        	if ra<=285. and ra>125. and dec<0. and dec>-65.:
				c+=1
				expected = S_1GHz*(1.E9/145.E6)**(SpIndex)
				
				if expected >= 5. and maj <= (3.*60.): 
					strng = 'Y'
					ycount+=1
				else: strng = 'N'
				
				print Green_name,ra,dec,maj,expected,strng

print 'Num in Green 2014:',G['SNR'].shape[0]
print 'Num we detect:',GreenVus['SNR'].shape[0]
print 'Num we miss (and should see if no self-abs)',ycount

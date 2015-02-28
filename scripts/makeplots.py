import pylab
import numpy as np
import pyfits
from scipy.optimize import curve_fit

RA,DEC,Flux,errFlux,Maj,errMaj = np.loadtxt('nicelist.txt',unpack=True)

hdu = pyfits.open('../catalogs_plain/Jacobs.fits')
Jacobs = hdu[1].data

hdu = pyfits.open('../catalogs_matched/Jacobs_vs_PyBDSM.fits')
Jacobs_matched = hdu[1].data
hdu = pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
Green_matched = hdu[1].data


hist=False
scat=True
if scat==True: linfit=True
table = False
###
###FLUX HISTOGRAMS
###
if hist==True:
    pylab.hist(np.log10(Flux),30,color='b',label='This work (all)')
    pylab.hist(np.log10(Jacobs['S145']),30,color='r',alpha=0.5,label='Jacobs et al. 2011 (all)')
    pylab.hist(np.log10(Jacobs_matched['S145']),30,color='r',label='Jacobs et al. 2011 (matched)')
    pylab.legend(loc='best')
    pylab.xlabel('log$_{10}$(S$_{145}$) (Jy)')
    pylab.ylabel('Count')
    pylab.show()

if scat==True:
    MASK = Jacobs_matched['S145']<100.
    us = Jacobs_matched['Total_flux'][MASK]
    us_err = Jacobs_matched['E_Total_flux'][MASK]
    danny = Jacobs_matched['S145'][MASK]
    danny_err = Jacobs_matched['RMS'][MASK]

    def fitFunc(x,m,c):
        return m*x + c
    def fitFunc2(x,a,b,c):
        return a*x**2. + b*x + c

    for i in range(us.shape[0]):
        pylab.errorbar(us[i],danny[i],xerr=us_err[i],yerr=danny_err[i],fmt='bo')

    if linfit:
        fitParams,fitCovariances = curve_fit(fitFunc,us,danny)
        print ' fit coefficients:\n', fitParams
        print ' Covariance matrix:\n', fitCovariances

        #sigma_m, sigma_c
        sigma = [np.sqrt(fitCovariances[0,0]),np.sqrt(fitCovariances[1,1])]

        print 'LINEAR FIT: JACOBS=(%f+-%f)US + (%f+-%f)'%(fitParams[0],sigma[0],fitParams[1],sigma[1])

        pylab.plot(us,fitFunc(us,fitParams[0],fitParams[1]),'k-')
        pylab.plot(us,fitFunc(us,fitParams[0]+sigma[0],fitParams[1]+sigma[1]),'k:')
        pylab.plot(us,fitFunc(us,fitParams[0]-sigma[0],fitParams[1]-sigma[1]),'k:')

        y1 = (fitParams[0]+sigma[0])*np.sort(us) + fitParams[1]+sigma[1]
        y2 = (fitParams[0]-sigma[0])*np.sort(us) + fitParams[1]-sigma[1]

        pylab.fill_between(np.sort(us),y2,y1,color='black',alpha=0.3)

        pylab.text(5,32,r'$S^{145\,\rm{MHz}}_{\rm{Jacobs\,et\,al.}} \propto (0.9\pm0.2)\,S^{145\,\rm{MHz}}_{\rm{This\,work}}$',fontsize=16)#,bbox=dict(facecolor='red', alpha=0.5))

        pylab.xlim(2.5,30.)
        pylab.ylim(2.4,37.)
    pylab.xlabel('This Work (Jy)',size=15)
    pylab.ylabel('Jacobs et al. 2011 (Jy)',size=15)
    #pylab.suptitle('145 MHz flux of MRC extragalactic sources',size=15)
    pylab.show()

###
#RESULTS TABLES
#PyBDSM: RA,DEC,Flux,errFlux,Maj,errMaj
###
print
if table==True:
    for i in range(RA.shape[0]):
        #if errFlux[i]>Flux[i]:
        #    print NOT READY
        print i,'&',RA[i],'&',DEC[i],'&',str(int(Flux[i]))+'$\pm$'+str(int(errFlux[i])),'&',str(int(Maj[i]*60))+'$\pm$'+str(int(errMaj[i]*60)),'\\\\'

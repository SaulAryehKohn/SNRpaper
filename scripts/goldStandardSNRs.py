import pyfits, pylab, sys
import numpy as np
from scipy.optimize import curve_fit

hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
GreenVus = hdulist[1].data

plot = False

SNRfreqs = [
	['G004.5+06.8',	[[1285,15.4],[1365.1,14.8],[1402.5,14.6],[1464.9,14.2],[4835.1,6.1],[4885.1,6.1]]],
	['G005.5+00.3',	[[330,14.3]]],
	['G007.7-03.7',	[[1400,9.9],[8400,4.6]]],
	['G008.7-00.1',	[[327,129]]],
	['G011.2-00.3',	[[5000,9]]],
	['G018.1-00.1',	[[330,14.3]]],
	['G018.8+00.3',	[[5000,15.3]]],
	['G018.9-01.1',	[[5000,19.6]]],
	['G021.8-00.6',	[[5000,24]]],
	['G023.3-00.3',	[[1400,59.7]]],
	['G292.0+01.8',	[[1400,11.9],[2300,11.4],[5200,8.8]]],
	['G296.7-00.9',	[[1400,2.5]]],
	['G296.8-00.3',	[[1300,7]]],
	['G304.6+00.1',	[[1400,10.9]]],
	['G309.8+00.0',	[[408,26.4],[5000,7.4]]],
	['G315.4-00.3',	[[843,3.1]]],
	['G326.3-01.8',	[[4800,25],[8640,15]]],
	['G337.3+01.0',	[[843,20]]],
	['G340.4+00.4',	[[843,5.9]]],
	['G343.1-00.7',	[[843,8.5],[4500,3.9],[8550,2.4]]],
	['G349.7+00.2',	[[843,22]]],
	['G350.0-02.0',	[[1400,22.3]]],
	['G352.7-00.1',	[[843,4.4],[1400,3.1]]],
	['G355.9-02.5',	[[1000,8],[1470,5],[5000,3.4]]],
	['G356.2+04.5',	[[327,8.1]]],
	['G357.7-00.1',	[[1400,69],[4900,82],[8300,88]]]
	]
	
for i in range(len(SNRfreqs)):
	Gname = SNRfreqs[i][0]
	FreqFluxArr = SNRfreqs[i][1]
	for j in range(GreenVus['SNR'].shape[0]):
		if Gname==GreenVus['SNR'][j]: 
			S_145 = GreenVus['Total_flux'][j]
			E_S_145 = GreenVus['E_Total_flux'][j]
			SpIndex = GreenVus['Sp-Index'][j]
	FreqFluxArr.insert(0,[145.,S_145])
	FreqFluxArr = np.array(FreqFluxArr)
	
	freq_MHz = FreqFluxArr[:,0]
	flux_Jy = FreqFluxArr[:,1]
	
	def fitFunc(x,m,c): return m*x + c
	
	fitParams,fitCovariances = curve_fit(fitFunc,np.log10(freq_MHz),np.log10(flux_Jy))
	#print ' fit coefficients:\n', fitParams
	#print ' Covariance matrix:\n', fitCovariances
	
	sigma = [np.sqrt(fitCovariances[0,0]),np.sqrt(fitCovariances[1,1])]
	
	print '%s: alpha= %f +/- %f | %f | %i'%(Gname,-1.*fitParams[0],sigma[0],SpIndex,len(freq_MHz))
		
	if plot:
		pylab.loglog(freq_MHz, flux_Jy)
		pylab.xlabel(r'$\nu$ (MHz)', size=15)
		pylab.ylabel(r'Integrated Flux (Jy)', size=15)
		pylab.savefig('../figs/SNR_%s_spectrum.png'%Gname)
		pylab.close()
	
	del(Gname);del(FreqFluxArr)

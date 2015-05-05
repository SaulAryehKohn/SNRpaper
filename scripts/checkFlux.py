import pyfits
import numpy as np
import pylab

Green = False
Paladini = True

if Green:
    hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
    GreenVus = hdulist[1].data
    hdudub=pyfits.open('../data/GSNRdoubles.fits')
    GreenDoubles = hdudub[1].data
    DubNames = GreenDoubles['Green_SNR']
    
    name = []
    expected = []
    e_expected=[]
    measured = []
    e_measured=[]
    major = []
    c=0
    for i in range(GreenVus['SNR'].shape[0]):
        Green_name = GreenVus['SNR'][i]
        ra = GreenVus['_RAJ2000'][i]
        dec= GreenVus['_DEJ2000'][i]
        maj= GreenVus['MajDiam'][i]
        S_1GHz = GreenVus['S_1GHz_'][i]
        u_S_1GHz=GreenVus['u_S_1GHz_'][i]
        SpIndex =GreenVus['Sp-Index'][i]
        u_SpIndex=GreenVus['u_Sp-Index'][i]

        if u_S_1GHz=='?' or u_SpIndex=='?' or maj>180.: continue #i.e. throw out uncertain or diffuse data -- JEA's "Gold Standard"
        #if u_S_1GHz=='?' or u_SpIndex=='?': continue
        name.append(Green_name)
        expected.append(S_1GHz*(1.E9/145.E6)**(SpIndex))
        measured.append(GreenVus['Total_flux'][i])
        major.append(maj)
        c+=1
    print c, '/', GreenVus['SNR'].shape[0]


    expected = np.array(expected)
    measured = np.array(measured)
    major = np.array(major)
    """
    for j in range(len(measured)):
		if name[j] not in DubNames: pylab.plot(measured[j],expected[j],'go')
		else: pylab.plot(measured[j],expected[j],'ro')
	
	pylab.plot(measured,expected,'go')
	pylab.plot(np.arange(100),np.arange(100),'k-')
	pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$')
	pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$')
	pylab.xlim(0,60)
	pylab.ylim(0,600)
	pylab.show()
	pylab.close()
   
    for j in range(len(measured)):
    	if name[j] not in DubNames: pylab.scatter(measured[j],expected[j],s=major,c='green')
    	else: pylab.scatter(measured[j],expected[j],s=major,c='red')
    """
    pylab.scatter(measured,expected,s=major,c='green')
    pylab.show()
    pylab.close()
    """
    for j in range(len(measured)):
    	if name[j] not in DubNames: pylab.scatter(measured[j],expected[j],s=major,c='green')
    	else: pylab.scatter(measured[j],expected[j],s=major,c='red')
    """
    
    bound=40.#arcmins
    boundit=True
    if boundit:
    	pylab.scatter(measured[major>bound],expected[major>bound],s=2.*major[major>bound],c='white',label=r"$>\,20'$ diameter")
    	pylab.scatter(measured[major<bound],expected[major<bound],s=2.*major[major<bound],c='green',label=r"$<\,20'$ diameter")
    else: pylab.scatter(measured,expected,s=2.*major,c='green')
    pylab.plot(np.arange(100),np.arange(100),'k-')
    pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$ (Jy)',size=15)
    pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$ (Jy)',size=15)
    pylab.xlim(0,60)
    pylab.ylim(0,600)
    pylab.legend(loc='best',numpoints=1)
    pylab.show()
    pylab.close()

###############
chisquared=True
plotting=False
###############

if Paladini:
	"""
	Trying to minimize the chi-squared:

	chi^2 = | (Fmeas - Fexp)|^2/eFmeas^2 <-- is this the correct noise level to use?

	where the free parameter to sweep over is the 
	alpha in Fexpected=Fmeas*(2.7E9/145E6)^alpha
	"""


	hdulist=pyfits.open('../catalogs_matched/Paladini_vs_PyBDSM.fits')
	PalVus = hdulist[1].data

	interest_list = [0, 1, 8, 9, 16, 18, 19, 20, 32, 33, 42, 46, 49, 52, 53, 61, 67, 75, 78, 79, 80, 89, 92, 99, 103, 107, 108, 111, 113, 116, 123, 125, 126, 131, 132, 133, 141, 144, 149, 150, 152, 153, 154, 166, 167, 168, 170, 174, 176, 179, 180, 181, 184, 187, 188, 189, 191, 192, 199, 202, 203, 204, 212]

	expected = []
	e_expected=[]
	measured = []
	e_measured=[]
	diameter = []
	c=0

	chisq_master = []

	for i in range(PalVus['Gname'].shape[0]):
	
		chisq_indiv = []
	
		Pal_name = PalVus['Gname'][i]
		Source_id = PalVus['Source_id'][i]
		diam= PalVus['theta'][i]
		S_27GHz = PalVus['S2_7GHz'][i]
		eS_27GHz = PalVus['e_S2_7GHz'][i]
		#u_S_1GHz=PalVus['u_S_1GHz_'][i]
		#SpIndex =PalVus['Sp-Index'][i]
		#u_SpIndex=PalVus['u_Sp-Index'][i]

		#if u_S_1GHz=='?' or u_SpIndex=='?' or maj>5.: continue #i.e. throw out uncertain or diffuse data
		#if u_S_1GHz=='?' or u_SpIndex=='?': continue #i.e. throw out uncertain data
	
		if Source_id not in interest_list: continue
		
		if chisquared:
			for alpha in np.arange(-1.,1.,0.001):
				EXPC = S_27GHz*(2.7E9/145.E6)**(alpha)
				eEXPC = eS_27GHz*(2.7E9/145.E6)**(alpha)
				MEAS = PalVus['Total_flux'][i]
				eMEAS= PalVus['E_Total_flux'][i]
		
				#cSQ_nosig = np.absolute(MEAS - EXPC)**2.
				cSQ_sig = (np.absolute(MEAS - EXPC)**2.)/(eEXPC**2. + eMEAS**2.)
				chisq_indiv.append(cSQ_sig)
	
			chisq_master.append(chisq_indiv)
	
		#expected.append(S_27GHz*(2.7E9/145.E6)**(0.1))
		#e_expected.append(eS_27GHz*(2.7E9/145.E6)**(0.1))
		
		expected.append(S_27GHz*(2.7E9/145.E6)**(0.0))
		e_expected.append(eS_27GHz*(2.7E9/145.E6)**(0.0))
		measured.append(PalVus['Total_flux'][i])
		e_measured.append(PalVus['E_Total_flux'][i])
		diameter.append(diam)
		c+=1
	print c,'/',PalVus['Gname'].shape[0]


	expected = np.array(expected)
	measured = np.array(measured)
	major = np.array(diameter)
	if plotting:
		pylab.errorbar(measured,expected,xerr=e_measured,yerr=e_expected,fmt='yo')
		pylab.plot(np.arange(100),np.arange(100),'k-')
		pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$')
		pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$')
		pylab.xlim(0,150)
		pylab.ylim(0,150)
		pylab.show()
		pylab.close()

		pylab.scatter(measured,expected,s=diameter,c='yellow')
		pylab.show()
		pylab.close()

		pylab.errorbar(measured,expected,xerr=e_measured,yerr=e_expected,linestyle='None',c='black')
		pylab.scatter(measured,expected,s=5.*major,c='yellow')
		pylab.plot(np.arange(100),np.arange(100),'k-')
		pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$ (Jy)',size=15)
		pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$ (Jy)',size=15)
		pylab.xlim(0,150)
		pylab.ylim(0,150)
		pylab.show()
		pylab.close()
	
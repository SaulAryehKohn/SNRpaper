import pyfits
import numpy as np
import pylab

Green = True
Paladini = True

if Green:
    hdulist=pyfits.open('../catalogs_matched/Green_vs_PyBDSM.fits')
    GreenVus = hdulist[1].data
    expected = []
    measured = []
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

        #if u_S_1GHz=='?' or u_SpIndex=='?' or maj>5.: continue #i.e. throw out uncertain or diffuse data
        if u_S_1GHz=='?' or u_SpIndex=='?': continue
        expected.append(S_1GHz*(1.E9/145.E6)**(SpIndex))
        measured.append(GreenVus['Total_flux'][i])
        major.append(maj)
        c+=1
    print c


    expected = np.array(expected)
    measured = np.array(measured)
    major = np.array(major)
    """
    n, bins, patches = pylab.hist(expected/measured, 50, histtype='stepfilled')
    pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
    pylab.xlabel(r'Expected S$_{145\,\rm{MHz}}$ / Measured S$_{145\,\rm{MHz}}$',size=15)
    pylab.ylabel('Count',size=15)

    pylab.show()
    pylab.close()
    """
    pylab.plot(measured,expected,'bo')
    pylab.plot(np.arange(100),np.arange(100),'k-')
    pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$')
    pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$')
    pylab.xlim(0,60)
    pylab.ylim(0,600)
    pylab.show()
    pylab.close()

    pylab.scatter(measured,expected,s=major)
    pylab.show()
    pylab.close()

    pylab.scatter(measured,expected,s=major,c='green')
    pylab.plot(np.arange(100),np.arange(100),'k-')
    pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$')
    pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$')
    pylab.xlim(0,60)
    pylab.ylim(0,600)
    pylab.show()
    pylab.close()

if Paladini:
    hdulist=pyfits.open('../catalogs_matched/Paladini_vs_PyBDSM.fits')
    PalVus = hdulist[1].data
    expected = []
    measured = []
    diameter = []
    c=0
    for i in range(PalVus['Gname'].shape[0]):
        Pal_name = PalVus['Gname'][i]

        diam= PalVus['theta'][i]
        S_27GHz = PalVus['S2_7GHz'][i]
        #u_S_1GHz=PalVus['u_S_1GHz_'][i]
        #SpIndex =PalVus['Sp-Index'][i]
        #u_SpIndex=PalVus['u_Sp-Index'][i]

        #if u_S_1GHz=='?' or u_SpIndex=='?' or maj>5.: continue #i.e. throw out uncertain or diffuse data
        #if u_S_1GHz=='?' or u_SpIndex=='?': continue
        expected.append(S_27GHz*(2.7E9/145.E6)**(0.1))
        measured.append(PalVus['Total_flux'][i])
        diameter.append(diam)
        c+=1
    print c


    expected = np.array(expected)
    measured = np.array(measured)
    major = np.array(diameter)

    pylab.plot(measured,expected,'bo')
    pylab.plot(np.arange(100),np.arange(100),'k-')
    pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$')
    pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$')
    pylab.xlim(0,150)
    pylab.ylim(0,150)
    pylab.show()
    pylab.close()

    pylab.scatter(measured,expected,s=diameter)
    pylab.show()
    pylab.close()

    pylab.scatter(measured,expected,s=diameter,c='yellow')
    pylab.plot(np.arange(100),np.arange(100),'k-')
    pylab.xlabel(r'measured SNR S$_{145\,\rm{MHz}}$')
    pylab.ylabel(r'expected SNR S$_{145\,\rm{MHz}}$')
    pylab.xlim(0,150)
    pylab.ylim(0,150)
    pylab.show()
    pylab.close()

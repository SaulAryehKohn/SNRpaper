# Update 2015/4/14

import astropy
import aplpy
import numpy as np
import pylab as pl

# I think pyregion is kind of a stupid parser.  can't deal with the units of the circle radius or something?
#f = open('green_snr_catalog.reg','r')
#lines = f.readlines()
#f.close()
#for i in range(3,len(lines)):
#    lines[i] = lines[i].split('#')[0]+'\n'
#
#f = open('green_snr_catalog_for_aplpy.reg','w')
#f.writelines(lines)
#f.close()

# Green's catalog
hdu = astropy.io.fits.open('../data/green_snr_catalog_may2014_detailed.fits')
green = hdu[1].data
l_green = green['_Glon']
b_green = green['_Glat']
r_green = []
for i in range(len(l_green)):
    r_green.append(np.array([green['Dmaj'][i],green['Dmin'][i]]).max()/60.)
r_green = np.array(r_green)

good_radio = np.where((green['u_s_1ghz_'] != '?') * (green['u_alpha'] != '?'))[0]
bad_radio = np.where((green['u_s_1ghz_'] == '?') + (green['u_alpha'] == '?'))[0]

# The map
# Shit.  I didn't specify the right FITS header?
#if False:
map = aplpy.FITSFigure('../data/GalacticPlane747.fits',convention='calabretta')

map.show_grayscale(vmin=-2,vmax=7,invert=True)
map.show_contour(colors='red',levels=[5,10,15,20,25])
map.add_grid()
map.tick_labels.set_xformat('ddd.d')
map.tick_labels.set_yformat('ddd.d')
map.grid.set_xspacing(1)
map.grid.set_yspacing(1)
map.grid.show()
#map.show_circles(l_green[good_radio],b_green[good_radio],r_green[good_radio],edgecolor='lightgreen',linewidth=2)
#map.show_circles(l_green[bad_radio],b_green[bad_radio],r_green[bad_radio],edgecolor='lightgreen',linewidth=2,linestyle='--')
#map.show_regions('all_matches.reg')

for il,l in enumerate(np.arange(30,200-360,-15)):
    ll = l
    if (ll < 0):
        ll = 360+ll
    print ll
    map.recenter(l,0,width=15,height=15)
    map.save('../figs/GP_'+"{0:03d}".format(il)+'.png')

    #pl.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 06:42:53 2017

This script produces plots of HII distributions in galaxies. It uses 
standardized classes to read metadata, control data, and observation data.
It produces a single chart with three component plots.
    1) A histogram of HII regions radial bins from the galaxy center
    2) A plot of HII region density as a function of radial distance
    3) The two-dimensional distribution of HII regions
Current limitations include: only plotting data for a single galaxy at a time
and being limited to plane-of-sky (POS) coordinates (as opposed to galaxy
coordinates)


@author: Astronomy
"""
import pylab as pl
import numpy as np
import CatLIB001 as CL

drive="f:"

Target="M101"
TargetType="Galaxies"

HISTparams=CL.HII_plot_params(drive,Target,"POSHist")
DENSparams=CL.HII_plot_params(drive,Target,"POSDens")
LOCparams=CL.HII_plot_params(drive,Target,"POSLoc")
GXparams=CL.Galaxy_Parameters(drive,Target)
#print PLparams.RA2000,PLparams.DE2000
path=drive+"/Astronomy/Projects/Galaxies/"+Target+"/Imaging Data/Mapping/"
fn=HISTparams.DataFile
CatList=CL.Catalog_List(path+fn)
dr=(np.array(CatList.RAJ2000)-GXparams.RA2000)*60. #in arc minutes
dd=(np.array(CatList.DEJ2000)-GXparams.DE2000)*60 #in arc minutes
radii=np.sqrt(dr**2.+dd**2.)

nb=np.arange(HISTparams.X0,HISTparams.X1+1,HISTparams.DX)
hist=np.histogram(radii, bins=nb)
bin_centers=np.arange(1,HISTparams.X1+1,HISTparams.DX)
bin_areas=np.pi*((bin_centers+1)**2-(bin_centers-1)**2)
density=hist[0]/bin_areas
#print nb
#print bin_centers
#print "radii=",radii
#print hist[0]
#print bin_areas

#print "density=",density

pl.figure(figsize=(10., 4.), dpi=150, facecolor="white")
###############################################################################
ax = pl.subplot2grid((2, 5), (0, 0))
ax0 = pl.subplot2grid((2, 5), (0, 0), colspan=3)
#pl.subplot(2, 1, 1)
successC=CL.PlotHII(Target,radii,nb,HISTparams) 
###############################################################################
#pl.subplot(2, 1, 2)
ax1 = pl.subplot2grid((2, 5), (1, 0), colspan=3)
successC=CL.PlotHII(Target,bin_centers,density,DENSparams) 

###############################################################################
ax2 = pl.subplot2grid((2, 5), (0, 3), colspan=2, rowspan=2)
successC=CL.PlotHII(Target,dr,dd,LOCparams) 
###############################################################################
pl.subplots_adjust(left=0.06, bottom=0.09, right=0.98, top=0.95,
            wspace=0.4, hspace=0.3)
pl.savefig(path+Target+" H II Region Distribution.png",dpi=300)

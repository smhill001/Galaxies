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
import GalaxyLIB as GX

#Control Information
drive="f:"
Target="M101"
TargetType="Galaxies"

#Parameter Initialization
HISTparams=GX.HII_plot_params(drive,Target,"POSHist")
DENSparams=GX.HII_plot_params(drive,Target,"POSDens")
LOCparams=GX.HII_plot_params(drive,Target,"POSLoc")
GXparams=GX.Galaxy_Parameters(drive,Target)

#Reading observational data  and transforming the origin to the galactic center
path=drive+"/Astronomy/Projects/Galaxies/"+Target+"/Imaging Data/Mapping/"
fn=HISTparams.DataFile
DataList=GX.ObsDataList(path+fn)
dr=(np.array(DataList.RAJ2000)-GXparams.RA2000)*60. #in arc minutes
dd=(np.array(DataList.DEJ2000)-GXparams.DE2000)*60 #in arc minutes
radii=np.sqrt(dr**2.+dd**2.)

#Computing the distribution histogram and density as a function of radius
nb=np.arange(HISTparams.X0,HISTparams.X1+1,HISTparams.DX)
hist=np.histogram(radii, bins=nb)
bin_centers=np.arange(1,HISTparams.X1+1,HISTparams.DX)
bin_areas=np.pi*((bin_centers+1)**2-(bin_centers-1)**2)
density=hist[0]/bin_areas

#Set up the canvas for plotting
pl.figure(figsize=(10., 4.), dpi=150, facecolor="white")
###############################################################################
ax = pl.subplot2grid((2, 5), (0, 0))
ax0 = pl.subplot2grid((2, 5), (0, 0), colspan=3)
#pl.subplot(2, 1, 1)
successC=GX.PlotHII(Target,radii,nb,HISTparams) 
###############################################################################
#pl.subplot(2, 1, 2)
ax1 = pl.subplot2grid((2, 5), (1, 0), colspan=3)
successC=GX.PlotHII(Target,bin_centers,density,DENSparams) 

###############################################################################
ax2 = pl.subplot2grid((2, 5), (0, 3), colspan=2, rowspan=2)
successC=GX.PlotHII(Target,dr,dd,LOCparams) 
###############################################################################
pl.subplots_adjust(left=0.06, bottom=0.09, right=0.98, top=0.95,
            wspace=0.4, hspace=0.3)
pl.savefig(path+Target+" H II Region Distribution.png",dpi=300)

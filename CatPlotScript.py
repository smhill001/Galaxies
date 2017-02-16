# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 06:42:53 2017

@author: Astronomy
"""
import pylab as pl
import numpy as np
import CatLIB001 as CL

drive="f:"

Target="M81"
TargetType="Galaxies"
plotparams=CL.HII_plot_params(drive,Target)
print plotparams.RA2000,plotparams.DE2000
path=drive+"/Astronomy/Projects/Galaxies/"+Target+"/Imaging Data/Mapping/"
fn=plotparams.CatFile
CatList=CL.Catalog_List(path+fn)
dr=(np.array(CatList.RAJ2000)-plotparams.RA2000)*60. #in arc minutes
dd=(np.array(CatList.DEJ2000)-plotparams.DE2000)*60 #in arc minutes
radii=np.sqrt(dr**2.+dd**2.)

nb=np.arange(plotparams.X0,plotparams.X1+1,plotparams.DX)
hist=np.histogram(radii, bins=nb)
bin_centers=np.arange(1,plotparams.X1+1,plotparams.DX)
bin_areas=np.pi*((bin_centers+1)**2-(bin_centers-1)**2)
density=hist[0]/bin_areas
print nb
print bin_centers
#print "radii=",radii
print hist[0]
print bin_areas

print "density=",density
#pl.scatter(bin_centers,hist[0])
pl.figure(figsize=(4., 4.), dpi=150, facecolor="white")
pl.subplot(1, 1, 1)
pl.scatter(dr,dd)

pl.figure(figsize=(6.5, 4.), dpi=150, facecolor="white")
###############################################################################
pl.subplot(2, 1, 1)
successC=CL.PlotHist(Target,radii,nb,plotparams) 
###############################################################################
pl.subplot(2, 1, 2)
successC=CL.PlotPOSDensity(Target,bin_centers,density,plotparams) 
###############################################################################
pl.subplots_adjust(left=0.08, bottom=0.09, right=0.98, top=0.95,
            wspace=None, hspace=None)
pl.savefig(path+Target+" H II Region Distribution.png",dpi=300)

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 06:42:53 2017

@author: Astronomy
"""
import pylab as pl
import numpy as np
import CatLIB001 as CL

drive="f:"

Target="M101"
TargetType="Galaxies"
plotparams=CL.HII_plot_params(drive,Target)
print plotparams.RA2000,plotparams.DE2000
path=drive+"/Astronomy/Projects/Galaxies/"+Target+"/Imaging Data/Mapping/"
fn=plotparams.CatFile
CatList=CL.Catalog_List(path+fn)
dr=(np.array(CatList.RAJ2000)-plotparams.RA2000)*60. #in arc minutes
dd=(np.array(CatList.DEJ2000)-plotparams.DE2000)*60 #in arc minutes
radii=np.sqrt(dr**2.+dd**2.)

#Note: For M33 and other inclined galaxies, I need to account for the
#  inclination and the position angle so I'm not simply looking at the 
#  projected radius.

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

pl.figure(figsize=(6.5, 4.), dpi=150, facecolor="white")
pl.subplot(2, 1, 1)
#Plot Layout Configuration
x0=plotparams.X0
x1=plotparams.X1
xtks=x1/2+1

y0=plotparams.Y0
y1=plotparams.Y1

# Set x limits
pl.xlim(x0,x1)
# Set x ticks
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
# Set y limits
pl.ylim(y0,y1)
# Set y ticks
#pl.yscale('log')

pl.grid()
pl.tick_params(axis='both', which='major', labelsize=7)
pl.ylabel(r"$H$ $II$ $Region$ $(Count)$",fontsize=7)
#pl.xlabel(r"$Radius$ $(arcmin)$",fontsize=7)

pl.title("H II Region Distribution",fontsize=9)
#pl.plot(JupiterINT_20130612UT[:,0]/10.,JupiterINT_20130612UT[:,1]*0.60,label='INT_20130612UT',linewidth=1)
#pl.plot(JupiterDSK_20130612UT[:,0]/10.,JupiterDSK_20130612UT[:,1]*0.60,label='DSK_20130612UT',linewidth=0.5)
#pl.plot(JupiterRNG_20130612UT[:,0]/10.,JupiterRNG_20130612UT[:,1]*0.60,label='RNG_20130612UT',linewidth=0.5)
pl.hist(radii,bins=nb,color='r',label=Target)

#pl.scatter(WavelengthCenters,NetCountsArray,linewidth=0,label='Antares 20110809UT',color='r')
pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})

###############################################################################

pl.subplot(2, 1, 2)

y0=0
y1=1.5

# Set x limits
pl.xlim(x0,x1)
# Set x ticks
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
# Set y limits
pl.ylim(y0,y1)
# Set y ticks
#pl.yscale('log')

pl.grid()
pl.tick_params(axis='both', which='major', labelsize=7)
pl.ylabel(r"$H$ $II$ $Region$ $(Count-arcmin^{-2})$",fontsize=7)
pl.xlabel(r"$Radius$ $(arcmin)$",fontsize=7)

#pl.title("H II Region Distribution",fontsize=9)
#pl.plot(JupiterINT_20130612UT[:,0]/10.,JupiterINT_20130612UT[:,1]*0.60,label='INT_20130612UT',linewidth=1)
#pl.plot(JupiterDSK_20130612UT[:,0]/10.,JupiterDSK_20130612UT[:,1]*0.60,label='DSK_20130612UT',linewidth=0.5)
#pl.plot(JupiterRNG_20130612UT[:,0]/10.,JupiterRNG_20130612UT[:,1]*0.60,label='RNG_20130612UT',linewidth=0.5)
pl.scatter(bin_centers,density,color='r',label=Target)

#pl.scatter(WavelengthCenters,NetCountsArray,linewidth=0,label='Antares 20110809UT',color='r')
pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})

pl.subplots_adjust(left=0.08, bottom=0.09, right=0.98, top=0.95,
            wspace=None, hspace=None)

pl.savefig(path+Target+" H II Region Distribution.png",dpi=300)

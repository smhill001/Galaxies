# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 06:42:53 2017

@author: Astronomy
"""
import pylab as pl
import numpy as np
import CatLIB001 as CL


#M33
#path="F:/Astronomy/Projects/Galaxies/M33/Imaging Data/Mapping/"
#fn="HII_Tags01.csv"
#RA0=23.4625
#DE0=30.660277
#r1=41
#rbin=2
#Galaxy="M33"

#M81
#path="F:/Astronomy/Projects/Galaxies/M81/Imaging Data/"
#fn="Hill_H_II_Tags.csv"
#RA0=148.8875
#DE0=69.06583
#r1=21
#rbin=2
#Galaxy="M81"

#M101
path="F:/Astronomy/Projects/Galaxies/M101/Imaging Data/Mapping/"
fn="M101_H_II_Tags.csv"
RA0=210.8000
DE0=54.34861
r1=41
rbin=2
Galaxy="M101"

TestList=CL.Catalog_List(path+fn)
dr=(np.array(TestList.RAJ2000)-RA0)*60. #in arc minutes
dd=(np.array(TestList.DEJ2000)-DE0)*60 #in arc minutes
radii=np.sqrt(dr**2.+dd**2.)

#Note: For M33 and other inclined galaxies, I need to account for the
#  inclination and the position angle so I'm not simply looking at the 
#  projected radius.

nb=np.arange(0,r1,rbin)
hist=np.histogram(radii, bins=nb)
bin_centers=np.arange(1,r1,rbin)
bin_areas=np.pi*((bin_centers+1)**2-(bin_centers-1)**2)
density=hist[0]/bin_areas
print nb
print bin_centers
print hist[0]
print bin_areas

print "density=",density
#pl.scatter(bin_centers,hist[0])

pl.figure(figsize=(6.5, 4.), dpi=150, facecolor="white")
pl.subplot(2, 1, 1)
#Plot Layout Configuration
x0=0.
x1=r1-1.
xtks=x1/2+1

y0=0
y1=80

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
pl.hist(radii,bins=nb,color='r',label=Galaxy)

#pl.scatter(WavelengthCenters,NetCountsArray,linewidth=0,label='Antares 20110809UT',color='r')
pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})

pl.subplot(2, 1, 2)
#Plot Layout Configuration
x0=0.
x1=r1-1
xtks=x1/2+1

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
pl.scatter(bin_centers,density,color='r',label=Galaxy)

#pl.scatter(WavelengthCenters,NetCountsArray,linewidth=0,label='Antares 20110809UT',color='r')
pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})

pl.subplots_adjust(left=0.08, bottom=0.09, right=0.98, top=0.95,
            wspace=None, hspace=None)

pl.savefig(path+Galaxy+" H II Region Distribution.png",dpi=300)

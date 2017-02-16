# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 09:21:01 2017

This library is intended to read, manipulate and write astronomical 
    catalog information. Catalogs can be online or local ASCII and can
    be from professional references or locally generated, e.g., from Aladin.

@author: Astronomy
"""

class HII_plot_params:
    def __init__(self,drive,ObjIdentifierDD):
        #View has two options: raw or flux?
        self.ID=ObjIdentifierDD
        self.TargetType=''  #PN, ST, etc.
        self.RA2000=0.
        self.DE2000=0.
        self.X0=0.
        self.X1=0.
        self.DX=0.
        self.Y0=0.
        self.Y1=0.
        self.DY=0.
        self.Ytype=''  #log or linear
        self.CatFile='' #spectral model file.

        CfgFile=open(drive+'/Astronomy/Python Play/Galaxies/HIIPlotConfig.txt','r')
        CfgLines=CfgFile.readlines()
        CfgFile.close()
        nrecords=len(CfgLines)
        #print CfgLines

        for recordindex in range(1,nrecords):
            fields=CfgLines[recordindex].split(',')
            #print fields[0], fields[1]
            if fields[0] == ObjIdentifierDD:
                print "In first if, fields[1]",fields[:]
                self.TargetType=str(fields[1])
                self.RA2000=float(fields[2])
                self.DE2000=float(fields[3])
                self.X0=float(fields[4])
                self.X1=float(fields[5])
                self.DX=float(fields[6])
                self.Y0=float(fields[7])
                self.Y1=float(fields[8])
                self.DY=float(fields[9])
                self.Ytype=str(fields[10])
                self.CatFile=str(fields[11])

class Catalog_List:
    """
    Used by some custom PN spectra programs, e.g., *M57Spectrum20150913UT.py*,
    to obtain lists of ASCII input file for plotting. Meta-data on TargetID
    and Each FITS file
    self-identifies it's filter from the header meta-data and the 
    parameters of that filter with regard to photometry are then
    obtained by a table look up routine (list here)
    """
    def __init__(self,CatalogListFile):
#Object,Cont_Flag,RAJ2000,DEJ2000,X,Y,Label_Flag,Info        
        
        #The initial plan is to read ALL records in the observation list
        self.ObjectIdentifierDD=['']  #Keyword for source identification
        self.Cont_Flag=['']           #Unknowns
        self.RAJ2000=[0.0]            #RA of source in degrees
        self.DEJ2000=[0.0]            #DE of source in degrees
        self.X=[0.0]                  #Unknown
        self.Y=[0.0]                  #Unknown
        self.Label_Flag=['']          #Unknown
        self.Info=['']                #Free text comment/info
        self.NObs=0                   #Number of sources
        self.FirstTime=True
        
        CfgFile=open(CatalogListFile,'r')
        CfgLines=CfgFile.readlines()
        CfgFile.close()
        nrecords=len(CfgLines)
        #print CfgLines,nrecords

        for recordindex in range(1,nrecords):
            fields=CfgLines[recordindex].split(',')
            #print fields
            if self.FirstTime:
                self.ObjectIdentifierDD[0]=str(fields[0])
                self.Cont_Flag[0]=str(fields[1])
                self.RAJ2000[0]=float(fields[2])
                self.DEJ2000[0]=float(fields[3])
                self.X[0]=float(fields[4])
                self.Y[0]=float(fields[5])
                self.Label_Flag[0]=str(fields[6])
                self.Info[0]=str(fields[7])
                self.FirstTime=False
                self.NObs=1
            else:
                self.ObjectIdentifierDD.extend([str(fields[0])])
                self.Cont_Flag.extend([str(fields[1])])
                self.RAJ2000.extend([float(fields[2])])
                self.DEJ2000.extend([float(fields[3])])
                self.X.extend([float(fields[4])])
                self.Y.extend([float(fields[5])])
                self.Label_Flag.extend([str(fields[6])])
                self.Info.extend([str(fields[7])])
                self.NObs=self.NObs+1
                
def PlotHist(Target,radii,nb,plotparams):                
#Plot Layout Configuration
    import pylab as pl
    import numpy as np
    
    # Set x limits
    pl.xlim(plotparams.X0,plotparams.X1)
    # Set x ticks
    pl.xticks(np.linspace(plotparams.X0,plotparams.X1,plotparams.X1/2+1, endpoint=True))
    # Set y limits
    pl.ylim(plotparams.Y0,plotparams.Y1)
    # Set y ticks
    #pl.yscale('log')
    
    pl.grid()
    pl.tick_params(axis='both', which='major', labelsize=7)
    pl.ylabel(r"$H$ $II$ $Region$ $(Count)$",fontsize=7)
    
    pl.title("H II Region Distribution",fontsize=9)
    pl.hist(radii,bins=nb,color='r',label=Target)
    pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})        

    return 0        
    
def PlotPOSDensity(Target,bin_centers,density,plotparams): 
    import pylab as pl
    import numpy as np

    y0=0
    y1=1.5
    
    # Set x limits
    pl.xlim(plotparams.X0,plotparams.X1)
    # Set x ticks
    pl.xticks(np.linspace(plotparams.X0,plotparams.X1,plotparams.X1/2+1, endpoint=True))
    # Set y limits
    pl.ylim(y0,y1)
    # Set y ticks
    #pl.yscale('log')
    
    pl.grid()
    pl.tick_params(axis='both', which='major', labelsize=7)
    pl.ylabel(r"$H$ $II$ $Region$ $(Count-arcmin^{-2})$",fontsize=7)
    pl.xlabel(r"$Radius$ $(arcmin)$",fontsize=7)
    
    pl.scatter(bin_centers,density,color='r',label=Target)
    pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})
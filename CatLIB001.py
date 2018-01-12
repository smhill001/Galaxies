# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 09:21:01 2017

This library is intended to read, manipulate and write astronomical 
    catalog information. Catalogs can be online or local ASCII and can
    be from professional references or locally generated, e.g., from Aladin.

@author: Astronomy
"""

class Plot_Parameters:
     def __init__(self,drive,Identifier):
        """
        This is the BASE CLASS for 2D plot parameters.  ALL 2D plots
        posess at least an identifier, at type or intention, x and y axes,
        and data.
        
        SMH 1/11/18
        """
        self.ID=Identifier
        self.PlotType='' #Line plot, histogram, POS
        self.X0=0.
        self.X1=0.
        self.DX=0.
        self.Xtype='' #log or linear
        self.Y0=0.
        self.Y1=0.
        self.DY=0.
        self.Ytype=''  #log or linear
        self.DataFile='' #Data is in this file, or possible lists of data files


class Astrophysical_Parameters:
    def __init__(self,drive,TargetID):
        """
        This is the BASE CLASS for astrophysical object parameters.  ALL objects
        posess at least an identifier, object type and location.
        
        SMH 1/11/18
        """
    
        self.TargetID=TargetID
        self.TargetType=''  #PN, ST, etc.
        self.RA2000=0.0 #in degrees
        self.DE2000=0.0 #in degrees
        self.Distance=0.0 
        self.DistUnits='' #different for different scales: "AU", "LY" for now
        self.mV=0.0 #Visual band magnitude


class Galaxy_Parameters(Astrophysical_Parameters):
    """
    This class builds on the base class to add parameters specific to
    galaxies: position angle, inclination, and classification. Note that
    for other deep sky objects, in particular planetary nebulae, the 
    parameters would be identical or mostly identical. 
    
    SMH 1/11/18
    """
    def __init__(self,drive,TargetID):
        #View has two options: raw or flux?
        #Test_plot_params_base.__init__(self,drive,ObjIdentifierDD)
        self.PA=0.0 #degrees
        self.Inclination=0.0 #degrees
        self.classification='' #classification

        CfgFile=open(drive+'/Astronomy/Python Play/Galaxies/Galaxy_Parameters.txt','r')
        CfgLines=CfgFile.readlines()
        CfgFile.close()
        nrecords=len(CfgLines)
        #print CfgLines

        for recordindex in range(1,nrecords):
            fields=CfgLines[recordindex].split(',')
            #print fields[0], fields[1]
            if fields[0] == TargetID:
                print "In first if, fields[1]",fields[:]
                #self.TargetType=str(fields[1])
                self.TargetID=fields[0]
                self.TargetType=fields[1]
                self.RA2000=float(fields[2])
                self.DE2000=float(fields[3])
                self.Distance=float(fields[4])
                self.DistUnits=fields[5]
                self.mV=float(fields[6])


class HII_plot_params(Plot_Parameters):
    """
    This class builds on the base class to add parameters specific to
    HII plots. In this case, there are no additions, just the code to
    populate the object.
    
    SMH 1/11/18
    """
    def __init__(self,drive,PlotID,PlotType):
        #View has two options: raw or flux?

        self.ID=PlotID

        CfgFile=open(drive+'/Astronomy/Python Play/Galaxies/HIIPlotConfig.txt','r')
        CfgLines=CfgFile.readlines()
        CfgFile.close()
        nrecords=len(CfgLines)
        #print CfgLines

        for recordindex in range(1,nrecords):
            fields=CfgLines[recordindex].split(',')
            #print fields[0], fields[1]
            if fields[0] == PlotID:
                if fields[1] == PlotType:
                    print "In first if, fields[1]",fields[:]
                    self.PlotType=str(fields[1])
                    self.X0=float(fields[2])
                    self.X1=float(fields[3])
                    self.DX=float(fields[4])
                    self.Xtype=str(fields[5])
                    self.Y0=float(fields[6])
                    self.Y1=float(fields[7])
                    self.DY=float(fields[8])
                    self.Ytype=str(fields[9])
                    self.DataFile=str(fields[10])

class Catalog_List:
    """
    This class is the container for a list of objects taken from an ASCII
    catalog. In this case, it is configured to read a list of HII regions 
    that have been manually tagged in Aladin. It needs to be extended to 
    read from professional catalogs, either as exported by Aladin or directly
    from the Web.
    
    Another addition here could be photometric data for HII regions. 
    
    Finally, even this class has a lot in common with the galaxy meta-data
    class above. Together they are candidates for consolidation into a master
    class.
    
    SMH 1/9/18
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
                
def PlotHII(Target,X_data,Y_data,plotparams):                
#Plot Layout Configuration
    import pylab as pl
    import numpy as np
    
    pl.grid()
    pl.xlim(plotparams.X0,plotparams.X1)
    pl.xticks(np.arange(plotparams.X0,plotparams.X1+.000001,plotparams.DX))
    pl.ylim(plotparams.Y0,plotparams.Y1)
    pl.yticks(np.arange(plotparams.Y0,plotparams.Y1+.000001,plotparams.DY))  
    pl.tick_params(axis='both', which='major', labelsize=7)
    
    pl.title("H II Radial Distribution",fontsize=9)
    if plotparams.PlotType == "POSHist":
        pl.hist(X_data,bins=Y_data,label=Target)
        pl.ylabel(r"$H$ $II$ $Region$ $(Count)$",fontsize=7)
    elif plotparams.PlotType == "POSDens":
        p=pl.plot(X_data,Y_data,label=Target,marker='.',linewidth=1.0)
        pl.xlabel(r"$Radius$ $(arcmin)$",fontsize=7)
        pl.ylabel(r"$H$ $II$ $Region$ $(Count)$",fontsize=7)
        print "COLOR=",p[0].get_color()

    elif plotparams.PlotType == "POSLoc":
        pl.xlabel(r"$Delta$ $RA$ $(arcmin)$",fontsize=7)
        pl.ylabel(r"$Delta$ $DE$ $(arcmin)$",fontsize=7)
        pl.title("H II Location Distribution",fontsize=9)
        pl.scatter(X_data,Y_data,label=Target,marker='o',edgecolor="#1f77b4",
                   linewidth =1.0,facecolor="") 
        
    pl.legend(loc=1,ncol=2, borderaxespad=0.,prop={'size':6})        

    return 0        


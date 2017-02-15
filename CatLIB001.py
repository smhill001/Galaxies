# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 09:21:01 2017

This library is intended to read, manipulate and write astronomical 
    catalog information. Catalogs can be online or local ASCII and can
    be from professional references or locally generated, e.g., from Aladin.

@author: Astronomy
"""

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
                
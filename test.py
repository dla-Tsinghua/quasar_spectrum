#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:38:05 2019

@author: samwang
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import sympy
from astropy.io import fits
from matplotlib.pyplot import MultipleLocator

f = open('100quasar.txt','r')
line = f.readline()
data_list = []
while line:
    num = list(map(str,line.split()))
    #num.astype(int)
    if len(num[2])<4:
        num[2]='0'+num[2]
    data_list.append(num)
    line = f.readline()
f.close()

data_array=np.array(data_list)
n=len(data_array)
i=0
#a=0
#b=600

for i in range(0,n):
    x=data_array[i][0]
    y=data_array[i][1]
    w=data_array[i][2]
    if len(w)<4:
        w='0'+w
    print(x,y,w)
    hdu=fits.open('fits/spec-%s-%s-%s.fits'%(x,y,w))

    #hdu.info()

    flux=hdu[1].data['flux']
    loglam=hdu[1].data['loglam']
    lam=10**loglam
    z=hdu[2].data['Z']
    dla=1216*(1+z)

    a=0
    b=200
    while True:
        if b>np.max(flux):
            break
        else:
            b=b+100
    
    model=hdu[1].data['model']
    NV=1240*(1+z)
    CIV=1549*(1+z)
    HeII=1640*(1+z)
    CIII=1908*(1+z)
    MgII=2799*(1+z)
    plt.figure(figsize=(18,10))
    plt.xlabel('Wavelength'+'['+'$\AA$'+']',fontsize=18)
    plt.ylabel('Flux[$\mathregular{(10)^-17}$erg/$\mathregular{(cm)^2}$/s/'+'$\AA$'+']',fontsize=18)
    plt.xlim(3500,10500)
    plt.ylim(a,b)
    plt.tick_params(axis='both',which='major',labelsize=16)
    x_major_locator=MultipleLocator(500)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    plt.title('spec-%s-%s-%s.fits'%(x,y,w),fontdict=None,loc='center',pad='20',fontsize=30,color='blue')
    plt.grid()
    plt.plot(lam,flux,label='flux',c='black')
    plt.plot(lam,model,label='model',c='red')
    plt.legend(bbox_to_anchor=(0.88,1.02,10,20), loc=3,ncol=1, mode=None, borderaxespad=0,fontsize=18)
    plt.axvline(x=dla,ls="-",c="blue",linewidth=2)
    plt.text(dla,b-40,'Ly-'+'$\\alpha$',fontsize=25,color='green')
    plt.axvline(x=NV,ls="-",c="blue",linewidth=2)
    plt.text(NV,b-80,'N V 1240',fontsize=25,color='green')
    plt.axvline(x=CIV,ls="-",c="blue",linewidth=2)
    plt.text(CIV,b-40,'C IV 1549',fontsize=25,color='green')
    plt.axvline(x=HeII,ls="-",c="blue",linewidth=2)
    plt.text(HeII,b-80,'He II 1640',fontsize=25,color='green')
    plt.axvline(x=CIII,ls="-",c="blue",linewidth=2)
    plt.text(CIII,b-40,'C III 1908',fontsize=25,color='green')
    plt.axvline(x=MgII,ls="-",c="blue",linewidth=2)
    plt.text(MgII,b-40,'Mg II 2799',fontsize=25,color='green')
    #plt.show()
    plt.savefig('./spec-1/spec-%s-%s-%s.png'%(x,y,w),dpi=400)
    plt.show()
    print('spec-%s-%s-%s.png has saved'%(x,y,w))

    #plt.figure(figsize=(18,10))
    #plt.xlabel('Wavelength'+'['+'$\AA$'+']',fontsize=18)
    #plt.ylabel('Flux[$\mathregular{(10)^-17}$erg/$\mathregular{(cm)^2}$/s/'+'$\AA$'+']',fontsize=18)
    #plt.tick_params(axis='both',which='major',labelsize=16)
    #x_major_locator=MultipleLocator(100)
    #ax=plt.gca()
    #ax.xaxis.set_major_locator(x_major_locator)
    #plt.title('Ly-'+'$\\alpha$'+'-%s-%s-%s'%(x,y,w),fontdict=None,loc='center',pad='20',fontsize=30,color='blue')
    #plt.plot(lam,flux,label='flux',c='black')
    #plt.plot(lam,model,label='model',c='red')
    #plt.legend(bbox_to_anchor=(0.88,1.02,10,20), loc=3,ncol=1, mode=None, borderaxespad=0,fontsize=18)
    #plt.axvline(x=dla,ls="-",c="blue",linewidth=2)
    #plt.text(dla,b-40,'Ly-'+'$\\alpha$',fontsize=25,color='green')
    #plt.xlim(dla-500,dla+500)
    #plt.ylim(a,b)
    #plt.savefig('./ly-a/Ly-a-%s-%s-%s.png'%(x,y,w),dpi=400)
    #plt.show()
    #print('Ly-a-%s-%s-%s.png has saved'%(x,y,w))
    
    i=i+1
    #download(x,y,z)
 
    #g.write('curl -o spec-%s-%s-%s.fits https://dr14.sdss.org/sas/dr14/eboss/spectro/redux/v5_10_0/spectra/lite/%s/spec-%s-%s-%s.fits\n'%(x,y,z,x,x,y,z) )
    #i=i+1


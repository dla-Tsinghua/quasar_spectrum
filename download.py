#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:12:03 2019

@author: samwang
"""

import numpy as np
f = open('100quasar.txt','r')
g = open('get.sh', 'w')
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
for i in range(0,n):
    x=data_array[i][0]
    y=data_array[i][1]
    z=data_array[i][2]
    if len(z)<4:
        z='0'+z
    #download(x,y,z)
    g.write('curl -o spec-%s-%s-%s.fits https://dr14.sdss.org/sas/dr14/eboss/spectro/redux/v5_10_0/spectra/lite/%s/spec-%s-%s-%s.fits\n'%(x,y,z,x,x,y,z) )
    i=i+1
g.close()
    
    
#def download(x,y,z):
    #return "https://dr14.sdss.org/sas/dr14/eboss/spectro/redux/v5_10_0/spectra/lite/%s/spec-%s-%s-%s.fits".format(x,x,y,z)
#https://dr14.sdss.org/sas/dr14/eboss/spectro/redux/v5_10_0/spectra/lite/4219/

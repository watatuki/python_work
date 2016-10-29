#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import difflib

SrcPatchList = glob.glob('bsp-repo/*.patch')
DiffPatchListA = glob.glob('mainline-update/*.patch')
DiffPatchListB = glob.glob('ltsipatch/*.patch')

SrcPatchList.sort()

DiffPatchListA.sort()
DiffPatchListB.sort()
DiffPatchList = DiffPatchListA + DiffPatchListB

srcnum = len(SrcPatchList)
diffnum = len(DiffPatchList)

for i in range(srcnum):
    fs = open(SrcPatchList[i])
    base = fs.readlines()
    fs.close()
    
    match = 0 
    #print "調査中, %s" % SrcPatchList[i]
    
    #先頭4行は無視
    base[0] = ""
    base[1] = ""
    base[2] = ""
    base[3] = ""
    
    for j in range(diffnum):
        fd = open(DiffPatchList[j])
        dif = fd.readlines()
        fd.close()
        
        #先頭4行は無視
        dif[0] = ""
        dif[1] = ""
        dif[2] = ""
        dif[3] = ""
        
        point = difflib.SequenceMatcher(None,base,dif).ratio()
        
        if point == 1 :
            print "一致, %s , %s " % (SrcPatchList[i],DiffPatchList[j])
            match = 1

    if match == 0 :
        print "一致なし、%s" % SrcPatchList[i]
       


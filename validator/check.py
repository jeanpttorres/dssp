#!/usr/bin/env python
# This code is part of DSSP and DSSSP project developed by Jean P. Tremeschin and Edna Hoshino
# This code checks the solution values: dc and df 
#
import sys
import math

def dH(s,t):
    n = len(t)    
    if len(s) != n:
        raise Exception("lenght must be equal!")
    dif = 0
    for i in range(0,n):
        if s[i] != t[i]:
           dif += 1
    return dif

def bestSim(s,t):
    n = len(t)
    m = len(s)
    if m < n:
        raise Exception("m < n")
    minDif = n
    pos = 0
    for k in range(0,m-n+1):
        dif = dH(s[k:k+n],t)
        if dif < minDif:
            minDif = dif
            pos = k
    return (minDif,pos)

def bestDif(s,t):
    n = len(t)
    m = len(s)
    if m < n:
        raise Exception("m < n")
    maxDif = -1
    pos = 0
    for k in range(0,m-n):
        dif = dH(s[k:k+n],t)
        if dif > maxDif:
            maxDif = dif
            pos = k
    return (maxDif,pos)

def computeDc(S,t):
    dc = 0
    j = 0
    l = []
    for s in S:
        minDif,pos = bestSim(s,t)
        if minDif > dc:
            dc = minDif
            j = s
        l.append( (minDif,pos) )
    return (dc,j,l)

def computeDf(S,t):
    df = len(t)
    j = 0
    l = []
    for s in S:
        minDif,pos = bestSim(s,t)
        if minDif < df:
            df = minDif
            j = s
        l.append( (minDif,pos) )
    return (df,j,l)

def readSol(solf, solname):
    dc = -1
    df = -1
    s = None
    for line in solf :
        if line.startswith("dc = "):
            dc = int(line[5:-1])
        elif line.startswith("df = "):
            df = int(line[5:-1])
        elif line.startswith("Target String(x) = "):
            s = line[19:-1]
    if dc == -1 or df == -1 or s is None :
       print("Erro ao ler arquivo %s, dc=%d, df=%d, sol=%s" % (solname, dc, df, s) ) 
    return (dc, df, s)

def readInst(instf, instname):
    nsc = -1
    nsf = -1
    n = -1
    alfa = -1
    aux = instf.readline()
    alfa = int(aux[:-1])
    aux = instf.readline()
    pieces = aux.split(" ")
    nsc = int(pieces[0])
    nsf = int(pieces[1][:-1])
    aux = instf.readline()
    n = int(aux[:-1])
    # discard unused line and symbols line
    instf.readline()
    for i in range(0,alfa) :
        instf.readline()
    Sc = []
    Sf = []
    for i in range(0,nsc):
        aux = instf.readline()[:-1]
        if len(aux) != n:
            print("Error, string from sc of wrong size: %s should have %d chars" % (aux, n) )
        Sc.append(aux)
    for i in range(0,nsf):
        aux = instf.readline()[:-1]
        if len(aux) != n:
            print("Error, string from sf of wrong size: %s should have %d chars" % (aux, n) )
        Sf.append(aux)
    return (Sc, Sf, n)

def check(solname, instname, Sc, Sf, n, expdc, expdf, t):
    dc,jc,lc = computeDc(Sc, t)
    df,jf,lf = computeDf(Sf, t)
    res = True
    if dc != expdc:
        print("Error sol=%s, inst=%s, expected dc=%d, computed dc=%d" % (solname, instname, expdc, dc) )
        print("j=%s l=%s" % (jc,lc) )
        res = False
    
    if df != expdf:
        print("Error sol=%s, inst=%s, expected df=%d, computed df=%d" % (solname, instname, expdf, df) )
        print("j=%s l=%s" % (jf,lf) )
        res = False
    return res

def print_mode():
    sys.stderr.write("Args: [instance-file-name] [solution-file-name].\n")
    sys.exit(1)

# main
if len(sys.argv) < 3:
    sys.stderr.write("Missing mode.\n")
    print_mode()
    
instf = open(sys.argv[1], "r")
solf = open(sys.argv[2], "r")
Sc, Sf, n = readInst(instf, sys.argv[1])
dc, df, s = readSol(solf, sys.argv[2])
res = check(sys.argv[1], sys.argv[2], Sc, Sf, n, dc, df, s)
print("Check test on %s resulted %s" % (sys.argv[2],res))
if not res :
    print("When stopped due to time limit, False indicates there exists a better solution not found by the solver.")


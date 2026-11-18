import numpy as np
N=121;g=np.zeros((N,N),int);g[40,40]=12000;g[40,80]=12000;g[80,60]=12000
while g.max()>=4:
    t=g//4;g%=4
    g[1:]+=t[:-1];g[:-1]+=t[1:];g[:,1:]+=t[:,:-1];g[:,:-1]+=t[:,1:]
cols=["#1a1410","#3f7d4a","#e3c14a","#d9573f"]
r=''.join(f'<rect x="{i*4}" y="{j*4}" width="4" height="4" fill="{cols[g[j,i]]}"/>' for j in range(N) for i in range(N))
open('sp3.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N*4} {N*4}">{r}</svg>')

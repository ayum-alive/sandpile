import numpy as np
N=181;g=np.zeros((N,N),int);g[60,60]=12000;g[60,120]=12000;g[120,90]=12000
while g.max()>=4:
    t=g//4;g%=4
    g[1:]+=t[:-1];g[:-1]+=t[1:];g[:,1:]+=t[:,:-1];g[:,:-1]+=t[:,1:]
cols=["#1a1410","#3f7d4a","#e3c14a","#d9573f"]
r=''.join(f'<rect x="{i*3}" y="{j*3}" width="3" height="3" fill="{cols[g[j,i]]}"/>' for j in range(N) for i in range(N))
open('sp3b.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {N*3} {N*3}">{r}</svg>')

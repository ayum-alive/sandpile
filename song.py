import numpy as np
from midiutil import MIDIFile
N=121;g=np.zeros((N,N),int);g[N//2,N//2]=30000
while g.max()>=4:
    t=g//4;g%=4
    g[1:]+=t[:-1];g[:-1]+=t[1:];g[:,1:]+=t[:,:-1];g[:,:-1]+=t[:,1:]
sc=[0,2,4,7,9]
m=MIDIFile(1);m.addTempo(0,0,132);m.addProgramChange(0,0,0,11);m.addProgramChange(0,1,0,42)
t=0
for row in range(10,111,2):
    line=g[row,10:111:4]
    for j,v in enumerate(line[:16]):
        n=60+sc[(int(v)+j)%5]+12*(int(v)>=2)
        m.addNote(0,0,n,t+j*0.25,0.25,70+10*int(v))
    m.addNote(0,1,36+sc[(row//2)%5],t,4,60)
    t+=4
m.writeFile(open('sp.mid','wb'))

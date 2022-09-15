alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = "ddz=z="
for i in alp:
    a=a.replace(i,'*')
print(a)

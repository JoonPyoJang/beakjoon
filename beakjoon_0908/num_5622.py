a = input()
ret = 0
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for j in a:
    for i in dial:
        if j in i:
            ret += dial.index(i) +3
    
print(ret)
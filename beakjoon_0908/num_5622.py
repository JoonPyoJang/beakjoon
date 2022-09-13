# a = input()
time = 0
a = "UNUCIC"
def num_find(str_):
    out = 0
    if str_=='A' or str_=='B' or str_=='C':
        out = 3
    elif str_=='D' or str_=='E' or str_=='F':
        out = 4
    elif str_=='G' or str_=='H' or str_=='I':
        out = 5
    elif str_=='J' or str_=='K' or str_=='L':
        out = 6
    elif str_=='M' or str_=='N' or str_=='O':
        out = 7
    elif str_=='P' or str_=='Q' or str_=='R' or str_=='S':
        out = 8
    elif str_=='U' or str_=='T' or str_=='V':
        out = 9
    elif str_=='W' or str_=='X' or str_=='Y' or str_=='Z':
        out = 10
    return out
    
for i in a:
    time += num_find(i)
    

print(time)
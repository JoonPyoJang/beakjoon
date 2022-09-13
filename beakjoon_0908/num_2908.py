a,b = input().split()

revered_a = int(a[::-1])
revered_b = int(b[::-1])

if revered_a>revered_b:
    print(revered_a)
else:
    print(revered_b)
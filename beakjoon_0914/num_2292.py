#1로 시작하여 6*1 증가 후 6*2 증가 후 6*3 증가 후 6*4 이런식으로 계속 늘어난다.

n = int(input())

num_comb = 1
cnt = 1 #증가하는 값
while n > num_comb:
    num_comb += cnt*6  
    cnt += 1
print(cnt)


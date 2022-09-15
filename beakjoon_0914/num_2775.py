# a층의 b호에 살려면 자신의 아래 층의 1호부터 b호까지 사람들의 수의 합만큼 
# 데려와 살아야함
# a-1 층의 1호부터 b호까지 사람들의 수의 합
# 0층의 i 호에는 i 명이 산다.
# 0층 1호에 1명 2호에 2명 3호에 3명 1층 1호에 1명 2호에 3명 3호에 6명 3층 1호에 2명 2호에 

# 3층 4호
n = int(input())


for _ in range(n):
    h = int(input())
    w = int(input())+1
    list_ = list(range(w))
    count = 1
    for n in range(h):
        for i in range(1,w):
            list_[i] = list_[i-1] + list_[i]
            
        count += 1

    print(list_[w-1])



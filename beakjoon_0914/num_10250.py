#호텔 객실 채우기
#호텔에 가로 방수와 층수를 받아 손님을 차례대로 받는다
#손님을 받을 때에는 1호 즉 101호부터 받으며 201, 301, 401 순으로 받는다
#{층수자리}'0'{호수자리} 층이 20층이고 손님이 21번째부터 2호수
#{(손님수)%(호수자리 나머지)}'0'{(손님수)/(호수자리)}나머지가 있으면 올림
# 
import math
n = int(input()) #돌아가는 횟수
for _ in range(n):
    list_ = ''
    h,w,n = map(int, input().split())

    num = n//h +1
    floor = n%h
    if n%h==0:
        floor = h
    print(f"{floor*100+num}")

    


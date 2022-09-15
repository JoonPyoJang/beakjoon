# 낮에 올라가는 길이 a 밤에 미끄러지는 길이 b 정상까지 c

# 만약 (a-b)*날짜 = c
import math
# math 함수 내 올림 버림
# math.ceil(i) : 올림
# math.floor(i) : 내림
# math.trunc(i) : 버림

a,b,c = map(int, input().split())

date = math.ceil((c-a)/(a-b))+1


print(date)
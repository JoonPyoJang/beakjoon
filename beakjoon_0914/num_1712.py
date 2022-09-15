#손익 분기점 구하기
#고정 비용 A 가변비용 B 판매 수익 C 라고 가정을 했을때 손익 분기점 구하기
# C*(판매 수량) - A - B*(판매 수량) = 양수가 되어야 손익분기점
#손익 분기점이 존재하지 않는 경우 = B > C



a,b,c = map(int,input().split())
b_c = c - b


if b_c > 0:
    count = int(a/b_c)
    if count*b_c <= a:
        count +=1
else:
    count = -1

print(count)
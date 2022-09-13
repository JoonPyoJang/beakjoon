# 문자가 일치하지 않을때 문자를 저장하고 그 문자를 리스트에 저장 후 초기화
# 문자가 바뀌는지 확인 뒤에 문자를 저장하고 같으면 pass 아니면 확인작업
# 확인작업 : list를 만들어 값이 바껴 저장할때마다 list를 추가
# 하고 확인 문자가 리스트에 있으면 break 나 return으로 빠져나온다
# for 문이 끝나면 count +

n = int(input())
count = 0

for i in range(n):
    word = input()
    compare = ""
    make_list = []
    for j in word:
        if compare != j:
            if j not in make_list:
                make_list.append(j)
                compare = j
            else:
                count += 1
                break
                
    

print(n-count)
            
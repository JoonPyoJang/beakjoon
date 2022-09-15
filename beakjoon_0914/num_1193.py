# 숫자를 받아서 숫자만큼 for 문을 돌림
# 입력받은 숫자의 line 줄과 줄에 해당하는 번호가 몇번째인지 구함
# 몇번째인지는 증가하는 line 의 합
# 계속 더했을때 입력받은 번호수를 지나기 때문에 line 과 수를 빼서 따로 저장
# 따로 저장해서 나중에 for 문 분수나 분모 시작 숫자가 될 예정
# 저장된 숫자에서 짝수면 분모부터 홀수면 분자부터
# 이후 for 문에서 입력받은 숫자-gap 만큼 돌아가게 하는데 
# 짝수일때는 분자 증가 홀수일때는 분자 감소

# 분모 시작 숫자 필요함, count 수


n = int(input())
line = 0
start_num = 0
while n > start_num:
    line += 1
    start_num += line


gap = start_num - line
run = n - gap
print(line, start_num, gap, run)
for i in range(run):
    if line%2 == 0:
        num = i +1
        den = line - i
    else:
        num = line - i
        den = i +1
    print(f"{num}/{den}")









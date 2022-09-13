# a-z까지 알파벳을 비교하여 있으면 리스트에 리스트 번호 쓰고 없으면 -1

import sys
#a-z까지 리스트 생성
az_list = ""
send_list = []
for i in range(97, 123):
    az_list +=chr(i)
    send_list.append(-1)

text_ = input()
for i,j in enumerate(text_):

    result = az_list.find(j)

    if send_list[result]==-1:
        send_list[result] = i

result1 = ' '.join(map(str,send_list))
print(result1)

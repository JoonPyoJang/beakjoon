#대소문자 구분하지 않기 -> 만약 대문자로 입력했을때 32를 더 하면 소문자로 나옴 
#가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램

# a = input().upper()

# def num_count(list_):
#     num1=0
#     for i in list_:
#         num2 = list_.count(i)
#         if num1 == num2 and list_[list_point] != i:
#             return '?'
#         elif num1 < num2:
#             num1 = num2
#             list_point = list_.find(i)
#     return list_[list_point]

# print(num_count(a))


words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
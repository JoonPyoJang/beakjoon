#대소문자 구분하지 않기 -> 만약 대문자로 입력했을때 32를 더 하면 소문자로 나옴 
#가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램



a = input()

def num_change(a):
    list_ = ""
    for i in a:
        if ord(i) > 92:
            list_ += chr(ord(i)-32)
        else :
            list_ += i
    return list_

def num_count(list_):
    num1=0
    for i in list_:
        num2 = list_.count(i)
        if num1 == num2 and list_[list_point] != i:
            return '?'
        elif num1 < num2:
            num1 = num2
            list_point = list_.find(i)
    return list_[list_point]


list_ = num_change(a)
print(num_count(list_))


a = int(input())

for _ in range(a):
    num,list_ = input().split(" ")
    text_ = ""
    for i in list_[:20]:
            text_ += i*int(num)
    print(text_)

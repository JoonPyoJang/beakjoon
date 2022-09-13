import sys

num = int(sys.stdin.readline())
list_ = str(sys.stdin.readline())
total = 0

for i in range(num):
    total += int(list_[i])
print(total)



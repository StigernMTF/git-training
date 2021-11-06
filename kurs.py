a = int(input())
b = int(input())
while a > 0 and b > 0: # Комментарий(пробный)
    if a < b or a > b:
        print(a*b)
        exit(0)
    elif a == b:
        print(a)
        exit(0)
else:
    print('error')
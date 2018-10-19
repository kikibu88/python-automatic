x = input("구구단을 출력할 숫자를 입력하세요(2~9) :  ")
x = int(x)
for y in range(1,10):
    # print (type(x))
    print(x * y, end=' ')
    print(type(x))
    print(type(y))
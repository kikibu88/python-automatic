x = int(input ("Pleaseenter an integer: "))

if x < 0:
    x = 0
    print('입력값이음수라서0으로 치환')
elif x == 0:
    print('0')
elif x == 1:
    print('1')
else:
    print('1 이상')



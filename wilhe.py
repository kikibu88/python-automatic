s = 'supercalifragilisticexpialidociousz'
len_s = len(s)
count = 0

while True:
    input_char = input("세어보기 원하는 알파벳 입력: ")
    for index in range(0, len_s):
        s_char = s[index]
        if input_char == s_char:
            count = count + 1

    if count == 0:
        print("없는 문자이니 다시 입력하세요")
        continue

    break

print("입력된 문자 = %c 이고 몇개가 들어있나? %d개" %(input_char, count))

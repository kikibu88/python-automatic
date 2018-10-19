def count_char(s, input_char):
    len_s = len(s)
    count = 0

    while True:
        for index in range(0, len_s):
            s_char = s[index]
            if input_char == s_char:
                count = count + 1
        break

    return count

s = 'supercalifragilisticexpialidociousz'
input_char = 'a'
a = count_char(s, input_char)
print("입력된 문자 = %c 이고 몇개가 들어있나? %d개" %(input_char, a))

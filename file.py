f= open('구구단.xlsx', 'w')

for table in range(2,10):
    table_name = "*** " + str(table) + "단" + " ***" + "\n"
    f. write(table_name)

    for num in range(1,10):
        table_line = str(table) + '*' + str(num) + '=' + str(table * num) + '\n'
        f. write(table_line)

f.close()

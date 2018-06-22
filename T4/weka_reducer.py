def count(input):
    i = open(arg.input,'r')

    end = False
    number_lst = []

    line_count = 0
    while not end:
        line = i.readline()
        if not line == '':
            line = line.replace('\n','')
            line = line.replace(' ','')
            if len(line) == 1:
                number_lst.append((int(line),line_count))
        else:
            end = True
        line_count += 1

    close(i)

    n0 = 0, n1 = 0, n2 = 0, n3 = 0, n4 = 0, n5 = 0, n6 = 0, n7 = 0, n8 = 0, n9 = 0
    for i in range(len(number_lst)):
        if number_lst[i][0] == 0:
            n0 += 1
        elif number_lst[i][0] == 1:
            n1 += 1
        elif number_lst[i][0] == 2:
            n2 += 1
        elif number_lst[i][0] == 3:
            n3 += 1
        elif number_lst[i][0] == 4:
            n4 += 1
        elif number_lst[i][0] == 5:
            n5 += 1
        elif number_lst[i][0] == 6:
            n6 += 1
        elif number_lst[i][0] == 7:
            n7 += 1
        elif number_lst[i][0] == 8:
            n8 += 1
        elif number_lst[i][0] == 9:
            n9 += 1

def reduce(input):
    lst = count(input)

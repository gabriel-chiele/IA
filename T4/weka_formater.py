def formater(input, output, n):
    i = open(input,'r')
    o = open(output,'w')

    o.write('@RELATION Weka\n')
    o.write('\n')

    for j in range(1024):
        o.write('@ATTRIBUTE bnr%i	numeric\n' % j)

    o.write('@ATTRIBUTE class 	{0,1,2,3,4,5,6,7,8,9}\n')
    o.write('\n')
    o.write('@DATA\n')

    end = False
    str = ''

    first = True
    number = 0
    n0 = 0
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    n7 = 0
    n8 = 0
    n9 = 0
    while not end:
        line = i.readline()
        if not line == '':
            line = line.replace('\n','')
            line = line.replace(' ','')
            if not len(line) == 1:
                lst = list(line)
                new_line = ''
                for k in range(len(lst)):
                    if k == 0 and first:
                        first = False
                        new_line = lst[k]
                    else:
                        new_line = new_line + ',' + lst[k]
                str = str + new_line
            else:
                str = str + ',' + line + '\n'
                number = int(line)
                if number == 0 and n0 < n:
                    n0 += 1
                    o.write(str)
                elif number == 1 and n1 < n:
                    n1 += 1
                    o.write(str)
                elif number == 2 and n2 < n:
                    n2 += 1
                    o.write(str)
                elif number == 3 and n3 < n:
                    n3 += 1
                    o.write(str)
                elif number == 4 and n4 < n:
                    n4 += 1
                    o.write(str)
                elif number == 5 and n5 < n:
                    n5 += 1
                    o.write(str)
                elif number == 6 and n6 < n:
                    n6 += 1
                    o.write(str)
                elif number == 7 and n7 < n:
                    n7 += 1
                    o.write(str)
                elif number == 8 and n8 < n:
                    n8 += 1
                    o.write(str)
                elif number == 9 and n9 < n:
                    n9 += 1
                    o.write(str)

                str = ''
                first = True
        else:
            end = True

    i.close
    o.close
    print(n0)
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    print(n6)
    print(n7)
    print(n8)
    print(n9)

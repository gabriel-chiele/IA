import parser

arg = parser.parse()

i = open(arg.input,'r')
o = open(arg.output,'w')

end = False
str = ''

o.write('@RELATION Weka\n')
o.write('\n')

for j in range(1024):
    o.write('@ATTRIBUTE bnr%i	numeric\n' % j)

o.write('@ATTRIBUTE class 	{0,1,2,3,4,5,6,7,8,9}\n')
o.write('\n')
o.write('@DATA\n')

first = True

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
            o.write(str)
            str = ''
            first = True
    else:
        end = True

# @DATA

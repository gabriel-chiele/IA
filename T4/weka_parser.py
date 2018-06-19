import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', dest='input', required=True, help='arquivo de entrada')
parser.add_argument('--output', dest='output', required=True, help='arquivo de saída')

arg = parser.parse_args()

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

while not end:
    line = i.readline()
    if not line == '':
        line = line.replace('\n','')
        line = line.replace(' ','')
        if not len(line) == 1:
            lst = list(line)
            new_line = ''
            for k in range(len(lst)):
                if k == 0:
                    new_line = lst[k]
                else:
                    new_line = new_line + ',' + lst[k]
            str = str + new_line
        else:
            str = str + ',' + line + '\n'
            o.write(str)
            str = ''
    else:
        end = True

# @DATA

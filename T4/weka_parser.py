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
o.write('@ATTRIBUTE binary	string\n')
o.write('@ATTRIBUTE number	string\n')
o.write('@ATTRIBUTE class 	{0,1,2,3,4,5,6,7,8,9}\n')
o.write('\n')
o.write('@DATA\n')

while not end:
    line = i.readline()
    if not line == '':
        line = line.replace('\n','')
        line = line.replace(' ','')
        if not len(line) == 1:
            str = str + line
        else:
            str = str + ',' + line + '\n'
            o.write(str)
            str = ''
    else:
        end = True

# @DATA

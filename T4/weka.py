import parser
import weka_formater

if __name__ == '__main__':
    arg = parser.parse()
    weka_formater.formater(arg.input, arg.output, n)

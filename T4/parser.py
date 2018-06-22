import argparse

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', dest='input', required=True, help='arquivo de entrada')
    parser.add_argument('-o', dest='output', required=True, help='arquivo de saída')
    parser.add_argument('-n', dest='n', required=True, help='numero de instancias de cada numero')

    return parser.parse_args()

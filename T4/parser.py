import argparse

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', dest='input', required=True, help='arquivo de entrada')
    parser.add_argument('-o', dest='output', required=True, help='arquivo de saída')

    return parser.parse_args()

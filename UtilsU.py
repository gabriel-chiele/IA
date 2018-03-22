#
# Definição de métodos utilitários
#

from FieldU import Field
from optparse import OptionParser

# DEFINE UM PARSER E RETORNA AS OPÇÕES #
def ParseOption():
	err = False
	parser = OptionParser()
	parser.add_option("-f", "--input_file", dest="filename", help='caminho do arquivo de entrada')
	parser.add_option("-s", "--size", dest="size", type="int", help='tamanho da matriz')
	parser.add_option("-c", "--cartorios", dest="cartorios", type="int", help='numero de cartorios')
  
	options, args = parser.parse_args()

	if len(args) != 0: #TODO ?PQ O NUMERO DE ARGS ESTA DANDO SEMPRE '0'?
		parser.error('Faltando Parametros! -h para ver a ajuda')
		err = True
	if options.filename == '':
		parser.error('Caminho do arquivo nao pode ser vazio')
		err = True
	if options.size < 2:
		parser.error('O tamanho da matriz deve ser no minimo 2')
		err = True
	if options.cartorios == 0:
		parser.error('Precisamos de no minimo 1 cartorio')
		err = True

	if not err:
		return options
	else:
		return nil

def LoadFile(filename):
	print(filename)

def GenerateField(size, cartorios):
	field = Field(size)
	#	field.mGround[][] = c_Cartorio
	return field

def EndCredits():
	print('Encerrando simulacao em\n3 ...')
	sleep(1)
	print('2 ...')
	sleep(1)
	print('1 ...')
	sleep(1)




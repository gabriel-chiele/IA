#
# Definição de métodos utilitários
#

import sys
from time import sleep
from FieldU import Field
from optparse import OptionParser
from AgentU import *

# DEFINE UM PARSER E RETORNA AS OPÇÕES #
def ParseOption():
	err = False
	parser = OptionParser()
	parser.add_option("-f", "--input_file", dest="filename", help='caminho do arquivo de entrada')
	parser.add_option("-s", "--size", dest="size", type="int", help='tamanho da matriz')
  
	options, args = parser.parse_args()

	if not (len(sys.argv) != 5):
		if options.filename == '':
			parser.error('Caminho do arquivo nao pode ser vazio')
			err = True
		if options.size < 2:
			parser.error('O tamanho da matriz deve ser no minimo 2')
			err = True
	else:
		parser.error('Faltando parametros! -h para ver a ajuda')
		err = True

	if not err:
		return options
	else:
		return None

def LoadFile(filename):
	try:
		fFile = open(filename, 'r')
	except:
		return None

	line = ''
	nLineNumber = 0

	while ((nLineNumber == 0) or not (line == '')  ):
		lstLines = line.split(' ')
		
		if nLineNumber == 0:
			nCouplesNumber = lstLines[0]
			nCartoriosNumber = lstLines[1]
			conf = Config(nCouplesNumber,nCartoriosNumber)
		else:
			pref = lstLines[1: nCouplesNumber]
			if (lstLines[0] < (nCouplesNumber + 1)):
				gender = c_MALE
			else:
				gender = c_FEMALE
	
			ag = Agent(lstLines[0], pref, c_FEMALE)
			conf.AddAgent(ag)

		nLineNumber = nLineNumber + 1

	return conf

def GenerateField(size, cartorios):
	field = Field(size)
	#	field.mGround[][] = c_Cartorio
	return field

def EndCredits(short):
	if not short:
		print('Encerrando simulacao em\n3 ...')
		sleep(1)
		print('2 ...')
		sleep(1)
		print('1 ...')
		sleep(1)

	print('Simulacao encerrada!')




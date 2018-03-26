#
# Definicao de metodos utilitarios
#

import sys
from time import sleep
from FieldU import Field
from optparse import OptionParser
from AgentU import *
from ConfigU import *
from ConstantsU import *

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

	nLineNumber = 0
	print('Lendo as configuracoes da simulacao...')
	while (True):
		line = fFile.readline()
		if (line == ''):
			break

		line = line[:-1]
		lstLines = line.split(' ')
		
		if nLineNumber == 0:
			nCouplesNumber = int(lstLines[0])
			nCartoriosNumber = int(lstLines[1])
			conf = Config(nCouplesNumber,nCartoriosNumber)
		else:
			pref = lstLines[1:]
			if (nLineNumber < (nCouplesNumber + 1)):
				gender = c_MALE
			else:
				gender = c_FEMALE
	
			ag = Agent(int(lstLines[0]), pref, gender)
			conf.AddAgent(ag)

		nLineNumber = nLineNumber + 1

	PrintConf(conf)
	fFile.close()
	return conf

def GenerateField(size, cartorios):
	print('Gerando o mapa...')
	field = Field(size, cartorios)
	return field

def PrintConf(conf):
	print('Numero de casais: %i' % conf.nCouplesNumber)
	print('Numero de cartorios: %i' % conf.nCartoriosNumber)
	for agente in conf.lstAgents:
		print('Agente: ' + agente.ToString())

def EndCredits(short):
	if not short:
		print('Encerrando simulacao em\n3 ...')
		sleep(1)
		print('2 ...')
		sleep(1)
		print('1 ...')
		sleep(1)

	print('Simulacao encerrada!')
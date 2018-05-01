#
# Definicao de metodos utilitarios
#

import sys

import AgentU
import ConfigU
import ConstantsU
import GlobalsU
import FieldU
import PriorityQueueU

from math 		import sqrt
from time 		import sleep
from optparse 	import OptionParser
from random		import randrange

def ParseOption():
	err = False
	parser = OptionParser()
	parser.add_option("-f", "--input_file", dest="filename", help='caminho do arquivo de entrada')
	parser.add_option("-s", "--size", dest="size", type="int", help='tamanho da matriz')
	parser.add_option("-v", "--verbose", dest="verbose" , action="store_true", help='ativa modo verboso', default=False)

	options, args = parser.parse_args()

	if (not (len(sys.argv) < 5)) and (not (len(sys.argv) > 6)):
		if options.filename == '':
			parser.error('Caminho do arquivo nao pode ser vazio')
			err = True
		if options.size < 5:
			parser.error('O tamanho da matriz deve ser no minimo 5')
			err = True
	elif (len(sys.argv) > 6):
		parser.error('Parametros desconhecidos')
		err = True
	else:
		parser.error('Faltando parametros! -h para ver a ajuda')
		err = True

	if not err:
		return options
	else:
		return None

def LoadConfigurations(options):
	try:
		fFile = open(options.filename, 'r')
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
			conf = ConfigU.Config(options.size, nCouplesNumber,nCartoriosNumber)
		else:
			pref = lstLines[1:]
			if (nLineNumber < (nCouplesNumber + 1)):
				gender = ConstantsU.c_MALE
			else:
				gender = ConstantsU.c_FEMALE

			ag = AgentU.Agent(int(lstLines[0]), pref, gender)
			conf.AddAgent(ag)

		nLineNumber = nLineNumber + 1

	fFile.close()
	GlobalsU.setVerbose(options.verbose)
	return conf

def EraseConf(conf):
	conf.nSize = None
	del conf.lstAgents[:]
	if GlobalsU.Verbose():
		print('Limpando variaveis auxiliares...')

def EndCredits(sTime, nQtdMarriages, nQtdDivorces):
	if GlobalsU.Verbose():
		print('Encerrando simulacao em\n3 ...')
		sleep(1)
		print('2 ...')
		sleep(1)
		print('1 ...')
		sleep(1)

	print(ConstantsU.tc_EndScreen % (sTime, nQtdMarriages, nQtdDivorces))

def CalculateHeuristic(tp1, tp2):
    (x1, y1) = tp1
    (x2, y2) = tp2
    return (abs(x1 - x2) + abs(y1 - y2))

def CalculateEuclidianDistance(tpPos, lstCartorios):
	closest = (0,0)
	nBestDistance = -1
	nThisDistance = 0
	for cartorio in lstCartorios:
		nThisDistance = sqrt(((tpPos[0] - cartorio.tpPos[0])**2) + ((tpPos[1] - cartorio.tpPos[1])**2))

		if (nThisDistance < nBestDistance) or (nBestDistance == -1):
			nBestDistance = nThisDistance
			closest = cartorio.tpPos
	return closest

def ReconstructPath(From, Start, End):
    tpCurrent = End
    lstPath = []
    while tpCurrent != Start:
        lstPath.append(tpCurrent)
        tpCurrent = From[tpCurrent]
    lstPath.append(Start)
    lstPath.pop(0)
    lstPath.reverse()
    return lstPath

def AStarSearch(Field, Start, End):
    pqFrontier = PriorityQueueU.PriorityQueue()
    pqFrontier.put(Start, 0)
    dctCameFrom = {}
    dctCost = {}
    dctCameFrom[Start] = None
    dctCost[Start] = 0

    while not pqFrontier.empty():
        tpCurrent = pqFrontier.get()

        if tpCurrent == End:
            break

        for tpNext in Field.GetNeighbors(tpCurrent, End):
            nNewCost = dctCost[tpCurrent] + 1
            if tpNext not in dctCost or nNewCost < dctCost[tpNext]:
                dctCost[tpNext] = nNewCost
                nPriority = nNewCost + CalculateHeuristic(End, tpNext)
                pqFrontier.put(tpNext, nPriority)
                dctCameFrom[tpNext] = tpCurrent

    return dctCameFrom

def CalculateTotalMarriages(lstCartorios):
	sum = 0
	for cartorio in lstCartorios:
		sum = sum + cartorio.nNumberOfMarriages

	return sum

def CalculateTotalDivorces(lstCartorios):
	sum = 0
	for cartorio in lstCartorios:
		sum = sum + cartorio.nNumberOfDivorces

	return sum

def EqualTuples(tp1, tp2):
	return ((tp1[0] == tp2[0]) and (tp1[1] == tp2[1]))

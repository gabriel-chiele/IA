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

def CalculateHeuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
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
    current = End
    path = []
    while current != Start:
        path.append(current)
        current = From[current]
    path.append(Start)
    path.pop(0)
    path.reverse()
    return path

def AStarSearch(field, start, goal):
    frontier = PriorityQueueU.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in field.GetNeighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + CalculateHeuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from

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

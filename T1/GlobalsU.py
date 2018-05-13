#
#	Modulo de variaveis globais
#

g_bVerbose = False
g_EndSimulation = False

def setVerbose(bVerbose):
	global g_bVerbose
	g_bVerbose = bVerbose

def Verbose():
	global g_bVerbose
	return g_bVerbose

def setEndSimulation(bEnd):
	global g_EndSimulation
	g_EndSimulation = bEnd

def EndSimulation():
	global g_EndSimulation
	return g_EndSimulation
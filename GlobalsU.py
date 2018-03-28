#
#	Definicao da classe agente
#

g_bVerbose = False;

def setVerbose(bVerbose):
	global g_bVerbose
	g_bVerbose = bVerbose

def Verbose():
	global g_bVerbose
	return g_bVerbose
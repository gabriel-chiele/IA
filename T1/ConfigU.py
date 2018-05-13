#
#	Definicao da classe de consfiguracoes da simulacao
#

import GlobalsU

class Config:
	def __init__(self, size, cn1, cn2):
		self.nSize				= size
		self.nCouplesNumber		= cn1
		self.nCartoriosNumber	= cn2
		self.lstAgents			= []

	def AddAgent(self, ag):
		self.lstAgents.append(ag)

	def PrintConf(self):
		if (GlobalsU.Verbose()):
			print('Tamanho do mapa: %i' % self.nSize)
			print('Numero de casais: %i' % self.nCouplesNumber)
			print('Numero de cartorios: %i' % self.nCartoriosNumber)
			for agente in self.lstAgents:
				print('Agente: %s' % agente.ToString())
		

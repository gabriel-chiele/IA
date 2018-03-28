#
#	Definicao da classe de consfiguracoes da simulacao
#

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
			print('Numero de casais: %i' % self.nCouplesNumber)
			print('Numero de cartorios: %i' % self.nCartoriosNumber)
			for agente in self.lstAgents:
				print('Agente: ' + agente.ToString())
		

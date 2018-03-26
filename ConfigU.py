#
#	Definição da classe de consfigurações da simulação
#

class Config:
	def __init__(self, cn1, cn2):
		self.nCouplesNumber		= cn1
		self.nCartoriosNumber	= cn2
		self.lstAgents			= []

	def AddAgent(self, ag):
		self.lstAgents.append(ag)
		

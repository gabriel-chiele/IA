#
#	Definição da classe de consfigurações da simulação
#

class Config:
	def __init__(self, cn1, cn2):
		self.nCouplesNumber		= 0
		self.nCartoriosNumber	= 0
		self.lstAgents			= []

	def AddAgent(self, ag):
		self.lstAgents.append(ag)
		

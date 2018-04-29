#
#	Definicao da classe proposta
#

class Proposal:
	def __init__(self, nMyID, nPretenderID):
		self.nAgentMadeProposeID = nMyID
		self.nAgentProposedID = nPretenderID
		self.bAccepted = False

	def Accept(self):
		self.bAccepted = True

	def Reject(self):
		self.bAccepted = False

	def CheckProposeResponse(self):
		return self.bAccepted

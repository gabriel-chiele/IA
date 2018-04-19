#
#	Definicao da classe propsta

class Proposal:
	def __init__(self, nMyID, nPretenderID):
		self.nAgentMadeProposeID = nMyID
		self.nAgentProposedID = nPretenderID
		self.bAccepted = False

	def Accept():
		self.bAccepted = True

	def Reject():
		self.bAccepted = False

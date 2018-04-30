#
#	Definicao da classe proposta
#

class Proposal:
	def __init__(self, nMyID, nPretenderID, tpCartorio):
		self.nAgentMadeProposeID = nMyID
		self.nAgentProposedID = nPretenderID
		self.bAccepted = False
		self.tpCartorio = tpCartorio

	def Accept(self):
		self.bAccepted = True

	def Reject(self):
		self.bAccepted = False

	def CheckProposeResponse(self):
		return self.bAccepted

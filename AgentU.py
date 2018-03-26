#
#	Definicao da classe agente
#
from ConstantsU	import *

class Agent:
	def __init__(self, ID, pref, gender):
		self.nID 			= ID	
		self.lstPreferences	= pref
		self.bMarried 		= False
		self.nCoupleID		= 0
		self.cGender		= gender
		self.tpPos			= (0,0)
		self.lstCartorios	= []
		self.nFacing		= c_NORTE

	def ToString(self):
		return str(self.nID) + ' - ' + self.cGender + ' - '  + str(self.lstPreferences)

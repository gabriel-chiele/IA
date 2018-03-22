#
#	Definição da classe agente
#

from UtilsU     import *
from ConstantsU import *

class Agent:
	def __init__(self, ID, pref, gender):
		self.nID 					 = ID	
		self.lstPrefereces = pref
		self.bMarried 		 = False
		self.nCoupleID		 = 0
		self.cGender			 = gender
		self.tpPos	 			 = (0,0)
		self.lstCartorios	 = []
		self.nFacing			 = cNORTE

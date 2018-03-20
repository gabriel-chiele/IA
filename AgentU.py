#
#	Definição da classe agente
#

from UtilsU     import *
from ConstantsU import *

class Agent:
	def __init__(self):
		self.nID 					 = 0	
		self.lstPrefereces = []
		self.bMarried 		 = False
		self.nCoupleID		 = 0
		self.cGender			 = ''
		self.tpPos	 			 = (0,0)
		self.lstCartorios	 = []
		self.nFacing			 = cNORTE

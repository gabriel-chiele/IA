#
# Definição da classe campo
#

from ConstantsU import *

class Field:
	def __init__(self, s):
		self.nSize       = s
		self.lstCartorio = []
		self.lstWalls 	 = []
		self.mGround   	 = [[c_Clear]*s for s in range(s)]

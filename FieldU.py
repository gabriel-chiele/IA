#
# Definição da classe campo
#

class Field:
	def __init__(self, l, c):
		self.matrix   	 = [l][c]
		self.nLines  		 = l
		self.nColumns 	 = c
		self.lstCartorio = []
		self.lstWalls 	 = []

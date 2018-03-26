#
# Definição da classe parede
#

from ConstantsU import *
from random		import choice
from random 	import randrange

class Wall:
	def __init__(self, nFieldSize):
		self.nWallSize = (nFieldSize // 2) + 1
		self.lstPos = []
		self.CalculatePosition(nFieldSize)

	def CalculatePosition(self, nFieldSize):
		bFit = False

		while not (bFit):
			nDir = choice([c_NORTE, c_SUL, c_LESTE, c_OESTE])
			
			nX = randrange(nFieldSize - 1)
			nY = randrange(nFieldSize - 1)

			nSizeVariation = randrange(2)

			if nDir == c_NORTE:
				if ((nX - (self.nWallSize - nSizeVariation)) <  0):
					bFit = True
			elif nDir == c_SUL:
				if ((nX + (self.nWallSize - nSizeVariation)) <  nFieldSize):
					bFit = True
			elif nDir == c_LESTE:
				if ((nY + (self.nWallSize - nSizeVariation)) <  nFieldSize):
					bFit = True
			elif nDir == c_OESTE:
				if ((nY - (self.nWallSize - nSizeVariation)) <  0):
					bFit = True

		for i in range(self.nWallSize - nSizeVariation):
			if nDir == c_NORTE:
				self.lstPos.append(tuple((nX - i, nY)))
			elif nDir == c_SUL:
				self.lstPos.append(tuple((nX + i, nY)))
			elif nDir == c_LESTE:
				self.lstPos.append(tuple((nX, nY + i)))
			elif nDir == c_OESTE:
				self.lstPos.append(tuple((nX, nY - i)))
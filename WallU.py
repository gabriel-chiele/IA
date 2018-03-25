#
# Definição da classe parede
#

from ConstantsU import *

class Wall:
	def __init__(self, nFieldSize, nWallSize):
		self.nWallSize = (nWallSize // 2) + 1
		self.CalculatePosicion(nFieldSize)

	def CalculatePosicion(self, nFieldSize)
		bFit = False

		while not (bFit):
			nDir = choice([c_NORTE, c_SUL, c_LESTE, c_OESTE])
			
			nX = randrange(nFieldSize - 1)
			nY = randrange(nFieldSize - 1)

			nSizeVariation = randrange(2)

			if nDir = c_NORTE:
				if ((nX - (self.nWallSize - nSizeVariation)) <  0):
					bFit = True
			else if nDir = c_SUL:
				if ((nX + (self.nWallSize - nSizeVariation)) <  nFieldSize):
					bFit = True
			else if nDir = c_LESTE:
				if ((nY + (self.nWallSize - nSizeVariation)) <  nFieldSize):
					bFit = True
			else if nDir = c_OESTE:
				if ((nY - (self.nWallSize - nSizeVariation)) <  0):
					bFit = True

		for i in range(self.nWallSize - nSizeVariation):
			if nDir = c_NORTE:
				self.lstPos.append(nX - i, nY)
			else if nDir = c_SUL:
				self.lstPos.append(nX + i, nY)
			else if nDir = c_LESTE:
				self.lstPos.append(nX, nY + i)
			else if nDir = c_OESTE:
				self.lstPos.append(nX, nY - i)
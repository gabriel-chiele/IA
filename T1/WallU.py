#
# Definicao da classe parede
#

import ConstantsU
import GlobalsU

from random	import randrange

class Wall:
	def __init__(self, nFieldSize, nWallNumber):
		self.nID = nWallNumber
		self.nWallSize = (nFieldSize // 2) + 1
		self.lstPos = []
		self.CalculatePosition(nFieldSize)

	def CalculatePosition(self, nFieldSize):
		nWallQtd = nFieldSize // ConstantsU.c_FIELD_SIZE_FACTOR
		nSizeVariation = randrange(ConstantsU.c_SIZE_VARIATION)
		size = (self.nWallSize - nSizeVariation)

		nX = randrange((nFieldSize - size - 1))
		nY = (self.nID * ConstantsU.c_FIELD_SIZE_FACTOR) - ConstantsU.c_WALL_SPACING_FACTOR

		for i in range(size):
			self.lstPos.append(tuple((nX + i, nY)))



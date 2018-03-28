#
# Definicao da classe parede
#

import ConstantsU

from random	import choice, randrange

class Wall:
	def __init__(self, nFieldSize):
		self.nWallSize = (nFieldSize // 2) + 1
		self.lstPos = []
		self.CalculatePosition(nFieldSize)

	def CalculatePosition(self, nFieldSize):
		bFit = False

		while not (bFit):
			nDir = choice([ConstantsU.c_NORTE, ConstantsU.c_SUL, ConstantsU.c_LESTE, ConstantsU.c_OESTE])
			
			nX = randrange(nFieldSize - 1)
			nY = randrange(nFieldSize - 1)

			nSizeVariation = randrange(ConstantsU.c_SIZE_VARIATION)

			if nDir == ConstantsU.c_NORTE:
				if ((nX - (self.nWallSize - nSizeVariation)) <  0):
					bFit = True
			elif nDir == ConstantsU.c_SUL:
				if ((nX + (self.nWallSize - nSizeVariation)) <  nFieldSize):
					bFit = True
			elif nDir == ConstantsU.c_LESTE:
				if ((nY + (self.nWallSize - nSizeVariation)) <  nFieldSize):
					bFit = True
			elif nDir == ConstantsU.c_OESTE:
				if ((nY - (self.nWallSize - nSizeVariation)) <  0):
					bFit = True

		for i in range(self.nWallSize - nSizeVariation):
			if nDir == ConstantsU.c_NORTE:
				self.lstPos.append(tuple((nX - i, nY)))
			elif nDir == ConstantsU.c_SUL:
				self.lstPos.append(tuple((nX + i, nY)))
			elif nDir == ConstantsU.c_LESTE:
				self.lstPos.append(tuple((nX, nY + i)))
			elif nDir == ConstantsU.c_OESTE:
				self.lstPos.append(tuple((nX, nY - i)))
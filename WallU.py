#
# Definicao da classe parede
#

import ConstantsU
import GlobalsU

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
			size = (self.nWallSize - nSizeVariation)

			if nDir == ConstantsU.c_NORTE:
				if ((nY - size) >  0):
					bFit = True
			elif nDir == ConstantsU.c_SUL:
				if ((nY + size) <  nFieldSize):
					bFit = True
			elif nDir == ConstantsU.c_LESTE:
				if ((nX - size) >  0):
					bFit = True
			elif nDir == ConstantsU.c_OESTE:
				if ((nX + size) <  nFieldSize):
					bFit = True

			if bFit:
				self.PrintWallPositionDetails(nDir, nX, nY, size)

		for i in range(size):
			if nDir == ConstantsU.c_NORTE:
				self.lstPos.append(tuple((nX, nY - i)))
			elif nDir == ConstantsU.c_SUL:
				self.lstPos.append(tuple((nX, nY + i)))
			elif nDir == ConstantsU.c_LESTE:
				self.lstPos.append(tuple((nX - i, nY)))
			elif nDir == ConstantsU.c_OESTE:
				self.lstPos.append(tuple((nX + i, nY)))

	def PrintWallPositionDetails(self, ndir, x, y, size):
		if GlobalsU.Verbose():
			sdir = ConstantsU.DirToStr(ndir)
			print('Direcao: %s\t Inicio:(%i,%i)\t Tamanho:%i' % (sdir, x, y, size))
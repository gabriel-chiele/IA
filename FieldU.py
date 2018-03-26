#
# Definicao da classe campo
#

import numpy

from ConstantsU import *
from CartorioU 	import *
from WallU 	import *

class Field:
	def __init__(self, s, c):
		self.nSize		= s
		self.mGround		= numpy.zeros(shape=(s,s))
		self.nWallsQtd 		= self.nSize // 5
		self.lstWalls		= []
		self.lstCartorios 	= []

		self.GenerateWalls()
		self.GenerateCartorios(c)

	def GenerateWalls(self):
		print('Gerando as paredes...')
		for i in range(self.nWallsQtd):
			self.lstWalls.append(Wall(self.nSize))

		print('Posicionando as paredes...')
		for wall in self.lstWalls:
			for pos in wall.lstPos:
				self.mGround[pos[0]][pos[1]] = c_Wall

	def GenerateCartorios(self, nCartorios):
		print('Gerando os cartorios...')
		for i in range(nCartorios):
			self.lstCartorios.append(Cartorio(self.nWallsQtd, self.lstWalls, self.nSize))

		print('Posicionando cartorios...')
		for cartorio in self.lstCartorios:
			self.mGround[cartorio.tpPos[0]][cartorio.tpPos[1]] = c_Cartorio

	def VerifyWallPositions(self):
		print('')

	def VerifyCartoriosPositions(self):
		print('')

	def PrintMap(self):
		str = (self.nSize * '*' * 4) + '**'
		print(str)
		for i in range(self.nSize):
			str = '*'
			for j in range(self.nSize):
				if (self.mGround[i][j] == c_Clear):
					str = str + '    '
				elif (self.mGround[i][j] == c_Cartorio):
					str = str + ' CT '
				elif (self.mGround[i][j] == c_Wall):
					str = str + ' || '
				elif (self.mGround[i][j] == c_Agent):
					str = str + ' AG '
				elif (self.mGround[i][j] == c_Couple):
					str = str + ' CP '
			str = str + '*'
			print(str)
		str = (self.nSize * '*' * 4) + '**'
		print(str)

#
# Definição da classe campo
#

from ConstantsU import *
from CartorioU 	import *
from WallU 		import *

class Field:
	def __init__(self, s, c):
		self.nSize			= s
		self.mGround		= [[c_Clear] * s] * s
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
		for i in range(self.nSize):
			print(self.mGround[i])

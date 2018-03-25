#
# Definição da classe campo
#

from ConstantsU import *

class Field:
	def __init__(self, s, c):
		self.nSize			= s
		self.lstCartorio	= [(0,0) * c]
		self.mGround		= [[c_Clear]*s for s in range(s)]
		self.nWallsQtd 		= self.nSize // 5

		self.GenerateWalls()
		self.PlaceCartorios()

	def GenerateWalls(self):
		print('Gerando as paredes...')
		for i in range(self, nSide, self.nWallsQtd):
			self.lstWalls.append(Wall.Create(self.nSize))

		print('Posicionando as paredes...')
		for wall in self.lstWalls:
			for pos in wall.lstPos:
				self.mGroud[pos[0], pos[1]] = c_Wall

	def PlaceCartorios(self):
		print('Gerando os cartorios...')

		print('Posicionando cartorios...')

	def VerifyWallPositions(self):
		print('')

	def VerifyCartoriosPositions(self):
		print('')
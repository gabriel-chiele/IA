#
# Definicao da classe campo
#

import numpy
import ConstantsU
import CartorioU
import WallU
import GlobalsU

from random import randrange

class Field:
	def __init__(self, conf):
		print('Gerando o mapa...')
		self.nSize			= conf.nSize
		self.mGround		= numpy.zeros(shape=(conf.nSize, conf.nSize))
		self.nWallsQtd 		= self.nSize // 5
		self.lstWalls		= []
		self.lstCartorios 	= []

		self.GenerateWalls()
		self.GenerateCartorios(conf.nCartoriosNumber)
		self.PlaceAgents(conf)

	def GenerateWalls(self):
		print('Gerando as paredes...')
		for i in range(self.nWallsQtd):
			self.lstWalls.append(WallU.Wall(self.nSize))

		print('Posicionando as paredes...')
		for wall in self.lstWalls:
			for pos in wall.lstPos:
				self.SetPosition(pos, ConstantsU.c_Wall)

	def GenerateCartorios(self, nCartorios):
		print('Gerando os cartorios...')
		for i in range(nCartorios):
			self.lstCartorios.append(CartorioU.Cartorio(self.nWallsQtd, self.lstWalls, self.nSize))

		print('Posicionando cartorios...')
		for cartorio in self.lstCartorios:
			self.SetPosition(cartorio.tpPos, ConstantsU.c_Cartorio)

	def PlaceAgents(self, conf):
		print('Posicionando Agentes...')
		for agent in conf.lstAgents:
			bOK = False
			while not bOK:
				tpPos = (randrange(self.nSize), randrange(self.nSize))
				if (self.GetPosition(tpPos) == ConstantsU.c_Clear):
					self.SetPosition(tpPos, ConstantsU.c_Agent)
					agent.tpPos = tpPos
					bOK = True

	def VerifyWallPositions(self):
		print('')

	def VerifyCartoriosPositions(self):
		print('')

	def PrintMap(self):
		if (GlobalsU.Verbose()):
			str = (self.nSize * '*' * 4) + '**'
			print(str)
			for i in range(self.nSize):
				str = '*'
				for j in range(self.nSize):
					if (self.GetPosition((i, j)) == ConstantsU.c_Clear):
						str = str + '    '
					elif (self.GetPosition((i, j)) == ConstantsU.c_Cartorio):
						str = str + ' CT '
					elif (self.GetPosition((i, j)) == ConstantsU.c_Wall):
						str = str + ' || '
					elif (self.GetPosition((i, j)) == ConstantsU.c_Agent):
						str = str + ' AG '
					elif (self.GetPosition((i, j)) == ConstantsU.c_Couple):
						str = str + ' CP '
				str = str + '*'
				print(str)
			str = (self.nSize * '*' * 4) + '**'
			print(str)

	def GetPosition(self, tpPos):
		return self.mGround.item(tpPos[0], tpPos[1])

	def SetPosition(self, tpPos, obj):
		self.mGround[tpPos[0]][tpPos[1]] = obj

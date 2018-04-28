#
# Definicao da classe campo
#

import numpy
import ConstantsU
import CartorioU
import WallU
import GlobalsU
import UtilsU

from random import randrange
from copy import copy

class Field:
	def __init__(self, conf):
		print('Gerando o mapa...')
		self.nSize			= conf.nSize
		self.mGround		= numpy.zeros(shape=(conf.nSize, conf.nSize))
		self.nWallsQtd 		= self.nSize // 5
		self.lstWalls		= []
		self.lstCartorios 	= []
		self.lstAgents		= copy(conf.lstAgents)

		self.GenerateWalls()
		self.GenerateCartorios(conf.nCartoriosNumber)
		self.PlaceAgents()

	def GenerateWalls(self):
		print('Gerando as paredes...')
		for i in range(self.nWallsQtd):
			self.lstWalls.append(WallU.Wall(self.nSize, (i + 1)))

		print('Posicionando as paredes...')
		for wall in self.lstWalls:
			for pos in wall.lstPos:
				if GlobalsU.Verbose():
					self.PrintObjectPosition(pos, ConstantsU.c_Wall)
				self.SetPosition(pos, ConstantsU.c_Wall)

	def GenerateCartorios(self, nCartorios):
		print('Gerando os cartorios...')
		for i in range(nCartorios):
			self.lstCartorios.append(CartorioU.Cartorio(self.nWallsQtd, self.lstWalls, self.nSize))

		print('Posicionando cartorios...')
		for cartorio in self.lstCartorios:
			if GlobalsU.Verbose():
				self.PrintObjectPosition(cartorio.tpPos, ConstantsU.c_Cartorio)
			self.SetPosition(cartorio.tpPos, ConstantsU.c_Cartorio)

	def PlaceAgents(self):
		print('Posicionando Agentes...')
		for agent in self.lstAgents:
			bOK = False
			while not bOK:
				tpPos = (randrange(self.nSize), randrange(self.nSize))
				if (self.GetPosition(tpPos) == ConstantsU.c_Clear):
					agent.tpPos = tpPos
					agent.lstCartorios = copy(self.lstCartorios)
					self.SetPosition(tpPos, ConstantsU.c_Agent)
					if GlobalsU.Verbose():
						self.PrintObjectPosition(tpPos, ConstantsU.c_Agent)
					bOK = True

	def PrintMap(self):
		if (GlobalsU.Verbose()):
			str = (self.nSize * '*' * 4) + '**'
			print(str)
			for i in range(self.nSize):
				str = '*'
				for j in range(self.nSize):
					item = self.GetPosition((i, j))
					if ( item == ConstantsU.c_Clear):
						str = str + ' %s ' % (UtilsU.ObjToStr(ConstantsU.c_Clear, True))
					elif (item == ConstantsU.c_Cartorio):
						str = str + ' %s ' % (UtilsU.ObjToStr(ConstantsU.c_Cartorio, True))
					elif (item == ConstantsU.c_Wall):
						str = str + ' %s ' % (UtilsU.ObjToStr(ConstantsU.c_Wall, True))
					elif (item == ConstantsU.c_Agent):
						str = str + ' %s ' % (self.GetAgent((i,j)).ToString(short=True))
					elif (item == ConstantsU.c_Couple):
						str = str + ' %s ' % (UtilsU.ObjToStr(ConstantsU.c_Couple, True))
				str = str + '*'
				print(str)
			str = (self.nSize * '*' * 4) + '**'
			print(str)

	def GetPosition(self, tpPos):
		return self.mGround.item(tpPos[0], tpPos[1])

	def SetPosition(self, tpPos, obj):
		self.mGround[tpPos[0]][tpPos[1]] = obj

	def GetAgent(self, tpPos):
		for ag in self.lstAgents:
			if (ag.tpPos == tpPos):
				return ag

	def GetCouple(self, nCoupleID):
		for ag in self.lstAgents:
			if (ag.nID == nCoupleID):
				return ag

	def GetCartorio(self, tpPos):
		for ct in self.lstCartorios:
			if (ct.tpPos == tpPos):
				return ct

	def PrintObjectPosition(self, tpPos, obj):
		print('%s: (%i,%i)' % (UtilsU.ObjToStr(obj), tpPos[0], tpPos[1]))

	def InBounds(self, id):
		(x, y) = id
		return ((0 <= x < self.nSize) and (0 <= y < self.nSize))

    def IsPassable(self, id):
		bOK = True
		for wall in self.walls:
			bOK = bOK and (id not in self.walls)
		return bOK

	def GetNeighbors(self, id):
		(x, y) = id
		results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1), (x-1, y-1), (x+1, y-1), (x+1, y+1), (x-1, y+1)]
		results = filter(self.InBounds, results)
		results = filter(self.IsPassable, results)
		return results

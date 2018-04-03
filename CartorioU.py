#
#	Definicao da classe cartorio
#

from random import choice, randrange

class Cartorio:
	def __init__(self, nWallsQtd, lstWalls, nFieldSize):
		self.tpPos = tuple((0,0))
		self.CalculatePosition(nWallsQtd, lstWalls, nFieldSize)

	def CalculatePosition(self, nWallsQtd, lstWalls, nFieldSize):	
		nWich	   = randrange(nWallsQtd - 1)
		tpWallPos  = choice(lstWalls[nWich].lstPos)

		if ((tpWallPos[0] + 1) < nFieldSize):
			self.tpPos = tuple((tpWallPos[0] + 1, self.tpPos[1]))
		elif ((tpWallPos[0] - 1) < 0):
			self.tpPos = tuple((tpWallPos[0] - 1, self.tpPos[1]))

		if ((tpWallPos[1] + 1) < nFieldSize):
			self.tpPos = tuple((self.tpPos[0], tpWallPos[1] + 1))
		elif ((tpWallPos[1] - 1) < 0):
			self.tpPos = tuple((self.tpPos[0], tpWallPos[1] - 1))

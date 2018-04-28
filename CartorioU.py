#
#	Definicao da classe cartorio
#

from random import choice, randrange

class Cartorio:
	def __init__(self, nWallsQtd, lstWalls, nFieldSize):
		self.tpPos = tuple((0,0))
		self.CalculatePosition(nWallsQtd, lstWalls, nFieldSize)
		self.lstPresence = []

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

	def CheckIn(self, agent):
		self.lstPresence.append(agent)

	def CheckOut(self, agent):
		self.lstPresence.remove(agent)

	def CoupleArrived(self, nID):
		for ag in self.lstPresence:
			if (ag.nID == nID) and not (ag.bMarried):
				return True
		return False

	def CreateCouple(self, field, ag):
		CoupleAg = field.GetCouple(ag.nCoupleID)
		ag.bMarried = True
		ag.nCoupleID = CoupleAg.nID

		CoupleAg.bMarried = True
		CoupleAg.nCoupleID = ag.nCoupleID
		CoupleAg.tpPos = (-1,-1) #retira do mapa
		CoupleAg.OnCartorio = None
		CoupleAg.OnCartorio.CheckOut(self)

	def DivorceCouple(self, field, ag):
		CoupleAg = field.GetCouple(ag.nCoupleID)
		ag.bMarried = False
		ag.nCoupleID = 0

		CoupleAg.bMarried = False
		CoupleAg.nCoupleID = 0
		CoupleAg.tpPos = (0,0) #TODO: pegar posição valida próxima a posição do cartorio
		CoupleAg.OnCartorio = ag.OnCartorio
		CoupleAg.OnCartorio.CheckIn(self)

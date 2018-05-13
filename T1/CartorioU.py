#
#	Definicao da classe cartorio
#

import GlobalsU
import ConversionU

from random import choice, randrange

class Cartorio:
	def __init__(self, nWallsQtd, lstWalls, nFieldSize):
		self.tpPos = tuple((0,0))
		self.CalculatePosition(nWallsQtd, lstWalls, nFieldSize)
		self.lstPresence = []
		self.nNumberOfMarriages = 0
		self.nNumberOfDivorces = 0

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
		if (agent not in self.lstPresence):
			self.lstPresence.append(agent)
			agent.bChecked = True
			if (GlobalsU.Verbose()):
				print('%s fez CheckIn no cartorio %s' % (agent.ToString(short=True), self.tpPos))

	def CheckOut(self, agent):
		if (agent in self.lstPresence):
			self.lstPresence.remove(agent)
			agent.bChecked = False
			if (GlobalsU.Verbose()):
				print('%s fez CheckOut no cartorio %s' % (agent.ToString(short=True), self.tpPos))

	def CoupleArrived(self, nID, cMyGender):
		for ag in self.lstPresence:
			if (ag.nID == nID) and not (cMyGender == ag.cGender):
				return True
		return False

	def GetAgent(self, nID, cGender):
		for ag in self.lstPresence:
			if (ag.nID == nID) and (cGender == ag.cGender):
				return ag
		return None

	def CreateCouple(self, nMyID, nCoupleID, cMyGender):
		ag1 = self.GetAgent(nMyID, cMyGender)
		ag2 = self.GetAgent(nCoupleID, ConversionU.OpositeGender(cMyGender))

		ag1.bMarried = True
		ag1.nCoupleID = ag2.nID

		ag2.bMarried = True
		ag2.nCoupleID = ag1.nCoupleID
		ag2.tpPos = (-1,-1) #retira do mapa
		self.CheckOut(ag2)
		ag2.OnCartorio = None

		self.CheckOut(ag1)
		ag1.OnCartorio = None

		self.nNumberOfMarriages = self.nNumberOfMarriages + 1

	def DivorceCouple(self, ag):
		CoupleAg = field.GetCouple(ag.nCoupleID)
		ag.bMarried = False
		ag.nCoupleID = 0

		CoupleAg.bMarried = False
		CoupleAg.nCoupleID = 0
		CoupleAg.tpPos = (0,0) #TODO: pegar posição valida próxima a posição do cartorio
		CoupleAg.OnCartorio = ag.OnCartorio
		CoupleAg.OnCartorio.CheckIn(self)

		self.nNumberOfDivorces = self.nNumberOfDivorces + 1

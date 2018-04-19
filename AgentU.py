#
#	Definicao da classe agente
#

import ConstantsU
import GlobalsU
import ProposalU

from math import sqrt
from random import choice

class Agent:
	def __init__(self, ID, pref, gender):
		self.nID			= ID
		self.lstPreferences	= pref
		self.bMarried		= False
		self.nCoupleID		= 0
		self.cGender		= gender
		self.tpPos			= (0,0)
		self.lstCartorios	= []
		self.nFacing		= choice([ConstantsU.c_NORTE,
									ConstantsU.c_NORDESTE,
									ConstantsU.c_LESTE,
							 		ConstantsU.c_SUDESTE,
									ConstantsU.c_SUL,
									ConstantsU.c_SUDOESTE,
									ConstantsU.c_OESTE,
									ConstantsU.c_NOROESTE])

		self.LastAction = ConstantsU.c_OTHER
		self.Action 		= ConstantsU.c_OTHER

		self.lstProximity = []
		self.agMatch = None

		self.lstMadeProposes = []
		self.lstPendingProposes = []

	def CalculateEuclidianDistance(self):
		closest = (0,0)
		nBestDistance = 0
		nThisDistance = 0
		for cartorio in self.lstCartorios:
			nThisDistance = sqrt(((self.tpPos[0] - cartorio.tpPos[0])**2) + ((self.tpPos[1] - cartorio.tpPos[1])**2))

			if (nThisDistance < nBestDistance) or (nBestDistance == 0):
				nBestDistance = nThisDistance
				closest = cartorio.tpPos

		return closest

	def ChooseBestProposal(self):
		nBestMatch = -1
		if not (self.lstPendingProposes == []):
			for prop in self.lstPendingProposes:
				if (nBestMatch == -1) or (nBestMatch < prop.nAgentMadeProposeID):
					nBestMatch = prop.nAgentMadeProposeID

			return nBestMatch
		else:
			return None

	def LookAround(self, field):
		self.lstProximity = []
		for i in range(-ConstantsU.c_VISION_RANGE, ConstantsU.c_VISION_RANGE + 1):
			if ((self.tpPos[0] + i) < 0) or ((self.tpPos[0] + i) > field.nSize) or ((self.tpPos[0] + i) == field.nSize):
				pass
			else:
				for j in range(-ConstantsU.c_VISION_RANGE, ConstantsU.c_VISION_RANGE + 1):
					if ((self.tpPos[1] + j) < 0) or ((self.tpPos[1] + j) > field.nSize) or ((self.tpPos[1] + j) == field.nSize):
						pass
					else:
						tpTempPos = (self.tpPos[0] + i, self.tpPos[1] + j)
						nFilled = field.GetPosition(tpTempPos)

						if (nFilled == ConstantsU.c_Agent):
							ag = field.GetAgent(tpTempPos)
							if not (ag.ToString(short=True) == self.ToString(short=True)):
								self.lstProximity.append(ag)
								if GlobalsU.Verbose():
									print('%s Spotted: %s' % (self.ToString(short=True), ag.ToString()))

	def ChooseAction(self):
		self.LastAction = self.Action
		self.Action = ConstantsU.c_OTHER
		self.agMatch = None

		BestProposal = self.ChooseBestProposal()

		if (self.lstProximity == []):
			self.Action = ConstantsU.c_STEP
		else:
			for ag in self.lstProximity:
				if (self.agMatch == None) and not (ag.cGender == self.cGender):
					self.agMatch = ag
				elif (self.agMatch == None) and (ag.cGender == self.cGender):
					pass
				elif (self.agMatch.nID < ag.nID) and not (ag.cGender == self.cGender):
					self.agMatch = ag

			if not (self.agMatch == None) and not (BestProposal == None):
				if (self.agMatch.nID < BestProposal) and not (self.bMarried):
					self.Action = ConstantsU.c_MARRY
				elif (self.agMatch.nID < BestProposal) and (self.bMarried):
					if (self.nCoupleID < BestProposal):
						self.Action = ConstantsU.c_DIVORCE
					else:
						self.Action = ConstantsU.c_STEP
			elif (self.agMatch == None) and not (BestProposal == None):
				if (self.bMarried) and (self.nCoupleID < BestProposal):
					self.Action = ConstantsU.c_DIVORCE
				elif not (self.bMarried):		
					self.Action = ConstantsU.c_MARRY		
				else:
					self.Action = ConstantsU.c_STEP
			elif not (self.agMatch == None) and (BestProposal == None):
				if (self.bMarried) and (self.nCoupleID < self.agMatch.nID):
					self.Action = ConstantsU.c_PROPOSE
				elif not (self.bMarried):
					self.Action = ConstantsU.c_PROPOSE
				else:
					self.Action = ConstantsU.c_STEP
			else:
				self.Action = ConstantsU.c_STEP

		if GlobalsU.Verbose():
			print(ConstantsU.AcToStr(self.Action))

	def ExecuteAction(self, field):
		if (self.Action == ConstantsU.c_STEP):
			self.Step(field)
		elif (self.Action == ConstantsU.c_PROPOSE):
			self.Propose()
		elif (self.Action == ConstantsU.c_MARRY):
			#self.Marry()
			self.Step(field)
		elif (self.Action == ConstantsU.c_DIVORCE):
			#self.Divorce()
			self.Step(field)

	def Step(self, field):
		if GlobalsU.Verbose():
			print(ConstantsU.DirToStr(self.nFacing))

		field.SetPosition(self.tpPos, ConstantsU.c_Clear)
		tpStep = self.CalculateNextStep(field)
		self.tpPos = (tpStep[0], tpStep[1])
		field.SetPosition(self.tpPos, ConstantsU.c_Agent)

	def Propose(self):
		if GlobalsU.Verbose():
			print('%s Fazendo proposta de casamento para %s' %(self.ToString(short=True), self.agMatch.ToString(short=True)))
		prpPropose = ProposalU.Proposal(self.nID, self.agMatch.nID)
		self.lstMadeProposes.append(prpPropose)
		self.agMatch.lstPendingProposes.append(prpPropose)

	def Marry(self):
		print('Casando')

	def Divorce(self):
		print('Divorciando')

	def VerifyStep(self, tpStep, field):
		if (tpStep[0] > field.nSize -1):
			return False
		if (tpStep[1] > field.nSize -1):
			return False
		if (tpStep[0] < 0):
			return False
		if (tpStep[1] < 0):
			return False
		if not (field.GetPosition(tpStep) == ConstantsU.c_Clear):
			return False

		return True

	def CalculateNextStep(self, field):
		bOK = False
		while not bOK:
			if (self.nFacing == ConstantsU.c_NORTE):
				tpStep = (self.tpPos[0] - 1, self.tpPos[1])

			elif(self.nFacing == ConstantsU.c_NORDESTE):
				tpStep = (self.tpPos[0] - 1, self.tpPos[1] + 1)

			elif(self.nFacing == ConstantsU.c_LESTE):
				tpStep = (self.tpPos[0], self.tpPos[1] + 1)

			elif(self.nFacing == ConstantsU.c_SUDESTE):
				tpStep = (self.tpPos[0] + 1, self.tpPos[1] + 1)

			elif(self.nFacing == ConstantsU.c_SUL):
				tpStep = (self.tpPos[0] + 1, self.tpPos[1])

			elif(self.nFacing == ConstantsU.c_SUDOESTE):
				tpStep = (self.tpPos[0] + 1, self.tpPos[1] - 1)

			elif(self.nFacing == ConstantsU.c_OESTE):
				tpStep = (self.tpPos[0], self.tpPos[1] - 1)

			elif(self.nFacing == ConstantsU.c_NOROESTE):
				tpStep = (self.tpPos[0] - 1, self.tpPos[1] - 1)

			if self.VerifyStep(tpStep, field):
				bOK = True
			else:
				self.nFacing = choice([ConstantsU.c_NORTE, ConstantsU.c_NORDESTE, ConstantsU.c_LESTE,
										ConstantsU.c_SUDESTE,	ConstantsU.c_SUL, ConstantsU.c_SUDOESTE,
										ConstantsU.c_OESTE,	ConstantsU.c_NOROESTE])
		return tpStep

	def ToString(self, short=False):
		if short:
			return str(self.nID) + self.cGender
		else:
			return str(self.nID) + ' - ' + self.cGender + ' - '  + str(self.lstPreferences)

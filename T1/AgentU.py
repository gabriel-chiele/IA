#
#	Definicao da classe agente
#

import ConstantsU
import GlobalsU
import ProposalU
import UtilsU
import ConversionU

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
		self.lstPathToCartorio = []
		self.tpCartorioPos = (-1,-1)
		self.OnCartorio = None
		self.bArrived	= False
		self.bChecked	= False
		self.nFacing	= choice([ConstantsU.c_NORTE,
									ConstantsU.c_NORDESTE,
									ConstantsU.c_LESTE,
							 		ConstantsU.c_SUDESTE,
									ConstantsU.c_SUL,
									ConstantsU.c_SUDOESTE,
									ConstantsU.c_OESTE,
									ConstantsU.c_NOROESTE])

		self.Action 	= ConstantsU.c_STEP

		self.lstProximity = []
		self.agMatch = None

		self.MadePropose = None
		self.AcceptedPropose = None
		self.lstPendingProposes = []

	def ChooseBestProposal(self):
		propBest = None
		if not (self.lstPendingProposes == []):
			for prop in self.lstPendingProposes:
				if (propBest == None) or (propBest.nAgentMadeProposeID < prop.nAgentMadeProposeID):
					propBest = prop

		return propBest

	def FilterPreference(self):
		agBest = None
		if not (self.lstProximity == []):
			for ag in self.lstProximity:
				if not (ag.cGender == self.cGender):
					if ((agBest == None) or (agBest.nID < ag.nID)):
						agBest = ag
		return agBest

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
							if not (ag == None):
								if not (ag.ToString(short=True) == self.ToString(short=True)):
									self.lstProximity.append(ag)
									if GlobalsU.Verbose():
										print('%s Spotted: %s' % (self.ToString(short=True), ag.ToString()))

	def ChooseAction(self):
		if (self.Action == ConstantsU.c_STEP) or (self.Action == ConstantsU.c_PROPOSE):
			if not (self.MadePropose == None):
				bAccepted = self.MadePropose.CheckProposeResponse()
				if (bAccepted):
					self.Action = ConstantsU.c_MARRY
					return None
				else:
					self.MadePropose = None
			if not (self.lstPendingProposes == []):
				prop = self.ChooseBestProposal()
				if (self.bMarried) and (self.nCoupleID < prop.nAgentMadeProposeID):
					prop.Accept()
					self.AcceptedPropose = prop
					self.Action = ConstantsU.c_DIVORCE
					return None
				else:
					prop.Accept()
					self.AcceptedPropose = prop
					self.Action = ConstantsU.c_MARRY
					return None
			if not (self.lstProximity == []):
				ag = self.FilterPreference()
				if not (ag == None):
					if ((self.bMarried) and (self.nCoupleID < ag.nID)) or not (self.bMarried) :
						self.agMatch = ag
						self.Action = ConstantsU.c_PROPOSE
						return None
			if (self.lstProximity == []):
				self.Action = ConstantsU.c_STEP

		if (self.Action == ConstantsU.c_MARRY):
			if (self.bMarried) and not (self.tpPos == (-1,-1)):
				self.Action = ConstantsU.c_STEP
			elif(self.bMarried) and (self.tpPos == (-1,-1)):
				self.Action = ConstantsU.c_OTHER

		if (self.Action == ConstantsU.c_DIVORCE):
			print('completar')

		if (self.Action == ConstantsU.c_OTHER):
			print('Fora do mapa')

	def ExecuteAction(self, field):
		if (self.Action == ConstantsU.c_STEP):
			self.Step(field)
		elif (self.Action == ConstantsU.c_PROPOSE):
			self.Propose()
		elif (self.Action == ConstantsU.c_MARRY):
			self.Marry(field)
		elif (self.Action == ConstantsU.c_DIVORCE):
			#self.Divorce()
			self.Step(field)

	def Step(self, field):
		if GlobalsU.Verbose():
			print(ConversionU.DirToStr(self.nFacing))

		field.SetPosition(self.tpPos, ConstantsU.c_Clear)
		tpStep = self.CalculateNextStep(field)
		self.tpPos = (tpStep[0], tpStep[1])
		if not (self.bMarried):
			field.SetPosition(self.tpPos, ConstantsU.c_Agent)
		else:
			field.SetPosition(self.tpPos, ConstantsU.c_Couple)

	def Propose(self):
		if GlobalsU.Verbose():
			print('%s Fazendo proposta de casamento para %s' %(self.ToString(short=True), self.agMatch.ToString(short=True)))
		self.tpCartorioPos = UtilsU.CalculateEuclidianDistance(self.tpPos, self.lstCartorios)
		prpPropose = ProposalU.Proposal(self.nID, self.agMatch.nID, self.tpCartorioPos)
		self.MadePropose = prpPropose
		self.agMatch.lstPendingProposes.append(prpPropose)

	def Marry(self, field):
		if (self.MadePropose == None):
			self.agMatch = field.GetCouple(self.AcceptedPropose.nAgentMadeProposeID, ConversionU.OpositeGender(self.cGender))
			self.tpCartorioPos = self.AcceptedPropose.tpCartorio
		elif(self.AcceptedPropose == None):
			self.agMatch = field.GetCouple(self.MadePropose.nAgentProposedID, ConversionU.OpositeGender(self.cGender))

		if GlobalsU.Verbose():
			print('%s Casando com %s' %(self.ToString(short=True), self.agMatch.ToString(short=True)))

		if (self.lstPathToCartorio == []) and not (self.bArrived):
			From = UtilsU.AStarSearch(field, self.tpPos, self.tpCartorioPos)
			self.lstPathToCartorio = UtilsU.ReconstructPath(From, self.tpPos, self.tpCartorioPos)
			if GlobalsU.Verbose():
				print('Caminho para o cartorio: %s' %(self.lstPathToCartorio))
		elif not (len(self.lstPathToCartorio) < 1):
			field.SetPosition(self.tpPos, ConstantsU.c_Clear)
			self.tpPos = (self.lstPathToCartorio[0][0], self.lstPathToCartorio[0][1])
			field.SetPosition(self.tpPos, ConstantsU.c_Agent)
			self.lstPathToCartorio.pop(0)
			if (self.lstPathToCartorio == []):
				self.bArrived = True
				print(self.tpCartorioPos)
				self.OnCartorio = field.GetCartorio(self.tpCartorioPos)
			if GlobalsU.Verbose():
				print('Caminho para o cartorio : %s' %(self.lstPathToCartorio))
		elif (self.lstPathToCartorio == []) and (self.bArrived) and not (self.bChecked):
			self.OnCartorio.CheckIn(self)
		else:
			if not (self.MadePropose == None):
				bCoupleArrived = self.OnCartorio.CoupleArrived(self.MadePropose.nAgentProposedID, self.cGender)
				if (bCoupleArrived):
					field.SetPosition(field.GetCouple(self.MadePropose.nAgentProposedID, ConversionU.OpositeGender(self.cGender)).tpPos, ConstantsU.c_Clear)
					self.OnCartorio.CreateCouple(self.nID, self.MadePropose.nAgentProposedID, self.cGender)
					self.MadePropose = None
					self.bArrived = False

	def Divorce(self):
		if GlobalsU.Verbose():
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

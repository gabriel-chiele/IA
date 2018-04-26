#
#	Definicao da classe agente
#

import ConstantsU
import GlobalsU
import ProposalU
import UtilsU

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
		self.OnCartorio = None
		self.bArrived	= False
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
		self.lstPendingProposes = []
		self.bAcceptedPropose = False

	def ChooseBestProposal(self):
		nBestMatch = -1
		propBest = None
		if not (self.lstPendingProposes == []):
			for prop in self.lstPendingProposes:
				if (nBestMatch == -1) or (nBestMatch < prop.nAgentMadeProposeID):
					nBestMatch = prop.nAgentMadeProposeID

			for prop in self.lstPendingProposes:
				if (prop.nAgentMadeProposeID == nBestMatch):
					return prop

	def FilterPreference(self):
		agBest = None
		if not (self.lstProximity == []):
			for ag in self.lstProximity:
				if (agBest == None) or (agBest.nID < ag.nID):
					agBest = ag
		return ag

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
		if (self.Action == ConstantsU.c_STEP) or (self.Action == ConstantsU.c_PROPOSE):
			if not (self.MadePropose == None):
				bAccepted = self.MadePropose.CheckProposeResponse()
				if (bAccepted):
					self.Action = ConstantsU.c_MARRY
					self.bAcceptedPropose = True
					return None
				else:
					self.bAcceptedPropose = False
					self.MadePropose = None
			if not (self.lstPendingProposes == []):
				prop = self.ChooseBestProposal()
				if (self.bMarried) and (self.nCoupleID < prop.nAgentMadeProposeID):
					prop.Accept()
					self.bAcceptedPropose = True
					self.Action = ConstantsU.c_DIVORCE
					return None
				else:
					prop.Accept()
					self.bAcceptedPropose = True
					self.Action = ConstantsU.c_MARRY
					return None
			if not (self.lstProximity == []):
				ag = self.FilterPreference()
				if ((self.bMarried) and (self.nCoupleID < ag.nID)) or not (self.bMarried) :
					self.agMatch = ag
					self.Action = ConstantsU.c_PROPOSE
					return None
			if (self.lstProximity == []):
				self.Action = ConstantsU.c_STEP

		if (self.Action == ConstantsU.c_MARRY):
			print('completar...')

		if (self.Action == ConstantsU.c_DIVORCE):
			print('completar...')

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
			print(UtilsU.DirToStr(self.nFacing))

		field.SetPosition(self.tpPos, ConstantsU.c_Clear)
		tpStep = self.CalculateNextStep(field)
		self.tpPos = (tpStep[0], tpStep[1])
		field.SetPosition(self.tpPos, ConstantsU.c_Agent)

	def Propose(self):
		if GlobalsU.Verbose():
			print('%s Fazendo proposta de casamento para %s' %(self.ToString(short=True), self.agMatch.ToString(short=True)))
		prpPropose = Proself.PathToCartorioposalU.Proposal(self.nID, self.agMatch.nID)
		self.lstMadeProposes.append(prpPropose)
		self.agMatch.lstPendingProposes.append(prpPropose)

	def Marry(self, field):
		if GlobalsU.Verbose():
			print('%s Casando com %s' %(self.ToString(short=True), self.agMatch.ToString(short=True)))

		if (self.lstPathToCartorio == []) and not (bArrived):
			tpCartorioPos = UtilsU.CalculateEuclidianDistance(self.lstCartorios)
			self.lstPathToCartorio = UtilsU.AStartSearch(field,self.tpPos,tpCartorioPos)
		elif not (len(self.lstPathtoCartorio) == 1):
			field.SetPosition(self.tpPos, ConstantsU.c_Clear)
			self.tpPos = (self.lstPathToCartorio[0][0], self.lstPathToCartorio[0][1])
			field.SetPosition(self.tpPos, ConstantsU.c_Agent)
			self.lstPathToCartorio.pop(0)
		elif (len(self.lstPathToCartorio) == 1):
			self.bArrived = True
			self.OnCartorio = field.GetCartorio(self.lstPathToCartorio[0])
			self.OnCartorio.CheckIn(self)
			self.lstPathToCartorio.pop(0)
		else:
			#bArrived = self.OnCartorio.CoupleArrived()
			# se chegou cria casal
			# senão espera

	#	TODO: armazenar a proposta aceita nos dois agentes
	#				neste else verificar se eu fiz a proposta ou se eu aceitei a proposta feita
	#				dependendo disto eu pego o ID do outro agente e verifica se ele esta presente no cartorio
	#				se ele estiver cria casal
	#				senão espera
			
			
				

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

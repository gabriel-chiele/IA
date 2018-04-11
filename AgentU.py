#
#	Definicao da classe agente
#

import ConstantsU
import GlobalsU

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

	def LookAround(self, field):
		lstProximity = []		
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
								lstProximity.append(ag)
								if GlobalsU.Verbose():
									print('%s Spotted: %s' % (self.ToString(short=True), ag.ToString()))

		return lstProximity

	def ChooseAction(self, lstProximity):
		action = ConstantsU.c_OTHER
		if (lstProximity == []):
			action = ConstantsU.c_STEP
		else:
			for ag in lstProximity:
				if (self.bMarried):
					if (ag.nID > self.nCoupleID) and not (ag.cGender == self.cGender):
						action = ConstantsU.c_DIVORCE
					else:
						action = ConstantsU.c_STEP
				elif not (ag.cGender == self.cGender):
					action = ConstantsU.c_MARRY
				else:
					action = ConstantsU.c_STEP
					
		if GlobalsU.Verbose():
			print(ConstantsU.AcToStr(action))		
		return action # oq fazer se casado e nID menor que o nCoupleID ? talvez STEP
			

	def Step(self, field):
		if GlobalsU.Verbose():
			print(ConstantsU.DirToStr(self.nFacing))

		bOK = False
		field.SetPosition(self.tpPos, ConstantsU.c_Clear)

		while not bOK:
			if (self.nFacing == ConstantsU.c_NORTE):
				self.tpPos = (self.tpPos[0] - 1, self.tpPos[1])

			elif(self.nFacing == ConstantsU.c_NORDESTE):
				self.tpPos = (self.tpPos[0] - 1, self.tpPos[1] + 1)

			elif(self.nFacing == ConstantsU.c_LESTE):
				self.tpPos = (self.tpPos[0], self.tpPos[1] + 1)

			elif(self.nFacing == ConstantsU.c_SUDESTE):
				self.tpPos = (self.tpPos[0] + 1, self.tpPos[1] + 1)

			elif(self.nFacing == ConstantsU.c_SUL):
				self.tpPos = (self.tpPos[0] + 1, self.tpPos[1])

			elif(self.nFacing == ConstantsU.c_SUDOESTE):
				self.tpPos = (self.tpPos[0] + 1, self.tpPos[1] - 1)

			elif(self.nFacing == ConstantsU.c_OESTE):
				self.tpPos = (self.tpPos[0], self.tpPos[1] - 1)

			elif(self.nFacing == ConstantsU.c_NOROESTE):
				self.tpPos = (self.tpPos[0] - 1, self.tpPos[1] - 1)

			if self.VerifyStep(self.tpPos, field):
				bOK = True
			else:
				print('Mudou de direcao')
				self.nFacing = choice([ConstantsU.c_NORTE, ConstantsU.c_NORDESTE, ConstantsU.c_LESTE,
										ConstantsU.c_SUDESTE,	ConstantsU.c_SUL, ConstantsU.c_SUDOESTE,
										ConstantsU.c_OESTE,	ConstantsU.c_NOROESTE])

		field.SetPosition(self.tpPos, ConstantsU.c_Agent)

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

	def Chase(self):
		print('marry')

	def GoToCartorio(self):
		print('divorce')


	def ToString(self, short=False):
		if short:
			return str(self.nID) + self.cGender
		else:
			return str(self.nID) + ' - ' + self.cGender + ' - '  + str(self.lstPreferences)


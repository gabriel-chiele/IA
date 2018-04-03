#
#	Definicao da classe agente
#

import ConstantsU
import GlobalsU

from math import sqrt

class Agent:
	def __init__(self, ID, pref, gender):
		self.nID						= ID	
		self.lstPreferences	= pref
		self.bMarried				= False
		self.nCoupleID			= 0
		self.cGender				= gender
		self.tpPos					= (0,0)
		self.lstCartorios		= []
		self.nFacing				= ConstantsU.c_NORTE

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
					action = ConstantsU.c_MARRY
					
		if GlobalsU.Verbose():
			print(ConstantsU.AcToStr(action))		
		return action # oq fazer se casado e nID menor que o nCoupleID ? talvez STEP
			

	def Step(self):
		print('step')

	def ToString(self, short=False):
		if short:
			return str(self.nID) + self.cGender
		else:
			return str(self.nID) + ' - ' + self.cGender + ' - '  + str(self.lstPreferences)


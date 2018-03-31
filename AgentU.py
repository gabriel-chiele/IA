#
#	Definicao da classe agente
#

import ConstantsU

from math import sqrt

class Agent:
	def __init__(self, ID, pref, gender):
		self.nID 			= ID	
		self.lstPreferences	= pref
		self.bMarried 		= False
		self.nCoupleID		= 0
		self.cGender		= gender
		self.tpPos			= (0,0)
		self.lstCartorios	= []
		self.nFacing		= ConstantsU.c_NORTE

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
		# TODO: clocar o agente em lista temporaria e depois verificar a preferencia
		# entre todos os agentes na lista, e me direcionar ao de maior rank
		for i in range(-ConstantsU.c_VISION_RANGE, ConstantsU.c_VISION_RANGE):
			if (self.tpPos[0] + i) < 0:
				pass
			elif (self.tpPos[0] + i) > field.nSize:
				pass
			else:
				for j in range(-ConstantsU.c_VISION_RANGE, ConstantsU.c_VISION_RANGE):
					if (self.tpPos[1] + i) < 0:
						pass
					elif (self.tpPos[1] + i) > field.nSize:
						pass
					else:
						tpTempPos = (tpPos[0] + i, tpPos[1] + j)
						nFilled = field.GetPosition(tpTempPos)

						if (nFilled == c_Agent):
							ag = field.getAgent(tpTempPos)

	def ToString(self):
		return str(self.nID) + ' - ' + self.cGender + ' - '  + str(self.lstPreferences)

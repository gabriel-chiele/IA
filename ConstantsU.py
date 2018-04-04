#
#	Modulo de constante
#

#
#	constantes representacao dos objetos
#
c_Clear    = 0
c_Cartorio = 1
c_Wall     = 2
c_Agent    = 3
c_Couple   = 4

def ObjToStr(nObj, short=False):
	if(nObj == c_Clear):
		if short:
			sObj = '  '
		else:
			sObj = 'VAZIO'
	elif (nObj == c_Cartorio):
		if short:
			sObj = 'CT'
		else:
			sObj = 'CARTORIO'
	elif (nObj == c_Wall):
		if short:
			sObj = '||'
		else:
			sObj = 'PAREDE'
	elif (nObj == c_Agent):
		if short:
			sObj = 'AG'
		else:
			sObj = 'AGENTE'
	elif (nObj == c_Couple):
		if short:
			sObj = 'CP'
		else:
			sObj = 'CASAL'

	return sObj

#
#	constantes de direcao
#
c_NORTE		= 0
c_NORDESTE= 1	
c_LESTE		= 2
c_SUDESTE	= 3
c_SUL			= 4
c_SUDOESTE= 5
c_OESTE 	= 6
c_NOROESTE= 7
c_NENHUMA	= 8


def DirToStr(nDir):
	if(nDir == c_NORTE):
		sDir = 'NORTE'
	elif (nDir == c_NORDESTE):
		sDir = 'NORDESTE'
	elif (nDir == c_LESTE):
		sDir = 'LESTE'
	elif (nDir == c_SUDESTE):
		sDir = 'SUDESTE'
	elif (nDir == c_SUL):
		sDir = 'SUL'
	elif (nDir == c_SUDOESTE):
		sDir = 'SUDOESTE'
	elif (nDir == c_OESTE):
		sDir = 'OESTE'
	elif (nDir == c_NOROESTE):
		sDir = 'NORDESTE'
	elif (nDir == c_NENHUMA):
		sDir = 'NENHUMA'

	return sDir

#
#	constantes de genero
#
c_MALE 		= 'M'
c_FEMALE	= 'F'

#
#	constantes de acao
#
c_STEP		= 0
c_DIVORCE = 1
c_MARRY		= 2
c_OTHER		= 255

def AcToStr(nAc):
	if(nAc == c_STEP):
		sAc = 'PASSO'
	elif (nAc == c_DIVORCE):
		sAc = 'DIVORCIO'
	elif (nAc == c_MARRY):
		sAc = 'CASAR'
	elif (nAc == c_OTHER):
		sAc = 'OUTRO'

	return sAc

#
#	constantes de variacao
#
c_SIZE_VARIATION 			= 4
c_VISION_RANGE				= 2
c_FIELD_SIZE_FACTOR 	= 5
c_WALL_SPACING_FACTOR = 3
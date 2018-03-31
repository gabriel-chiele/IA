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

def ObjToStr(nObj):
	if(nObj == c_Clear):
		sObj = 'VAZIO'
	elif (nObj == c_Cartorio):
		sObj = 'CARTORIO'
	elif (nObj == c_Wall):
		sObj = 'PAREDE'
	elif (nObj == c_Agent):
		sObj = 'AGENTE'
	elif (nObj == c_Couple):
		sObj = 'CASAL'

	return sObj

#
#	constantes de direcao
#
c_NORTE 	= 0
c_NORDESTE  = 1	
c_LESTE 	= 2
c_SUDESTE 	= 3
c_SUL		= 4
c_SUDOESTE  = 5
c_OESTE 	= 6
c_NOROESTE  = 7
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
#	constantes do mapa
#
c_SIZE_VARIATION = 4
#
# Definicao de metodos de conversão de dados
#

import ConstantsU

def ActionToStr(nAc):
	if(nAc == ConstantsU.c_STEP):
		sAc = 'PASSO'
	elif (nAc == ConstantsU.c_DIVORCE):
		sAc = 'DIVORCIO'
	elif (nAc == ConstantsU.c_MARRY):
		sAc = 'CASAR'
	elif (nAc == ConstantsU.c_PROPOSE):
		sAc = 'FAZER PEDIDO'
	elif (nAc == ConstantsU.c_OTHER):
		sAc = 'OUTRO'

	return sAc

def DirToStr(nDir):
	if(nDir == ConstantsU.c_NORTE):
		sDir = 'NORTE'
	elif (nDir == ConstantsU.c_NORDESTE):
		sDir = 'NORDESTE'
	elif (nDir == ConstantsU.c_LESTE):
		sDir = 'LESTE'
	elif (nDir == ConstantsU.c_SUDESTE):
		sDir = 'SUDESTE'
	elif (nDir == ConstantsU.c_SUL):
		sDir = 'SUL'
	elif (nDir == ConstantsU.c_SUDOESTE):
		sDir = 'SUDOESTE'
	elif (nDir == ConstantsU.c_OESTE):
		sDir = 'OESTE'
	elif (nDir == ConstantsU.c_NOROESTE):
		sDir = 'NORDESTE'
	elif (nDir == ConstantsU.c_NENHUMA):
		sDir = 'NENHUMA'

	return sDir

def ObjToStr(nObj, short=False):
	if(nObj == ConstantsU.c_Clear):
		if short:
			sObj = '  '
		else:
			sObj = 'VAZIO'
	elif (nObj == ConstantsU.c_Cartorio):
		if short:
			sObj = 'CT'
		else:
			sObj = 'CARTORIO'
	elif (nObj == ConstantsU.c_Wall):
		if short:
			sObj = '||'
		else:
			sObj = 'PAREDE'
	elif (nObj == ConstantsU.c_Agent):
		if short:
			sObj = 'AG'
		else:
			sObj = 'AGENTE'
	elif (nObj == ConstantsU.c_Couple):
		if short:
			sObj = 'CP'
		else:
			sObj = 'CASAL'

	return sObj

def OpositeGender(cGender):
	if(cGender == ConstantsU.c_MALE):
		return ConstantsU.c_FEMALE
	else:
		return ConstantsU.c_MALE

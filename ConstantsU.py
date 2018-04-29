#
#	Modulo de constante
#

import GlobalsU

#
#	constantes representacao dos objetos
#
c_Clear    = 0
c_Cartorio = 1
c_Wall     = 2
c_Agent    = 3
c_Couple   = 4

#
#	constantes de direcao
#
c_NORTE		= 0
c_NORDESTE	= 1
c_LESTE		= 2
c_SUDESTE	= 3
c_SUL		= 4
c_SUDOESTE	= 5
c_OESTE 	= 6
c_NOROESTE	= 7
c_NENHUMA	= 8

#
#	constantes de genero
#
c_MALE 		= 'M'
c_FEMALE	= 'F'

#
#	constantes de acao
#
c_STEP		= 0
c_DIVORCE 	= 1
c_MARRY		= 2
c_PROPOSE	= 3
c_OTHER		= 255

#
#	constantes de variacao
#
c_SIZE_VARIATION 		= 4
c_VISION_RANGE			= 2
c_FIELD_SIZE_FACTOR		= 5
c_WALL_SPACING_FACTOR 	= 3
c_MAX_TURNS				= 100
c_TURN_CLOCK	        = 0.5

#
#	constantes textuais
#
tc_Title 			= '\nTrabalho da disciplina de Inteligencia Artificial'
tc_Authors 			= '\nAutores'
tc_Name1 			= '\nGabriel Chiele'
tc_Name2 			= '\nMaiki Buffet'
tc_StartScreen 		= tc_Title + tc_Authors + tc_Name1 + tc_Name2
tc_EndOfSimulation 	= '\nSimulacao encerrada!'
tc_ExecutionTime	= '\n\nTempo total de execucao : %i segundos'
tc_EndScreen 		= tc_EndOfSimulation + tc_ExecutionTime

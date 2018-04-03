#
# Main
#

import AgentU
import FieldU
import UtilsU
import GlobalsU

if __name__ == '__main__':
	options = None
	conf = None

	options = UtilsU.ParseOption()
	
	if options == None:
		GlobalsU.setEndSimulation(True)
	else:
		conf = UtilsU.LoadConfigurations(options)

	if (conf == None):
		print('Arquivo de configuracao da simulacao invalido!')
		GlobalsU.setEndSimulation(True)
	else:
		conf.PrintConf()
		Field = FieldU.Field(conf)
		UtilsU.EraseConf(conf)
		Field.PrintMap()

		nTurnCount = 0

		print('Simulando...')
		while not (GlobalsU.EndSimulation()):			
			nTurnCount = nTurnCount + 1
			print('\nTurno %i:' % (nTurnCount))

			for ag in Field.lstAgents:
				lstProximity = ag.LookAround(Field)
				action = ag.ChooseAction(lstProximity)

			GlobalsU.setEndSimulation(True)		

	UtilsU.EndCredits()

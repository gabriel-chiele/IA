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
		Field.PrintMap()

		while (GlobalsU.EndSimulation()):
			print('Simulando...')
			GlobalsU.setEndSimulation(True)		

	UtilsU.EndCredits()

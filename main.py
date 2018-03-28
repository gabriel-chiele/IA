#
# Main
#

import AgentU
import FieldU
import UtilsU
import GlobalsU

if __name__ == '__main__':
	options = UtilsU.ParseOption()
	
	if options == None:
		EndCredits()
		sys.exit()

	conf = UtilsU.LoadConfigurations(options)
	if not (conf == None):
		conf.PrintConf()
		Field = FieldU.Field(conf)
		Field.PrintMap()
	else:
		print('Arquivo de configuracao da simulacao invalido!')

	UtilsU.EndCredits()

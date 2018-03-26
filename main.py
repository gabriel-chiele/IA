from AgentU import *
import FieldU
import UtilsU

if __name__ == '__main__':
	options = UtilsU.ParseOption()
	
	if options == None:
		EndCredits(True)
		sys.exit()

	conf = UtilsU.LoadFile(options.filename)

	if not (conf == None):	
		Field = UtilsU.GenerateField(options.size, conf.nCartoriosNumber)
	else:
		print('Arquivo de configuracao da simulacao invalido!')

	Field.PrintMap();

	UtilsU.EndCredits(False);

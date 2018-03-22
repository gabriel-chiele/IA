from AgentU import *
import FieldU
import UtilsU

if __name__ == '__main__':
	options = UtilsU.ParseOption()
	UtilsU.LoadFile(options.filename)
	
	if options == nil:
		EndCredits()
		sys.exit()

	Field = UtilsU.GenerateField(options.size,options.cartorios)

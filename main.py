#
# Main
#

import AgentU
import FieldU
import UtilsU
import GlobalsU
import ConstantsU

from time import sleep, time
from tkinter import *

class Application(Frame):
		def run(self):
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
				dtStartTime = time()
				while not (GlobalsU.EndSimulation()):			
					nTurnCount = nTurnCount + 1
					print('\nTurno %i:' % (nTurnCount))

					for ag in Field.lstAgents:
						lstProximity = ag.LookAround(Field)
						action = ag.ChooseAction(lstProximity)

						if (action == ConstantsU.c_STEP):
							ag.Step(Field)
						elif (action == ConstantsU.c_MARRY):
							ag.Step(Field)#Chase()
						elif (action == ConstantsU.c_DIVORCE):
							ag.Step(Field)#GoToCartorio()

						sleep(0.5)

					Field.PrintMap()
					if(nTurnCount == 100):
						GlobalsU.setEndSimulation(True)	

				dtEndTime = time()

			UtilsU.EndCredits(dtEndTime - dtStartTime)

		def createWidgets(self):
			self.QUIT = Button(self)
			self.QUIT["text"] = "QUIT"
			self.QUIT["fg"]   = "red"
			self.QUIT["command"] =  self.quit

			self.QUIT.pack({"side": "left"})

			self.START = Button(self)
			self.START["text"] = "Start"
			self.QUIT["fg"]   = "green"
			self.START["command"] = self.run

			self.START.pack({"side": "left"})

		def __init__(self, master=None):
			Frame.__init__(self, master)
			self.pack()
			self.createWidgets()

if __name__ == '__main__':
	root = Tk()
	app = Application(master=root)
	app.mainloop()
	root.destroy()










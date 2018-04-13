#
# Definicao da classe visual
#

import AgentU
import FieldU
import UtilsU
import GlobalsU
import ConstantsU

from time import sleep, time
from tkinter import *

class Visual(Frame):
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
				print('Turno %i:' % (nTurnCount))

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
				if(nTurnCount == ConstantsU.c_MAX_TURNS):
					GlobalsU.setEndSimulation(True)	

			dtEndTime = time()

		UtilsU.EndCredits(dtEndTime - dtStartTime)

	def createWidgets(self):
		self.lblTitleScreen = Label(self)
		self.lblTitleScreen['text'] = ConstantsU.tc_Screen
		self.lblTitleScreen['bg'] = "white"
		self.lblTitleScreen.grid(row=0,column=0,columnspan=2)

		self.btQuit = Button(self)
		self.btQuit["text"] = "Quit"
		self.btQuit['bg'] = "white"
		self.btQuit["fg"]   = "red"
		self.btQuit["command"] =  self.quit
		self.btQuit.grid(row=1, column=0, sticky=W+E)

		self.btStart = Button(self)
		self.btStart["text"] = "Start"
		self.btStart['bg'] = "white"
		self.btStart["fg"]   = "green"
		self.btStart["command"] = self.run
		self.btStart.grid(row=1, column=1, sticky=W+E)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

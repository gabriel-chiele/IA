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
		try :
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
				self.CreateGrid(Field)
				dtStartTime = time()
				while not (GlobalsU.EndSimulation()):			
					nTurnCount = nTurnCount + 1
					print('Turno %i:' % (nTurnCount))

					for ag in Field.lstAgents:
						ag.LookAround(Field)
						ag.ChooseAction()
						ag.ExecuteAction(Field)

					Field.PrintMap()
					self.UpdateGrid(Field)
					if(nTurnCount == ConstantsU.c_MAX_TURNS):
						GlobalsU.setEndSimulation(True)

					sleep(ConstantsU.c_TURN_CLOCK)

				dtEndTime = time()
				self.dtExecTime = dtEndTime - dtStartTime
				self.ForgetGrid(Field)
				UtilsU.EndCredits(self.dtExecTime)
				GlobalsU.setEndSimulation(False)
				self.EndMessage()
		except Exception as e:
			self.ErrorMessage(str(e))

	def ErrorMessage(self, strError):
		self.strText.set(strError)
		self.btQuit.grid(row=1, column=0, sticky=W+E)
		self.btStart.grid(row=1, column=1, sticky=W+E)

	def EndMessage(self):
		self.strText.set(ConstantsU.tc_EndScreen % self.dtExecTime)
		self.lblTitleScreen.grid(row=0,column=0,columnspan=2)
		self.btQuit.grid(row=1, column=0, sticky=W+E)
		self.btStart.grid(row=1, column=1, sticky=W+E)

	def StartSimulation(self):
		self.strText.set('Simulando...')
		self.btQuit.grid_forget()
		self.btStart.grid_forget()
		self.update()
		self.run()

	def UpdateGrid(self, field):
		self.PaintGrid(field)
		self.update()

	def CreateGrid(self, field):
		lstSlave = self.grid_slaves()
		for widget in lstSlave:
			widget.grid_forget()
		
		self.PaintGrid(field)

	def ForgetGrid(self, field):
		lstSlave = self.grid_slaves()
		for widget in lstSlave:
			widget.grid_forget()

	def PaintGrid(self, field):
		for i in range(field.nSize):
			for j in range(field.nSize):
				nItem = field.GetPosition((i,j))
				if (nItem == ConstantsU.c_Clear):
					frSquare = Frame(self, width=25, height=25, bg="white")
				elif (nItem == ConstantsU.c_Cartorio):
					frSquare = Frame(self, width=25, height=25, bg="yellow")
				elif (nItem== ConstantsU.c_Wall):
					frSquare = Frame(self, width=25, height=25, bg="blue")
				elif (nItem == ConstantsU.c_Agent):
					frSquare = Frame(self, width=25, height=25, bg="red")
				elif (nItem == ConstantsU.c_Couple):
					frSquare = Frame(self, width=25, height=25, bg="purple")			
				frSquare.grid(row=i, column=j)

	def createWidgets(self):
		self.strText = StringVar()
		self.strText.set(ConstantsU.tc_StartScreen)
		self.lblTitleScreen = Label(self, textvariable = self.strText) 
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
		self.btStart["command"] = self.StartSimulation
		self.btStart.grid(row=1, column=1, sticky=W+E)

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

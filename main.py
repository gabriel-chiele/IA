#
# Main
#

import VisualU

from tkinter import *

if __name__ == '__main__':
	root = Tk()
	root.wm_attributes('-type', 'splash')
	app = VisualU.Visual(master=root)
	app.mainloop()
	root.destroy()

from tkinter import *
from tkinter import ttk

import lss
import lss_const as lssc

# Constants
#CST_LSS_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
CST_LSS_Port = "COM3"				# For windows platforms
CST_LSS_Baud = lssc.LSS_DefaultBaud

# Create and open a serial port
lss.initBus(CST_LSS_Port, CST_LSS_Baud)

# Create LSS objects
mt  = motion(lss)

def goLimp():
	mt.estop()

def holdPosition():
	mt.freeze()

root = Tk()
root.title("LSS Arm Position Finder")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

base_angle = StringVar()
base_entry = ttk.Entry(mainframe, width=7, textvariable=base_angle)
base_entry.grid(column=1, row=2, sticky=(N, W, E), padx=5, pady=(0,5))

shoulder_angle = StringVar()
shoulder_entry = ttk.Entry(mainframe, width=7, textvariable=shoulder_angle)
shoulder_entry.grid(column=1, row=4, sticky=(N, W, E), padx=5, pady=(0,5))

elbow_angle = StringVar()
elbow_entry = ttk.Entry(mainframe, width=7, textvariable=elbow_angle)
elbow_entry.grid(column=1, row=6, sticky=(N, W, E), padx=5, pady=(0,5))

wrist_angle = StringVar()
wrist_entry = ttk.Entry(mainframe, width=7, textvariable=base_angle)
wrist_entry.grid(column=1, row=8, sticky=(N, W, E), padx=5, pady=(0,5))


ttk.Button(mainframe, text="Limp", command=goLimp).grid(column=3, row=2, padx=5, pady=5)

ttk.Button(mainframe, text="Hold", command=holdPosition).grid(column=3, row=4, padx=5, pady=5)

ttk.Label(mainframe, text="Base Position").grid(column=1, row=1, sticky=(S, W, E), padx=5, pady=(5,0))
ttk.Label(mainframe, text="Shoulder Position").grid(column=1, row=3, sticky=(S, W, E), padx=5, pady=(5,0))
ttk.Label(mainframe, text="Elbow Position").grid(column=1, row=5, sticky=(S, W, E), padx=5, pady=(5,0))
ttk.Label(mainframe, text="Wrist Position").grid(column=1, row=7, sticky=(S, W, E), padx=5, pady=(5,0))

base_entry.focus()

#root.bind("<Return>", calculate)

root.mainloop()
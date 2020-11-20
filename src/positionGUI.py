from tkinter import *
from tkinter import ttk

import lss
import lss_const as lssc

# for our arm's movement
from motion import motion


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

def Refresher():
	current_base.set(lss.LSS(1).getPosition())
	current_shoulder.set(lss.LSS(2).getPosition())
	current_elbow.set(lss.LSS(3).getPosition())
	current_wrist.set(lss.LSS(4).getPosition())
	root.after(50, Refresher)

def setBase():
	lss.LSS(1).move(base_angle.get())

def plus5Base():
	pass

def minus5Base():
	pass

def plus5Shoulder():
	pass

def minus5Shoulder():
	pass

def plus5Elbow():
	pass

def minus5Elbow():
	pass

def plus5Wrist():
	pass

def minus5Wrist():
	pass

def setShoulder():
	lss.LSS(2).move(shoulder_angle.get())

def setElbow():
	lss.LSS(3).move(elbow_angle.get())

def setWrist():
	lss.LSS(4).move(wrist_angle.get())

root = Tk()
root.title("LSS Arm Position Finder")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Position Labels
ttk.Label(mainframe, text="Base Position:").grid(column=1, row=1, sticky=(E), padx=(5,0), pady=5)
ttk.Label(mainframe, text="Shoulder Position:").grid(column=1, row=3, sticky=(E), padx=(5,0), pady=5)
ttk.Label(mainframe, text="Elbow Position:").grid(column=1, row=5, sticky=(E), padx=(5,0), pady=5)
ttk.Label(mainframe, text="Wrist Position:").grid(column=1, row=7, sticky=(E), padx=(5,0), pady=5)

#Read Angles
current_base = StringVar()
ttk.Label(mainframe, textvariable=current_base).grid(column=2, row=1, sticky=(W), padx=(0,5), pady=5)
current_shoulder = StringVar()
ttk.Label(mainframe, textvariable=current_shoulder).grid(column=2, row=3, sticky=(W), padx=(0,5), pady=5)
current_elbow = StringVar()
ttk.Label(mainframe, textvariable=current_elbow).grid(column=2, row=5, sticky=(W), padx=(0,5), pady=5)
current_wrist = StringVar()
ttk.Label(mainframe, textvariable=current_wrist).grid(column=2, row=7, sticky=(W), padx=(0,5), pady=5)


#Angles to Set To
base_angle = StringVar()
base_entry = ttk.Entry(mainframe, width=7, textvariable=base_angle)
base_entry.grid(column=1, row=2, sticky=(E), padx=5, pady=5)
shoulder_angle = StringVar()
shoulder_entry = ttk.Entry(mainframe, width=7, textvariable=shoulder_angle)
shoulder_entry.grid(column=1, row=4, sticky=(E), padx=5, pady=5)
elbow_angle = StringVar()
elbow_entry = ttk.Entry(mainframe, width=7, textvariable=elbow_angle)
elbow_entry.grid(column=1, row=6, sticky=(E), padx=5, pady=5)
wrist_angle = StringVar()
wrist_entry = ttk.Entry(mainframe, width=7, textvariable=wrist_angle)
wrist_entry.grid(column=1, row=8, sticky=(E), padx=5, pady=5)


#Command Buttons
ttk.Button(mainframe, text="Limp", command=goLimp).grid(column=5, row=2, padx=5, pady=5)
ttk.Button(mainframe, text="Hold", command=holdPosition).grid(column=5, row=4, padx=5, pady=5)
ttk.Button(mainframe, text="Set Base", command=setBase).grid(column=2, row=2, padx=5, pady=5)
ttk.Button(mainframe, width=3,text="+5", command=plus5Base).grid(column=3, row=2, padx=(5,0), pady=5)
ttk.Button(mainframe, width=3,text="-5", command=minus5Base).grid(column=4, row=2, padx=(0,5), pady=5)
ttk.Button(mainframe, text="Set Shoulder", command=setShoulder).grid(column=2, row=4, padx=5, pady=5)
ttk.Button(mainframe, width=3,text="+5", command=plus5Shoulder).grid(column=3, row=4, padx=(5,0), pady=5)
ttk.Button(mainframe, width=3,text="-5", command=minus5Shoulder).grid(column=4, row=4, padx=(0,5), pady=5)
ttk.Button(mainframe, text="Set Elbow", command=setElbow).grid(column=2, row=6, padx=5, pady=5)
ttk.Button(mainframe, width=3,text="+5", command=plus5Elbow).grid(column=3, row=6, padx=(5,0), pady=5)
ttk.Button(mainframe, width=3,text="-5", command=minus5Elbow).grid(column=4, row=6, padx=(0,5), pady=5)
ttk.Button(mainframe, text="Set Wrist", command=setWrist).grid(column=2, row=8, padx=5, pady=5)
ttk.Button(mainframe, width=3,text="+5", command=plus5Wrist).grid(column=3, row=8, padx=(5,0), pady=5)
ttk.Button(mainframe, width=3,text="-5", command=minus5Wrist).grid(column=4, row=8, padx=(0,5), pady=5)

base_entry.focus()
root.bind("<Escape>", goLimp())
root.bind("<Return>", holdPosition())
Refresher()
root.mainloop()
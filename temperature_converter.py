from Tkinter import *

#creating functions
def convertTemp():
	var = radio_button_var.get()
	temp = entry1.get()

	if var == 0: #F to C
	    temp_c = (float(temp) - 32) * 5/9
	    label2.config(text="Result: " + temp + "F " + "is equal to " + str(temp_c) + "C.")
	elif var == 1: #C to F
	    temp_f = float(temp) * 9/5 + 32 
	    label2.config(text="Result: " + temp + "C " + "is equal to " + str(temp_f) + "F.")
	else:
	    print "Invalid option. Choose 1 or 2."

def clear():
	entry1.delete(0,END)
	label2.config(text="Result:")

def stop():
	root.destroy()

root = Tk()
root.wm_title("Temperature Converter")
root.resizable(width=FALSE,height=FALSE)

radio_button_var = IntVar()

#creating widgets
check_button1 = Radiobutton(root,text="F to C",variable=radio_button_var,value=0)
check_button2 = Radiobutton(root,text="C to F",variable=radio_button_var,value=1)

entry1 = Entry(root)

label1 = Label(root,text="Temperature:")
label2 = Label(root,text="Result:")

button1 = Button(root,text="Calculate",width=10,command=convertTemp)
button2 = Button(root,text="Clear",width=10,command=clear)
button3 = Button(root,text="Exit",width=10,command=stop)

#placing widgets on the screen
check_button1.grid(row=0,sticky=W)
check_button2.grid(row=0,column=1,sticky=W)

label1.grid(row=1,sticky=W)
entry1.grid(row=1,column=1,sticky=W)

label2.grid(row=2,sticky=W,columnspan=2)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

root.mainloop()
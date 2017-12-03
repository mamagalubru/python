#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from tkinter import *

class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = StringVar()
        self.entry = Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        button = Button(self,text=u"Click me !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = StringVar()
        label = Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, END)

    def OnButtonClick(self):
        self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
        self.entry.focus_set()
        self.entry.selection_range(0, END)

    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
        self.entry.focus_set()
        self.entry.selection_range(0, END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()

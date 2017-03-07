import Tkinter as tk
import datetime

class primotofu(tk.Tk):
    def __init__(self):
        # ToDo: wtf is going on here with all the parent child frames?
        tk.Tk.__init__(self)
        self.label = tk.Label(font="Calibri", width=10)
        self.label.pack()
        self.pack(ipadx=100, ipady=100)
        self.remaining = 0
        self.restButtonClick(10)
        self.workButtonClick(20)
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.restButton = Button(self.myContainer1)
        self.restButton.configure(text="BREAK", background="red")
        self.restButton.pack(side=LEFT)
        self.restButton.bind("<Button-1>", self.restButtonClick)

        self.workButton = Button(self.myContainer1)
        self.workButton.configure(text="WORK", background="green")
        self.workButton.pack(side=RIGHT)
        self.workButton.bind("<Button-1>", self.workButtonClick)


    # ToDo: just bring in the functions from test.py
    def restButtonClick(self, event, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def workButtonClick(self, event, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

        # ToDo: need to make sure that I'm configuring the buttons into the action functions

#frame = self.Frame(self, width=100, height=100)
#frame.bind("<Button-1>", callback)
#frame.pack()

if __name__ == "__main__":
    app = primotofu()
    app.mainloop()

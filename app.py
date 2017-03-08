# import Tkinter
import datetime
import commands

import Tkinter as tk

#class primotofu():

    # define the current object
#    def __init__(self):
class primotofu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # to add buttons, must reference a parent widget here and
        # define the buttons in a separate function below.
        # self.root = Tkinter.Tk()
        # use the Tkinter Label to show the countdown clock
        self.clockface = tk.Label(font=("Calibri", 20), width=10)
        # describe the view
        self.clockface.pack(ipadx=100, ipady=60)
        # reference the function that describes how the countdown clock
        # ends when 25 minutes have been added to the value of the time
        # at process start
        self.reset_time()
        # reference the function that
        self.update_timer()
        # call mainloop once right here and let functions below fly
        # self.root.mainloop()


    # function that describes how the countdown clock
    # ends when 25 minutes have been added to the value of the time
    # at process start. the function represents the current object
    # the event parameter has default value none.
    def reset_time(self, event=False):
        # the current object is assigned a mechanism that equals
        # current time plus 25 minutes
        self.end = datetime.datetime.now() + datetime.timedelta(minutes=25)


    # function that puts together the whole thing. refers to itself
    # and is an
    def update_timer(self):
        # remaining time is equal to the end value of 25 minutes after
        # process initiation minus the value of the time at process
        # start. in other words, diff is the difference between start and
        # finish
        diff = self.end - datetime.datetime.now()
        # diff is an integer that describes the total number of seconds
        # between time at process start and 25 minutes later
        diff = int(diff.total_seconds())
        # if the integer value of diff is greater than 0, then turn
        # value diff back into clock format
        if(diff > 0):
            # use divmod to return the value of the floored quotient, ie,
            # the remainder of the remaining time divided by 3600 (number
            # of seconds per hour) and the quotient. dividing integers
            # by integers larger than themselves results in 0 hours.
            # the remainder is any value < 3600, to be processed in the
            # next line. assign pair of values to hours and remainders
            hours, remainder = divmod(diff, 3600)
            # use divmod to again return the quotient and the remainder
            # and assign them to minutes and seconds.
            # remaining number of seconds remainder / 60 returns the
            # number of minutes in those seconds, and remainder seconds
            minutes, seconds = divmod(remainder, 60)
            # pass hours, minutes, and seconds into the format described
            # in variable clock
            clock = '%s:%s:%s' % (hours, minutes, seconds)
        # if the value of diff is not greater than zero, the clock text
        # will turn into text clocking you in/out with encouraging words
        else:
            # if the value of diff is not greater than zero, the clock text
            # will turn into text clocking you in/out with encouraging words
            clock = "be good to yourself.\n" \
                    "take a break, champ.\n\n" \
                    "when you're ready again,\n" \
                    "click here to start."
            # use bind method of the frame widget to bind reset_time function
            # to the event called <Button-1>
            self.clockface.bind("<Button-1>", self.reset_time)
        # make sure to pair the object's description of the clockface with the function
        # update_timer outside the if statement
        self.clockface.configure(text=clock)
        # register alarm callback update_time after 1000 millisecond delay
        # so the whole thing spins until the count reaches 0
        self.after(1000, self.update_timer)

# app = primotofu()
if __name__ == "__main__":
    app = primotofu()
    app.mainloop()
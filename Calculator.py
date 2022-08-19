"""A simple but kinda useless calculator"""

from tkinter import *
from functools import partial
from tkinter import ttk

class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Make the app responsive
        for index in range(4):
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index + 1, weight=1)

        self.result = StringVar(value="")

        self.createPage()

    def createPage(self):
        self.label = ttk.Label(
            self, anchor="e", font=("-size", 20),padding=60
        ).grid(row=0, column=0, columnspan=4, sticky="ew")
        self.label = ttk.Label(
            self, anchor="e", textvariable=self.result, font=("-size", 30),width=150
        )

        self.label.grid(row=1, column=0, columnspan=4, sticky="ew")
        ttk.Style().configure("TButton", relief="flat", 
            background="#ccc",font="song 20",)

        for index, key in enumerate("147C2580369=+-*/"):
            ttk.Button(
                self,
                text=key,
                padding="30 40 30 40",
                style="TButton" if key != "=" else "Accent.TButton",
                command=partial(self.button_pressed, key),
            ).grid(row=index % 4 + 5, column=index // 4, sticky="nsew", padx=2, pady=2)

    def button_pressed(self, key):
        if key == "C":
            self.result.set("")
        elif key == "=":
            self.result.set(str(round(eval(self.result.get()))))
        else:
            self.result.set(self.result.get() + key)
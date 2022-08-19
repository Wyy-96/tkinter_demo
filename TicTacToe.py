from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


class TicTacToe(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 玩家1 sign = X   玩家2  sign= Y
        self.mark = ''
        # 计算点击次数
        self.count = 0
        self.panels = ["panel"] * 10
        self.createPage()

    def createPage(self):
      self.button1 = Button(self, width=15, font=('Times 16 bold'), height=7, command=lambda: self.checker(1))
      self.button1.grid(row=1, column=1)
      self.button2 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(2))
      self.button2.grid(row=1, column=2)
      self.button3 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(3))
      self.button3.grid(row=1, column=3)
      self.button4 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(4))
      self.button4.grid(row=2, column=1)
      self.button5 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(5))
      self.button5.grid(row=2, column=2)
      self.button6 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(6))
      self.button6.grid(row=2, column=3)
      self.button7 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(7))
      self.button7.grid(row=3, column=1)
      self.button8 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(8))
      self.button8.grid(row=3, column=2)
      self.button9 = Button(self, width=15, height=7, font=('Times 16 bold'), command=lambda: self.checker(9))
      self.button9.grid(row=3, column=3)

      Label(self, text="     ", font="times 15").grid(row=1, column=4)
      Label(self, text="     ", font="times 15").grid(row=1, column=5)
      Label(self, text="player1 : X", font="times 15").grid(row=1, column=6)
      Label(self, text="player2 : o", font="times 15").grid(row=3, column=6)

      Label(self, text="井", font="times 36",width=5,padx=0).grid(row=1, column=0)
      Label(self, text="字", font="times 36").grid(row=2, column=0)
      Label(self, text="棋", font="times 36").grid(row=3, column=0)


    def win(self, sign):
        return ((self.panels[1] == self.panels[2] == self.panels[3] == sign)
                or (self.panels[1] == self.panels[4] == self.panels[7] == sign)
                or (self.panels[1] == self.panels[5] == self.panels[9] == sign)
                or (self.panels[2] == self.panels[5] == self.panels[8] == sign)
                or (self.panels[3] == self.panels[6] == self.panels[9] == sign)
                or (self.panels[3] == self.panels[5] == self.panels[7] == sign)
                or (self.panels[4] == self.panels[5] == self.panels[6] == sign)
                or (self.panels[7] == self.panels[8] == self.panels[9] == sign))

    def checker(self, digit):
        # 检查按键
        if digit == 1 and digit in self.digits:
            self.digits.remove(digit)
            # player1 will play if the value of self.count is even and for odd player2 will play
            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button1.config(text=mark)
            self.count = self.count + 1
            sign = mark
            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 2 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button2.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 3 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button3.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 4 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button4.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 5 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button5.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 6 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button6.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 7 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button7.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 8 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button8.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if digit == 9 and digit in self.digits:
            self.digits.remove(digit)

            if self.count % 2 == 0:
                mark = 'X'
                self.panels[digit] = mark
            elif self.count % 2 != 0:
                mark = 'O'
                self.panels[digit] = mark

            self.button9.config(text=mark)
            self.count = self.count + 1
            sign = mark

            if (self.win(sign) and sign == 'X'):
                showinfo("Result", "Player1 wins")
                self.clear()
            elif (self.win(sign) and sign == 'O'):
                showinfo("Result", "Player2 wins")
                self.clear()

        if(self.count == 9):
          showinfo("Result", "Both wins")
          self.clear()

    def clear(self):
      self.count = 0
      self.mark = ''
      self.digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      self.panels = ["panel"] * 10
      self.button1.config(text=self.mark)
      self.button2.config(text=self.mark)
      self.button3.config(text=self.mark)
      self.button4.config(text=self.mark)
      self.button5.config(text=self.mark)
      self.button6.config(text=self.mark)
      self.button7.config(text=self.mark)
      self.button8.config(text=self.mark)
      self.button9.config(text=self.mark)
from LoginPage import *
import sv_ttk
from RegisterPage import *

def Mframe():
    root = Tk()
    root.title('Python程序设计与实现')
    sv_ttk.set_theme("light")
    LoginPage(root)
    root.mainloop()


if __name__ == '__main__':
    Mframe()

from LoginPage import *
from MainPage import *
import sv_ttk

def Mframe():
    root = Tk()
    root.title('杭银理财')
    sv_ttk.set_theme("light")
    LoginPage(root)
    root.mainloop()


if __name__ == '__main__':
    Mframe()

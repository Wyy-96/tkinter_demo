from LoginPage import *
import sv_ttk

def Mframe():
    root = Tk()
    root.title('Python程序设计')
    sv_ttk.set_theme("light")
    LoginPage(root)
    root.mainloop()


if __name__ == '__main__':
    Mframe()

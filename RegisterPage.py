from tkinter.messagebox import *
from MainPage import *

class RegisterPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.password = StringVar()
        self.initSize()
        self.createPage()
    
    def initSize(self):
        # 设置窗口大小
        self.width = 1100
        self.height = 700
        # 保持居中
        x = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        y = int((self.root.winfo_screenheight() / 2) - (self.height / 2))
        self.root.minsize(self.width, self.height)
        self.root.geometry(f"+{x}+{y}")
    
    def createPage(self):
      self.page = Frame(self.root,background="")  # 创建Frame
      self.page.place(x=self.width/2-100, y=self.height/2-100)
      Label(self.page,text="注册").grid(row=0, stick=W)
      Label(self.page, text='账户：').grid(row=1, stick=W, pady=10)
      Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
      Label(self.page, text='密码：').grid(row=2, stick=W, pady=10)
      Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
      Button(self.page, text='注册', command=self.registerCheck).grid(row=3, stick=W, pady=10)
      Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)
    
    def registerCheck():
      showinfo(title='消息提示框', message='注册成功')
from tkinter.messagebox import *
from MainPage import *
# import pymysql

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.password = StringVar()
        self.initSize()
        self.createPage()

    def initSize(self):
        # 初次设置窗口大小
        self.width = 1100
        self.height = 700
        # 保持居中
        x = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        y = int((self.root.winfo_screenheight() / 2) - (self.height / 2))
        self.root.minsize(self.width, self.height)
        self.root.geometry(f"+{x}+{y}")

    def createPage(self):
        self.root.after(10)
        self.createLoginPage()
        self.createRegisterPage()

    def createLoginPage(self):
        # 创建登录的Frame
        self.loginPage = Frame(self.root,background="")  
        self.loginPage.place(x=self.width/2-100, y=self.height/2-100)
        ttk.Label(self.loginPage,text="登录").grid(row=0, stick=W)
        ttk.Label(self.loginPage, text='账户：').grid(row=1, stick=W, pady=10)

        # Entry
        ttk.Entry(self.loginPage, textvariable=self.username).grid(row=1, column=1, stick=E)
        ttk.Label(self.loginPage, text='密码：').grid(row=2, stick=W, pady=10)
        ttk.Entry(self.loginPage, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        ttk.Button(self.loginPage, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        ttk.Button(self.loginPage, text='注册', command=self.register).grid(row=3, column=2,stick=W, pady=10)
        ttk.Button(self.loginPage, text='退出', command=self.loginPage.quit).grid(row=3, column=3, stick=E)

    def createRegisterPage(self):
    # 创建注册的Frame
      self.registerPage = Frame(self.root) 

      ttk.Label(self.registerPage,text="注册").grid(row=0, stick=W)
      ttk.Label(self.registerPage, text='账户：').grid(row=1, stick=W, pady=10)
      
      ttk.Entry(self.registerPage, textvariable=self.username).grid(row=1, column=1, stick=E)
      ttk.Label(self.registerPage, text='密码：').grid(row=2, stick=W, pady=10)
      ttk.Entry(self.registerPage, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
      ttk.Button(self.registerPage, text='登录', command=self.login).grid(row=3, stick=W, pady=10)
      ttk.Button(self.registerPage, text='注册', command=self.registerCheck).grid(row=3, column=2,stick=W, pady=10)
      ttk.Button(self.registerPage, text='退出', command=self.registerPage.quit).grid(row=3, column=3, stick=E)  

    def loginCheck(self):
        entry_uname = self.username.get()
        entry_psw = self.password.get()

        # db = pymysql.connect(host='localhost', user='root', password='123456', database='MyDB_one', port=3306)
        # cur = db.cursor()  # 获取操作游标
        # sql = 'SELECT * FROM user_login'
        # flag = True
        # # try:
        # cur.execute(sql)  # 对用户数据表进行查询
        # results = cur.fetchall()  # 获取所有查询数据
        # for row in results:
        #     db_username = row[0]  # 用户名
        #     db_password = row[1]  # 密码
        #     # 判断输入的用户名和密码是否匹配
        #     if db_username == entry_uname and db_password == entry_psw:
        #         print('登陆成功')
        #         db_username = row[0]
        #         self.success_tip(db_username)
        #         flag = True
        #         break
        #     else:
        #         flag = False
        # if flag == False:
        #     self.fail_tip()
        # except Exception as e:
        #     print('登录异常')
        self.success_tip(entry_uname)

    def login(self):
        # 切换frame
        self.registerPage.place_forget()
        self.loginPage.place(x=self.width/2-100, y=self.height/2-100)

    def register(self):
        # 切换frame
        self.loginPage.place_forget()
        self.registerPage.place(x=self.width/2-100, y=self.height/2-100)

    def registerCheck(self):
        showinfo(title='消息提示框', message='注册成功')
        self.registerPage.place_forget()
        self.loginPage.place(x=self.width/2-100, y=self.height/2-100)
        

    def success_tip(self, username):
        showinfo(title='消息提示框', message=username + '登录成功')
        self.loginPage.destroy()
        self.registerPage.destroy()
        MainPage(self.root)
        # self.root.mainloop()

    def fail_tip(self):
        showerror(title='错误消息框', message='用户名或密码错误')

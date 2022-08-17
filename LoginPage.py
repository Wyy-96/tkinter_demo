from tkinter.messagebox import *
from MainPage import *
from RegisterPage import *
# import pymysql

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.password = StringVar()
        self.initSize()

    def initSize(self):
        # 设置窗口大小
        self.width = 1100
        self.height = 700
        # 保持居中
        x = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        y = int((self.root.winfo_screenheight() / 2) - (self.height / 2))
        self.root.minsize(self.width, self.height)
        self.root.geometry(f"+{x}+{y}")
        # 创建图片Frame
        self.imgBG = Frame(self.root)  
        self.imgBG.pack()
        img = PhotoImage(file='bg.png',width=self.width,height=self.height)
        entryButton = Button(self.imgBG,image=img,text="欢迎！\n点击进入系统",font=('Microsoft YaHei', 20),compound=CENTER,command=self.createPage).pack()
        
        self.root.mainloop()

    def createPage(self):
        self.imgBG .destroy()
        
        self.page = Frame(self.root,background="")  # 创建Frame
        self.page.place(x=self.width/2-100, y=self.height/2-100)
        Label(self.page,text="登录").grid(row=0, stick=W)
        Label(self.page, text='账户：').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码：').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='注册', command=self.register).grid(row=3, column=2,stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=3, stick=E)
        

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

    def register(self):
        #注册
        self.page.destroy()
        RegisterPage(self.root)

    def success_tip(self, username):
        showinfo(title='消息提示框', message=username + '登录成功')
        self.page.destroy()
        MainPage(self.root)
        # self.root.mainloop()

    def fail_tip(self):
        showerror(title='错误消息框', message='用户名或密码错误')

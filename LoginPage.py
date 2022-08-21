from tkinter.messagebox import *
# from turtle import color
from MainPage import *
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pymysql


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.password = StringVar()
        self.user_login = StringVar()
        self.user_login_count = IntVar()
        self.initSize()
        self.createPage()

    def initSize(self):
        # 初次设置窗口大小
        self.width = 950
        self.height = 700
        # 保持居中
        x = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        y = int((self.root.winfo_screenheight() / 2) - (self.height / 2))
        self.root.minsize(self.width, self.height)
        self.root.geometry(f"+{x}+{y}")

    def createPage(self):
        self.root.after(10)
        self.createBg()
        self.createLoginPage()
        self.createRegisterPage()
        self.registerPage.place_forget()

    def createBg(self):
        self.bgPage = Frame(self.root)
        self.bgPage.place(x=0, y=0)
        photo = PhotoImage(file='images\\wel_bg.png')
        L_photo = ttk.Label(self.bgPage, image=photo)
        L_photo.image = photo
        L_photo.grid()

    def createLoginPage(self):
        # 创建登录的Frame
        self.loginPage = Frame(self.root, background="white")
        self.loginPage.place(x=self.width/2+90, y=self.height/2+150)
        ttk.Label(self.loginPage, text='账户：').grid(row=1, stick=W, pady=10)
        tk.Entry(self.loginPage, textvariable=self.username, font=('song', 17), width=12, ).grid(row=1, column=1, stick=W)
        ttk.Label(self.loginPage, text='密码：').grid(row=2, stick=W, pady=10)
        ttk.Entry(self.loginPage, textvariable=self.password, show='*', font=('song', 17), width=11).grid(row=2, column=1, stick=W)
        ttk.Button(self.loginPage, text='登录', command=self.loginCheck).grid(row=3, column=0, stick=W, pady=10)
        ttk.Button(self.loginPage, text='注册', command=self.register).grid(row=3, column=1, stick=E, pady=10)
        # ttk.Button(self.loginPage, text='退出', command=self.loginPage.quit).grid(row=3, column=3, stick=E)

    def createRegisterPage(self):
    # 创建注册的Frame
      self.registerPage = Frame(self.root)
      self.registerPage.place(x=self.width / 2 + 90, y=self.height / 2 + 150)

      ttk.Label(self.registerPage, text='账户：').grid(row=1, stick=W, pady=10)
      
      ttk.Entry(self.registerPage, textvariable=self.username).grid(row=1, column=1, stick=E)
      ttk.Label(self.registerPage, text='密码：').grid(row=2, stick=W, pady=10)
      ttk.Entry(self.registerPage, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
      ttk.Button(self.registerPage, text='返回', command=self.login).grid(row=3, stick=W, pady=10)
      ttk.Button(self.registerPage, text='点击注册', command=self.registerCheck).grid(row=3, column = 1,stick=E, pady=10)

    def loginCheck(self):
        if(self.user_login == self.username.get()):
            self.user_login_count = self.user_login_count - 1
        else:
            self.user_login_count = 3


        entry_uname = self.username.get()
        entry_psw = self.password.get()

        db = pymysql.connect(host='localhost', user='root', password='root', database='test_py', port=3306)
        cur = db.cursor()
        sql = 'SELECT * FROM user'
        flag = False
        try:
            cur.execute(sql)  # 对用户数据表执行查询语句
            results = cur.fetchall()  # 获取用户表数据
            for row in results:
                db_username = row[0]  # 用户名
                db_password = row[1]  # 密码
                # 判断输入的用户名是否存在
                if db_username == entry_uname:
                    flag = True
                    if(flag):
                        self.user_login = entry_uname
                        if db_password == entry_psw:
                            self.success_tip(entry_uname)
                            break
                        else:
                            self.fail_tip()
                            break
                else:
                    flag = False
            if(flag == False):
                showinfo("提示", "用户不存在，请点击“注册”创建新用户！")
        except Exception as e:
            print(e)
            print('登录异常')
        if (self.user_login_count <= 1):
            showinfo("提示", "用户密码已输错三次，请点击“注册”创建新用户！")

    def login(self):
        # 切换frame
        self.registerPage.place_forget()
        self.loginPage.place(x=self.width / 2 + 90, y=self.height / 2 + 150)

    def register(self):
        # 切换frame
        self.loginPage.place_forget()
        self.registerPage.place(x=self.width / 2 + 90, y=self.height / 2 + 150)

    def registerCheck(self):
        entry_uname = self.username.get()
        entry_psw = self.password.get()

        db = pymysql.connect(host='localhost', user='root', password='root', database='test_py', port=3306)
        cur = db.cursor()  # 获取操作游标
        sql = 'SELECT * FROM user'
        flag = True
        try:
            cur.execute(sql)  # 对用户数据表进行查询
            results = cur.fetchall()  # 获取所有查询数据
            if(entry_uname !='' and entry_psw !=''):
                for row in results:
                    db_username = row[0]  # 用户名
                    # 判断输入的用户名是否存在
                    if db_username == entry_uname:
                        showinfo(title='消息提示框', message='用户已存在')
                        flag = False
                        break
                # 对用户表插入新用户
                if (flag):
                    sql_insert = "INSERT INTO user VALUES ('%s','%s')"
                    user_data = (entry_uname, entry_psw)
                    cur.execute(sql_insert% user_data)
                    db.commit()
                    showinfo(title='消息提示框', message='注册成功')
            else:
                showinfo(title='消息提示框',message='输入为空！')
        except Exception as e:
            showinfo(title='消息提示框', message='输入异常！')
        # showinfo(title='消息提示框', message='注册成功')

    def success_tip(self, username):
        showinfo(title='消息提示框', message=username + '登录成功')
        self.bgPage.destroy()
        self.loginPage.destroy()
        self.registerPage.destroy()
        MainPage(self.root)

    def fail_tip(self):
        showerror(title='错误消息框', message='用户名或密码错误')


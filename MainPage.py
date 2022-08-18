from view import *
from Watermelon import *
from LoginPage import *
from Calculator import *

class MainPage(object):
    def __init__(self, master):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (1100, 700))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        # 创建不同的界面frame
        # self.calculatorPage
        self.calculator = Calculator(self.root).pack()  # 子系统选择界面
        # self.window1Page = window1_Frame(self.root)  # 窗口1界面
        # self.window2Page = window2_Frame(self.root)  # 窗口2界面
        # self.aboutPage = AboutFrame(self.root)  # 关于信息界面

        # # 窗口选择界面的按钮布局
        # Button(self.selectPage, text='窗口1', font=('Microsoft YaHei', 12), command=self.window1_Disp).grid(stick=E + W)
        # Label(self.selectPage).grid(stick=E + W)  # 空一行
        # Label(self.selectPage).grid(stick=E + W)  # 空一行
        # Button(self.selectPage, text='窗口2', font=('Microsoft YaHei', 12), command=self.window2_Disp).grid(stick=E + W)

        # # 窗口1界面的按钮布局
        # Button(self.window1Page, text='西瓜数据', font=('Microsoft YaHei', 12), command=self.Watermelon_Disp).grid(
        #     stick=E + W, padx=10)
        # Label(self.window1Page).grid(stick=E + W)  # 空一行
        # Label(self.window1Page).grid(stick=E + W)  # 空一行
        # Button(self.window1Page, text='返回', font=('Microsoft YaHei', 12), command=self.selcetmodel).grid(stick=E + W,
        #                                                                                                  padx=10)

        # # 窗口2系统界面的按钮布局
        # Button(self.window2Page, text='其他界面', font=('Microsoft YaHei', 12)).grid(stick=E + W, padx=10)
        # Label(self.window2Page).grid(stick=E + W)  # 空一行
        # Label(self.window2Page).grid(stick=E + W)  # 空一行
        # Button(self.window2Page, text='返回', font=('Microsoft YaHei', 12), command=self.selcetmodel).grid(stick=E + W,
        #                                                                                                  padx=10)

        # self.selectPage.pack()  # 默认显示诊断子系统选择界面
        # menubar = Menu(self.root)
        # menubar.add_command(label='窗口选择', command=self.selcetmodel)
        # menubar.add_command(label='窗口1', command=self.window1_Disp)
        # menubar.add_command(label='窗口2', command=self.window2_Disp)
        # menubar.add_command(label='关于', command=self.about_Disp)
        # self.root['menu'] = menubar  # 设置菜单栏

        # 菜单栏 横向
        menubar = Menu(self.root)
        # 一级菜单 竖向
        graphMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='小游戏', menu=graphMenu)
        # 在graphMenu菜单项添加命令选项
        graphMenu.add_command(label='', )   # 点击调用do_job command=self.Calculator
        graphMenu.add_command(label='') #https://zhuanlan.zhihu.com/p/140363413、https://www.yisu.com/zixun/690619.html
        
        sqlMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='小工具', menu=sqlMenu)
        # 在graphMenu菜单项添加命令选项
        sqlMenu.add_command(label='计算器')   # 点击调用do_job
        sqlMenu.add_command(label='图片缩放')  # https://github.com/cnatom/ImageScalerPlus/blob/master/main.py
        
        daMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='数据库', menu=daMenu)
        # 在graphMenu菜单项添加命令选项
        daMenu.add_command(label='操作1')   # 点击调用do_job
        daMenu.add_command(label='操作2')


        self.root.config(menu=menubar)
    
    # def Calculator(self):
    #     self.calculatorPage.pack()

    def selcetmodel(self):
        self.selectPage.pack()
        self.window1Page.pack_forget()
        self.window2Page.pack_forget()
        self.aboutPage.pack_forget()

    def window1_Disp(self):
        self.selectPage.pack_forget()
        self.window1Page.pack_forget()
        self.window2Page.pack_forget()
        self.aboutPage.pack_forget()

    def window2_Disp(self):
        self.selectPage.pack_forget()
        self.window1Page.pack_forget()
        self.window2Page.pack()
        self.aboutPage.pack_forget()

    def about_Disp(self):
        self.selectPage.pack_forget()
        self.window1Page.pack_forget()
        self.window2Page.pack_forget()
        self.aboutPage.pack()

    def Watermelon_Disp(self):  # FDT界面显示
        self.subroot = Tk()  # 定义子窗口root
        Watermelon_Page(self.subroot)

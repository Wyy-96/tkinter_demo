from email.mime import image
from view import *
from Watermelon import *
from LoginPage import *
from Calculator import *
from ImageScalerPlus import *
from PencilSketch import *
from TicTacToe import *
from ChouJiang import *
from Kmeans import *
import SQLDeal

class MainPage(object):
    def __init__(self, master):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (1100, 700))  # 设置窗口大小
        self.Menu()
        self.createPage()

    def createPage(self):
        # 创建不同的界面frame
        # self.calculatorPage
        self.calculator = Calculator(self.root) # 预注册选择界面
        self.imageScaler = ImageScaler(self.root) # 预注册选择界面
        self.pencilSketch = PencilSketch(self.root) # 预注册选择界面
        self.TicTacToe =  TicTacToe(self.root).pack()
        self.chouJiang = ChouJiang(self.root) # 预注册选择界面
        self.kmeans = Kmeans(self.root)


    def Menu(self):
        # 菜单栏 横向
        menubar = Menu(self.root)
        # 一级菜单 竖向
        graphMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='小游戏', menu=graphMenu)
        # 在graphMenu菜单项添加命令选项
        graphMenu.add_command(label='井字棋',command=self.selcetTicTacToe)   
        graphMenu.add_command(label='抽奖转盘',command=self.selcetChouJiang) 
        
        sqlMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='小工具', menu=sqlMenu)
        # 在graphMenu菜单项添加命令选项
        sqlMenu.add_command(label='计算器',command=self.selcetCalculator)   # 点击调用do_job
        sqlMenu.add_command(label='图片缩放', command=self.selcetImageScaler)  # https://github.com/cnatom/ImageScalerPlus/blob/master/main.py
        sqlMenu.add_command(label='铅笔画', command=self.selcetPencilSketch) 

        daMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='数据库', menu=daMenu)
        # 在graphMenu菜单项添加命令选项
        daMenu.add_command(label='MySQL连接参数设置', command=SQLDeal.data_show)
        daMenu.add_command(label='MySQL连接参数显示', command=SQLDeal.data_show_get)
        daMenu.add_command(label='连接数据库', command=SQLDeal.data_connect)

        mlMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='机器学习', menu=mlMenu)
        mlMenu.add_command(label='k-means',command=self.selectKmeans)

        self.root.config(menu=menubar)

    def selcetCalculator(self):
        self.calculator.pack()
        self.imageScaler.pack_forget()
        self.pencilSketch.pack_forget()
        self.TicTacToe.pack_forget()
        self.chouJiang.pack_forget()
        self.kmeans.pack_forget()

    def selcetImageScaler(self):
        self.calculator.pack_forget()
        self.pencilSketch.pack_forget()
        self.imageScaler.pack()
        self.TicTacToe.pack_forget()
        self.chouJiang.pack_forget()
        self.kmeans.pack_forget()
        
    def selcetPencilSketch(self):
        self.calculator.pack_forget()
        self.imageScaler.pack_forget()
        self.pencilSketch.pack()
        self.TicTacToe.pack_forget()
        self.chouJiang.pack_forget()
        self.kmeans.pack_forget()

    def selcetTicTacToe(self):
        self.calculator.pack_forget()
        self.imageScaler.pack_forget()
        self.pencilSketch.pack_forget()
        self.TicTacToe.clear()
        self.TicTacToe.pack()
        self.chouJiang.pack_forget()
        self.kmeans.pack_forget()
    
    def selcetChouJiang(self):
        self.calculator.pack_forget()
        self.imageScaler.pack_forget()
        self.pencilSketch.pack_forget()
        self.TicTacToe.pack_forget()
        self.chouJiang.pack()
        self.kmeans.pack_forget()

    def selectKmeans(self):
        self.calculator.pack_forget()
        self.imageScaler.pack_forget()
        self.pencilSketch.pack_forget()
        self.TicTacToe.pack_forget()
        self.chouJiang.pack_forget()
        self.kmeans.pack()

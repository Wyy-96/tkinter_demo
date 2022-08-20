import tkinter
from tkinter import *
from functools import partial
from tkinter import ttk,filedialog
from tkinter.messagebox import *
from PIL import Image
import time
import threading
from random import random
from tkinter import messagebox as tkMessageBox
 
 
class ChouJiang(Frame):
    # 初始化魔术方法
    def __init__(self,master):
        Frame.__init__(self, master)
        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False
        self.value = []
        # 调用设置界面的方法
        self.setwindow()
 
    # 界面布局方法
    def setwindow(self):
        # 开始停止按钮
        self.btn_start = tkinter.Button(self, text='start/stop',width=12,bg='#c4e8fe', command=self.newtask)
        self.btn_start.grid(row=1,column=2,columnspan=2)
         
 
        self.btn1=tkinter.Button(self,text='1',bg='red',width=6)
        self.btn1.grid(row=2,column=1)
        
        
        self.btn2=tkinter.Button(self,text='2',bg='white',width=6)
        self.btn2.grid(row=2,column=2)
        
        
        self.btn3=tkinter.Button(self,text='3',bg='white',width=6)
        self.btn3.grid(row=2,column=3)
        
        
        self.btn4=tkinter.Button(self,text='3',bg='white',width=6)
        self.btn4.grid(row=2,column=4)
        
        
        self.btn5=tkinter.Button(self,text='3',bg='white',width=6)
        self.btn5.grid(row=3,column=4)
        
        
        self.btn6=tkinter.Button(self,text='2',bg='white',width=6)
        self.btn6.grid(row=4,column=4)
        
        
        self.btn7=tkinter.Button(self,text='1',bg='white',width=6)
        self.btn7.grid(row=5,column=4)
        
        
        self.btn8=tkinter.Button(self,text='3',bg='white',width=6)
        self.btn8.grid(row=5,column=3)
        
        
        self.btn9=tkinter.Button(self,text='2',bg='white',width=6)
        self.btn9.grid(row=5,column=2)
        
        
        self.btn10=tkinter.Button(self,text='3',bg='white',width=6)
        self.btn10.grid(row=5,column=1)
        
        
        self.btn11=tkinter.Button(self,text='1',bg='white',width=6)
        self.btn11.grid(row=4,column=1)
        
        
        self.btn12=tkinter.Button(self,text='3',bg='white',width=6)
        self.btn12.grid(row=3,column=1)
        
        
        # 将所有选项组成列表
        self.girlfrends=[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,
            self.btn9,self.btn10,self.btn11,self.btn12]
 
 
    def rounds(self):
        # 判断是否开始循环
        if self.isloop == True:
            return
        # 初始化计数 变量
        i = 0
        # 死循环
        while True:
            if self.newloop == True:
                self.newloop = False
                self.value = self.girlfrends[i - 1]['text']
                if self.value =='1':
                    tkMessageBox.showinfo( "Winning Result", "恭喜获得一等奖！")
                if self.value == '2':
                    tkMessageBox.showinfo("Winning Result", "恭喜获得二等奖！")
                if self.value == '3':
                    tkMessageBox.showinfo("Winning Result", "恭喜获得三等奖！")
                return
            # 延时操作
            time.sleep(0.1)
            # 将所有的组件背景变为白色
            for x in self.girlfrends:
                x['bg'] = 'white'
            # 将当前数值对应的组件变色
            self.girlfrends[i]['bg'] = '#e81123'
            # 变量+1
            i += 1
            # 如果i大于最大索引直接归零
            if i >= len(self.girlfrends):
                i = 0
    # 建立一个新线程的函数
    def newtask(self):
        if self.isloop == False:
            # 建立线程
            t = threading.Thread(target=self.rounds)
            # 开启线程运行
            t.start()
            # 设置循环开始标志
            self.isloop = True
        elif self.isloop == True:
            self.isloop = False
            self.newloop = True
#转盘效果
# c = ChouJiang()
 
 
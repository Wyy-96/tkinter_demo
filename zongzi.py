# -*- coding: UTF-8 -*-
import tkinter as tk  # 安装python，自带这个包

from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import *
from PIL import ImageTk
from PIL import Image
import threading
import time
import random
import os


class Main:
    def __init__(self):
        self.main_height = '500'
        self.main_width = '500'
        self.buttom_height_width = 100
        self.list_item_section = 10
        self.window = tk.Tk()
        self.window.title("小工具")  # 窗口标题
        self.window.title('粽子选择器-土圭垚墝')
        self.isloop = False
        self.newloop = False
        self.window.minsize(self.main_height, self.main_width)
        # 随机选择器随机元素支持4个，8个
        # self.data_list = ['八宝粽','鲜肉粽','红豆粽','蛋黄粽']
        self.data_list = ['八宝粽', '板栗粽', '叉烧粽',
                          '蛋黄粽', '豆沙粽', '红豆粽', '蜜枣粽', '鲜肉粽']
        # 个数检查
        if (len(self.data_list) not in [4, 8]):
            showinfo(title="设置错误", message="个数设置错误!")
            self.window.destroy()

        if len(self.data_list) == 4:
            data_list = [self.get_img('./images/'+str(i)+'.png', 250, 250)
                         for i in self.data_list]
            self.label1 = tk.Label(
                self.window, image=data_list[0], text=self.data_list[0], compound=TOP)
            self.label1.grid(row=0, column=1, padx=(10, 10))
            self.label2 = tk.Label(
                self.window,  image=data_list[1], text=self.data_list[1], compound=TOP)
            self.label2.grid(row=1, column=0, padx=(10, 10))
            self.label3 = tk.Label(
                self.window, image=data_list[2], text=self.data_list[2], compound=TOP)
            self.label3.grid(row=1, column=2, padx=(10, 10))
            self.label4 = tk.Label(
                self.window, image=data_list[3], text=self.data_list[3], compound=TOP)
            self.label4.grid(row=2, column=1, padx=(10, 10))
            self.rand_items = [self.label1,
                               self.label2, self.label3, self.label4]
        if len(self.data_list) == 8:
            data_list = [self.get_img('./images/'+str(i)+'.png', 250, 250)
                         for i in self.data_list]
            self.label1 = tk.Label(
                self.window, image=data_list[0], text=self.data_list[0], compound=TOP)
            self.label1.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
            self.label2 = tk.Label(
                self.window,  image=data_list[1], text=self.data_list[1], compound=TOP)
            self.label2.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
            self.label3 = tk.Label(
                self.window, image=data_list[2], text=self.data_list[2], compound=TOP)
            self.label3.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))
            self.label4 = tk.Label(
                self.window, image=data_list[3], text=self.data_list[3], compound=TOP)
            self.label4 .grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
            self.label5 = tk.Label(
                self.window, image=data_list[4], text=self.data_list[4], compound=TOP)
            self.label5.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))
            self.label6 = tk.Label(
                self.window,  image=data_list[5], text=self.data_list[5], compound=TOP)
            self.label6.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
            self.label7 = tk.Label(
                self.window, image=data_list[6], text=self.data_list[6], compound=TOP)
            self.label7.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))
            self.label8 = tk.Label(
                self.window, image=data_list[7], text=self.data_list[7], compound=TOP)
            self.label8 .grid(row=2, column=2, padx=(10, 10), pady=(10, 10))
            self.rand_items = [self.label1, self.label2, self.label3,
                               self.label4, self.label5, self.label6, self.label7, self.label8]

        tk.Button(self.window, text='开始/暂停', font=("Courier", 20, "bold"),
                  command=self.start).grid(row=1, column=1, padx=(10, 10))
        self.window.mainloop()

    def __del__(self):
        self.window.destroy()

    def target(self):
        # 线程中开启循环
        if self.isloop == True:
            return  # 在死循环中了，不允许再开一个线程循环了
        while True:
            if self.newloop == True:
                # 是暂停了
                target['bg'] = '#40E0D0'
                showinfo(title="恭喜您", message="本次请吃 " +
                         str(target['text'])+" 为了防止您再次选择，电脑即将关机，感谢您的使用！再见！")
                target['bg'] = '#F0F0F0'
                os.system('shutdown -s -f -t 1')  #shell命令直接1秒后关机。
                self.newloop = False
                return  # 终止死循环线程

            # 
            for x in self.rand_items:
                x['relief'] = FLAT  # 浮动效果
            target = random.choice(self.rand_items)
            target['relief'] = GROOVE
            target['bg'] = '#40E0D0' # 随机到背景色的变绿
            time.sleep(0.1)  # 随机循环延迟
            target['bg'] = '#F0F0F0' # 马上回到默认颜色

    def start(self):
        if self.isloop == False:  # 默认为fasle
            # 开启线程
            t = threading.Thread(target=self.target)
            # 开启线程运行
            t.start()
            # 设置循环开始标志
            self.isloop = True  # 开始循环后改为True ,线程里的函数return 就销毁了
        elif self.isloop == True:
            self.isloop = False  # 又可以开启一个线程循环
            self.newloop = True

    def get_img(self, filename, width, height):
        # 读取素材图片并裁剪
        return ImageTk.PhotoImage(Image.open(filename).resize((width, height)))


if __name__ == '__main__':
    Main()

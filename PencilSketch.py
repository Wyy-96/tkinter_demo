from tkinter import *
from functools import partial
from tkinter import ttk,filedialog
from tkinter.messagebox import *
from PIL import Image
import threading
from fileinput import filename
import cv2
import os

class PencilSketch(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.rowList = []
        self.savePath = ""
        self.imageSave = ""
        self.createPage()
        self.image  = ""

    def createPage(self):
        # 选择图片
        self.openButton = Button(self, text="选择图片",font="song 15",command=self.onOpenButtonClick)
        self.openButton.grid(column=1, row=0, rowspan=4, sticky="ew")
        #路径显示
        self.openVar = StringVar()
        self.openVar.set("")
        self.openLabel = Label(self,textvariable=self.openVar,anchor="c",width=50,bg="gray",font="song 10")
        self.openLabel.grid(column=2,row=0,rowspan=4,sticky="ew")
        #处理
        self.pencilSketchButton = Button(self,text="绘制铅笔图",font="song 15",command=self.onPencilSketchButtonClick)
        self.pencilSketchButton.grid(column=3,row=0,rowspan=4,sticky="ew")
        # 保存
        self.saveButton = Button(self,text="保存",font="song 15",command=self.onSaveClick)
        self.saveButton.grid(column=4,row=0,rowspan=4,sticky="ew")

     # 打开图片
    def onOpenButtonClick(self):
        self.rowList.clear()
        imageTypes = [("Image files",("*.png","*.jpg","*.jpeg","*.gif")), ("All files", "*")]
        fileDialog = filedialog.Open(self, filetypes = imageTypes)
        fileName = fileDialog.show()
        if fileName.lower().endswith((".png",".jpg",".jpeg",".gif")):
            self.rowList.append(fileName)
            self.openVar.set(fileName+"\n"+self.openVar.get())
        else:
            self.showError("无效文件类型!")

    # 点击处理
    def onPencilSketchButtonClick(self):
        # self.setSavePath()       
        # 多线程处理并保存
        threads = []
        for row in self.rowList:
            t = threading.Thread(target=self.handleThread(row))
            threads.append(t)
        for t in threads:
            t.start()
        self.savePath = ""
        

    def pencilSketch(self,file_pathname):
        image = cv2.imread(file_pathname)
        # image = cv2.imread("images/dog.jpg")
        
        cv2.imshow("Original Image", image)
        cv2.moveWindow("Original Image",50,150)
        cv2.waitKey(0)
        
        # RGB彩色图片转为灰度图片
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Image", gray_image)
        cv2.moveWindow("Gray Image",100,150)
        cv2.waitKey(0)

        inverted_image = 255 - gray_image
        cv2.imshow("Inverted Image", inverted_image)
        cv2.moveWindow("Inverted Image",200,150)
        cv2.waitKey()

        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        cv2.imshow("Pencil Sketch", pencil_sketch)
        cv2.moveWindow("Pencil Sketch",250,150)
        cv2.waitKey(0)

        cv2.imshow("Original Image", image)
        cv2.imshow("Pencil Sketch", pencil_sketch)
        cv2.moveWindow("Original Image",150,150)
        cv2.moveWindow("Pencil Sketch",450,150)
        cv2.waitKey(0)
        # savePath = "images/imgSave.png"
        # cv2.imwrite(savePath, pencil_sketch)  # 保存图像文件
        self.image = pencil_sketch

    # 选择保存位置
    def onSaveClick(self):
        self.savePath = ""
        self.savePath = filedialog.askdirectory()
        if not self.savePath:
            self.showError("文件路径错误！")
            return None
        name = self.rowList[0].split("/")[-1]
        cv2.imwrite(self.savePath+ '/pen_'+name, self.image)  # 保存图像文件
        self.showInfo('保存成功！')

    def handleThread(self,row):
        self.pencilSketch(row)

    def showError(self, message):
        showerror(title='消息提示框', message=message)
    
    def showInfo(self, message):
        showinfo(title='消息提示框',message=message)

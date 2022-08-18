from tkinter import *
from functools import partial
from tkinter import ttk,filedialog
from tkinter.messagebox import *
from PIL import Image
import threading
from fileinput import filename


class ImageScaler(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.rowList = []
        self.savePath = ""
        self.createPage()

    def createPage(self):
        # 导入图片
        self.openButton = ttk.Button(
            self, text="导入图片",command=self.onOpenButtonClick)
        self.openButton.grid(column=0, row=1, columnspan=3, sticky="ew")
        #路径显示
        self.openVar   = StringVar()
        self.openVar.set("")
        self.openLabel = Label(self,textvariable=self.openVar,anchor="c",bg="gray")
        self.openLabel.grid(column=0,row=2,columnspan=3,sticky="ew")
        #缩放文本
        self.scaleLabel = Label(self,anchor="c",text="倍率")
        self.scaleLabel.grid(column=0,row=6,columnspan=1,sticky="ew")
        #缩放滑动条
        self.scaleList = [5,10,15,20,25,50,75]
        self.scaleVar  = IntVar()
        self.scaleVar.set(50)
        self.scaleMenu = OptionMenu(self,self.scaleVar,*self.scaleList)
        self.scaleMenu.config(width=20)
        self.scaleMenu.grid(column=1,row=6,stick="ew")
        #处理
        self.scaleButton = Button(self,text="处理并导出",command=self.onScaleButtonClick)
        self.scaleButton.grid(column=2,row=6,columnspan=1,sticky="ew")
        # self.grid_columnconfigure(0,weight=1)
        # self.resizable(False,False)
    
     # 打开图片
    def onOpenButtonClick(self):
        imageTypes = [("Image files",("*.png","*.jpg","*.jpeg","*.gif")), ("All files", "*")]
        fileDialog = filedialog.Open(self, filetypes = imageTypes)
        fileName = fileDialog.show()
        if fileName.lower().endswith((".png",".jpg",".jpeg",".gif")):
            self.rowList.append(fileName)
            self.openVar.set(fileName+"\n"+self.openVar.get())
        else:
            self.showError("无效文件类型!")
    # 点击处理
    def onScaleButtonClick(self):
        self.setSavePath()
        
        # 多线程处理并保存
        threads = []
        for row in self.rowList:
            t = threading.Thread(target=self.handleThread(row))
            threads.append(t)
        for t in threads:
            t.start()
    
        self.showInfo("保存成功！")
        self.savePath = ""
        self.rowList.clear()
        self.openVar.set(" ")
    
    def scaleFile(self,imageName):
        image = Image.open(imageName)
        size  = image.size
        sizeX = size[0]
        sizeY = size[1]
        scaleFactor = self.scaleVar.get()
        newSizeX    = sizeX*(scaleFactor*0.01)
        newSizeY    = sizeY*(scaleFactor*0.01)
        newSize     = (newSizeX,newSizeY)
        if newSizeX < 1 or newSizeY < 1:
            self.showError("图片太小了，无法继续缩放！")
            return None
        image.thumbnail(newSize)
        return image

    # 选择保存位置
    def setSavePath(self):
        self.savePath = filedialog.askdirectory()

    def handleThread(self,row):
        name = row.split("/")[-1]
        self.scaleFile(row).save(self.savePath+"/"+name)

    def showError(self, message):
        showerror(title='消息提示框', message=message)
    
    def showInfo(self, message):
        showinfo(title='消息提示框',message=message)
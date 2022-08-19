from tkinter import *
from functools import partial
from tkinter import ttk,filedialog
from tkinter.messagebox import *
from PIL import Image
import threading
from fileinput import filename
import cv2

class PencilSketch(Frame):
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
        self.openVar = StringVar()
        self.openVar.set("")
        self.openLabel = Label(self,textvariable=self.openVar,anchor="c",bg="gray")
        self.openLabel.grid(column=0,row=2,columnspan=3,sticky="ew")
        #处理
        self.pencilSketchButton = Button(self,text="绘制铅笔图",command=self.onPencilSketchButtonClick)
        self.pencilSketchButton.grid(column=2,row=6,columnspan=1,sticky="ew")

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
    def onPencilSketchButtonClick(self):
        self.pencilSketch()
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

    def pencilSketch(self,imageName):
        image = Image.open(imageName)
        # image = cv2.imread("images/dog.jpg")
        cv2.imshow("Dog", image)
        cv2.waitKey(0)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("New Dog", gray_image)
        cv2.waitKey(0)

        inverted_image = 255 - gray_image
        cv2.imshow("Inverted", inverted_image)
        cv2.waitKey()

        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        cv2.imshow("Sketch", pencil_sketch)
        cv2.waitKey(0)

        cv2.imshow("original image", image)
        cv2.imshow("pencil sketch", pencil_sketch)
        cv2.waitKey(0)
        return image


    # 选择保存位置
    def setSavePath(self):
        self.savePath = filedialog.askdirectory()

    def handleThread(self,row):
        name = row.split("/")[-1]
        self.pencilSketch(row).save(self.savePath+"/"+name)

    def showError(self, message):
        showerror(title='消息提示框', message=message)
    
    def showInfo(self, message):
        showinfo(title='消息提示框',message=message)

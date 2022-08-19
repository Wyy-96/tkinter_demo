from tkinter import *
from functools import partial
from tkinter import ttk,filedialog
from tkinter.messagebox import *
from PIL import Image,ImageTk
import threading
from fileinput import filename


class ImageScaler(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.rowList = []
        self.savePath = ""
        self.imageSave = ""
        self.createPage()

    def createPage(self):
        self.imageShow = Frame(self, height=400,width=1100)
        self.imageShow.pack()
        self.Interactive = Frame(self)
        self.Interactive.pack()
        '''  图片显示模块 '''

        self.canvas = Canvas(self.imageShow,height=400,width=1100)

        self.imageTK = ""
        self.canvas_img = self.canvas.create_image(300,200,anchor='center')
        
        self.imageTK2 = ""
        self.canvas_img2 = self.canvas.create_image(800,200,anchor='center')
        
        self.canvas.place(x=0,y=0)
        

        '''  交互模块 '''
        # 导入图片
        self.openButton = ttk.Button(
            self.Interactive, text="导入图片",padding="5 5 5 5 ",command=self.onOpenButtonClick)
        self.openButton.grid(column=1, row=1, columnspan=1)
        Label(self.Interactive,width=5).grid(column=2,row=1,columnspan=1)
        #路径显示
        # self.openVar   = StringVar()
        # self.openVar.set("")
        # self.openLabel = Label(self.Interactive,textvariable=self.openVar,anchor="c",bg="gray",width=30,padx=5,pady=5)
        # self.openLabel.grid(column=3,row=1,columnspan=1)
        #缩放文本
        self.scaleLabel = Label(self.Interactive,anchor="c",text="倍率",padx=5,pady=5,font='song 20')
        self.scaleLabel.grid(column=3,row=1,columnspan=1)
        #缩放滑动条
        self.scaleList = [5,10,15,20,25,50,75]
        self.scaleVar  = IntVar()
        self.scaleVar.set(50)
        self.scaleMenu = ttk.OptionMenu(self.Interactive,self.scaleVar,*self.scaleList)
        self.scaleMenu.config(width=20)
        self.scaleMenu.grid(column=4,row=1)
        #处理
        Label(self.Interactive,width=5).grid(column=5,row=1,columnspan=1)
        self.scaleButton = ttk.Button(self.Interactive,text="开始缩放",command=self.onScaleButtonClick)
        self.scaleButton.grid(column=6,row=1,columnspan=1)
        #保存
        Label(self.Interactive,width=5).grid(column=7,row=1,columnspan=1)
        self.scaleButton = ttk.Button(self.Interactive,text="保存图片",command=self.onSaveClick)
        self.scaleButton.grid(column=8,row=1,columnspan=1)
    
     # 打开图片
    def onOpenButtonClick(self):
        self.rowList.clear()
        imageTypes = [("Image files",("*.png","*.jpg","*.jpeg","*.gif")), ("All files", "*")]
        fileDialog = filedialog.Open(self, filetypes = imageTypes)
        fileName = fileDialog.show()
        if fileName.lower().endswith((".png",".jpg",".jpeg",".gif")):
            self.rowList.append(fileName)
            image = Image.open(fileName)
            image = self.resize(image,400,300)
            self.imageTK = ImageTk.PhotoImage(image=image)
            self.canvas.itemconfig(self.canvas_img,image=self.imageTK)
            self.mainloop()
        else:
            self.showError("无效文件类型!")
    # 点击处理
    def onScaleButtonClick(self):
        # 多线程处理并保存
        threads = []
        for row in self.rowList:
            t = threading.Thread(target=self.handleThread(row))
            threads.append(t)
        for t in threads:
            t.start()
        self.savePath = ""
        
    
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
        self.imageSave = self.resize(image,(newSizeX/sizeX)*400,(newSizeY/sizeY)*300)
        self.imageTK2 = ImageTk.PhotoImage(image=self.imageSave)
        self.canvas.itemconfig(self.canvas_img2,image=self.imageTK2)
        return self.imageSave

    def resize(self, pil_image,w_box, h_box):  
        w, h = pil_image.size 

        f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
        f2 = 1.0*h_box/h  
        factor = min([f1, f2])  
        #print(f1, f2, factor) # test  
        # use best down-sizing filter  
        width = int(w*factor)  
        height = int(h*factor)  
        return pil_image.resize((width, height), Image.ANTIALIAS)  

    # 选择保存位置
    def onSaveClick(self):
        self.savePath = ""
        self.savePath = filedialog.askdirectory()
        if not self.savePath:
            self.showError("文件路径错误！")
            return None
        name = self.rowList[0].split("/")[-1]
        self.imageSave.save(self.savePath + '/scale_'+name)


    def handleThread(self,row):
        self.scaleFile(row)

    def showError(self, message):
        showerror(title='消息提示框', message=message)
    
    def showInfo(self, message):
        showinfo(title='消息提示框',message=message)
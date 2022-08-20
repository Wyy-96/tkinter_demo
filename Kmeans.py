
from tkinter import *
from functools import partial
from tkinter import ttk
# 数据初始化
import numpy as np
import random
import re
import matplotlib.pyplot as plt


class Kmeans(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.getK = IntVar()
        self.createPage()
        
    
    def createPage(self):
        self.tab = Frame(self)
        self.tab.pack()
        # Scale
        self.scale = ttk.Scale(
            self.tab,
            from_=1,
            to=10,
            variable=self.getK,
            command= lambda _: self.getK.set(int(self.scale.get())),
        )
        self.scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        self.lableK = ttk.Label(
            self.tab, textvariable=self.getK
        )
        self.lableK.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")
        self.getK.set(4)
        ttk.Button(self.tab,text="btn",command=self.startCalu).grid(row=2, column=2, padx=(10, 20), pady=(20, 0), sticky="ew")

    def startCalu(self):
        self.dataSet = self.loadDataSet()
        self.centroidList = self.initCentroids(self.dataSet, self.getK.get())
        self.clusterDict = self.minDistance(self.dataSet, self.centroidList)
        self.newVar = self.getVar(self.centroidList, self.clusterDict)
        self.oldVar = 1  # 当两次聚类的误差小于某个值是，说明质心基本确定。
        self.times = 2
        while abs(self.newVar - self.oldVar) >= 0.00001:
            self.centroidList = self.getCentroids(self.clusterDict)
            self.clusterDict = self.minDistance(self.dataSet, self.centroidList)
            self.oldVar = self.newVar
            self.newVar = self.getVar(self.centroidList, self.clusterDict)
            self.times += 1
        self.showCluster(self.centroidList, self.clusterDict)

    def loadDataSet(self):
        dataSet = np.loadtxt("dataSet.csv")
        return dataSet
    
    def initCentroids(self,dataSet, k):
        # 从数据集中随机选取k个数据返回
        dataSet = list(dataSet)
        return random.sample(dataSet, k)
    
    def minDistance(self, dataSet, centroidList):

        # 对每个属于dataSet的item， 计算item与centroidList中k个质心的距离，找出距离最小的，并将item加入相应的簇类中
        clusterDict = dict() #dict保存簇类结果
        k = len(centroidList)
        for item in dataSet:
            vec1 = item
            flag = -1
            minDis = float("inf") # 初始化为最大值
            for i in range(k):
                vec2 = centroidList[i]
                distance = self.calcuDistance(vec1, vec2)  # error
                if distance < minDis:
                    minDis = distance
                    flag = i  # 循环结束时， flag保存与当前item最近的蔟标记
            if flag not in clusterDict.keys():
                clusterDict.setdefault(flag, [])
            clusterDict[flag].append(item)  #加入相应的类别中
        return clusterDict  #不同的类别
    
    def getVar(self,centroidList, clusterDict):
        # 计算各蔟集合间的均方误差
        # 将蔟类中各个向量与质心的距离累加求和
        sum = 0.0
        for key in clusterDict.keys():
            vec1 = centroidList[key]
            distance = 0.0
            for item in clusterDict[key]:
                vec2 = item
                distance += self.calcuDistance(vec1, vec2)
            sum += distance
        return sum
    
    def calcuDistance(self,vec1, vec2):
        # 计算向量1与向量2之间的欧式距离
        return np.sqrt(np.sum(np.square(vec1 - vec2)))  #注意这里的减号
    
    def getCentroids(self, clusterDict):
        #重新计算k个质心
        centroidList = []
        for key in clusterDict.keys():
            centroid = np.mean(clusterDict[key], axis=0)
            centroidList.append(centroid)
        return centroidList  #得到新的质心
    
    def showCluster(self, centroidList, clusterDict):
        # 展示聚类结果
        colorMark = ['or', 'ob', 'og', 'ok', 'oy', 'ow'] #不同簇类标记，o表示圆形，另一个表示颜色
        centroidMark = ['dr', 'db', 'dg', 'dk', 'dy', 'dw']

        for key in clusterDict.keys():
            plt.plot(centroidList[key][0], centroidList[key][1], centroidMark[key], markersize=12) #质心点
            for item in clusterDict[key]:
                plt.plot(item[0], item[1], colorMark[key])
        plt.show()
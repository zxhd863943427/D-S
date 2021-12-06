# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
import itertools
import numpy as np 
import pandas as pd 
from collections import defaultdict



# %%
#定义 Shapley 类
class Shapley:
    #输入的初始化数据应该为一个pd.df数据框，和元素数n
    def __init__(self,data:pd.DataFrame, n:int,cowName='uH') -> None:
        self.dataFrame = data
        self.n = n
        self.N = np.math.factorial(n)
        #调用初始化函数
        self.initElementSet()
        self.initSubsets()
        self.initDict(cowName)

####################################################################工具函数##########################################################   
    #返回全部子集
    #例子 
    #输入 s = ['m1','m2']
    #返回 ['m1','m2','m1,m2']
    def getSubsets(self,s):

        if len(s)==1:
            return s
        else:
            sub=[]
            for i in range(1,len(s)+1):
                sub.extend(map(list,itertools.combinations(s, i)))
        return list(map(",".join,map(sorted,sub)))

    #输入一个全排列结合以及对应的m1,返回一个m1出现的排列H1和去除m1的H1
    #例子
    #输入top_set = ['m1','m2','m1,m2'], m1='m1'
    #返回   [['m1',''],
    #       ['m1,m2','m2']]
    def uH_and_uH_without_m1(self,top_set,m1):
        answer = []
        for  subSet in top_set:
            if m1 in subSet:
                parent = subSet
                #清除m1的文本内容
                subSet=subSet.replace(m1+',','')
                subSet=subSet.replace(','+m1,'')
                subSet=subSet.replace(m1,'')
                child = subSet
                #加入到列表answer
                answer.append([parent,child])
        return answer

    #获取权重,输入一个子列表，自动生成权重
    def get_W(self, dubSet) ->int : 

        if dubSet == ['']:
            H = 0
        else:
            H = len(dubSet)    
        #计算权重
        W = np.math.factorial(H)*(np.math.factorial(self.n-H-1)) / np.math.factorial(self.n)
        return W

#####################################################初始化函数###################################################
    #初始贡献联盟字典
    def initDict(self,cowName):
        temp=dict(self.dataFrame[cowName])
        self.dataDict = defaultdict(int)
        self.dataDict.update(temp)
    
    #初始化元素集
    def initElementSet(self):
        self.elementSet = self.dataFrame.index[0:self.n]

    #初始化子集列表
    def initSubsets(self):
        index = self.elementSet
        self.subSets=self.getSubsets(index)

        
#####################################################计算函数####################################################
    #获取单个元素的Shapley值
    def getOneShapley(self,m_i):
        #提取出现m_i的子集和对应的排除m_i的子集
        m1=self.uH_and_uH_without_m1(self.dataDict,m_i)
        temp = 0
        #计算边际值
        for i in m1:
            a= self.dataDict[i[0]] -  self.dataDict[i[1]]
            list1 = i[1].split(',')
            a= self.get_W(list1) * a
            temp += a
        return(temp)

    def getAllShapley(self):
        self.shapleyValue = {}
        for i in self.elementSet:
            self.shapleyValue[i] = self.getOneShapley(i)
        return self.shapleyValue

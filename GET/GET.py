import re

def StrToInt(s):
    sum=0
    if s=='':
        return 0
    for i in s:
        sum=sum+pow(2,ord(i)-ord('a'))
    return sum

def IntToStr(i):
    cnt=0
    s=''
    while i>0:
        if i&1==1:
            s=s+chr(cnt+ord('a'))
        i=i>>1
        cnt=cnt+1
    return s

# 输入参数 m1 形如：[['',0.2],['a',0.5]]
def K_generator(m1,m2):
    k=0
    for i in m1:
        for j in m2:
            if StrToInt(i[0])&StrToInt(j[0])==0:
                k=i[1]*j[1]
    return k

# 输入参数 m1 形如：[['',0.2],['a',0.5]]
def M_generator(m1,m2):
    M={'':0}
    sum=0
    K=K_generator(m1,m2)
    for i in m1:
        for j in m2:
            if i[0]==j[0]=='':
                M['']=i[1]*j[1]
            t=StrToInt(i[0])&StrToInt(j[0])
            s=IntToStr(t)
            if(t==0):
                continue
            if s in M.keys():
                M[s]=M[s]+i[1]*j[1]
            else:
                M[s]=i[1]*j[1]
    L=[]
    for key in M:
        L.append([key,(1-M[''])*M[key]/(1-K)])
    return L

# 读取文件内信息生成 m，输入参数 文件名str
def m_generator(str):
    with open(str,"r") as f:
        m=f.readlines()
    cnt = 0
    for i in m:
        t = float(re.findall(r"\d+\.?\d*", i)[0])
        m[cnt] = [re.findall(r'[A-Za-z]*', i)[0], t]
        cnt = cnt + 1
    return m

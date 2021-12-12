import GET
import re

# 文件读入函数，输入参数为文件名
# 文件形式:每一行一个三角模糊数，形如 evidence a b c w
# 返回一个list，形如[['evidence',a,b,c,w]]
def s_input(file_name):
    with open(file_name,'r') as f:
        s=f.readlines()
    L=[]
    cnt=0
    for i in s:
        L.append([])
        L[cnt].append(re.findall(r'[A-Za-z]*', i)[0])
        for j in re.findall(r"\d+\.?\d*", i):
            L[cnt].append(float(j))
        cnt=cnt+1
    return L


# 强约束GBPA生成函数
# L为三角模糊数数据信息，形如[['evidence',a,b,c,w]]
# val为输入信息，浮点数
# 返回一个list列表，形如[['a',0.66666],['b',0.33333]]
def s_gbpa_generator(L,val):
    s={}
    sum=0
    for i in L:
        if val>i[1] and val<i[3]:
            if val<i[2]:
                s[i[0]]=(val-i[1])/(i[2]-i[1])
            else:
                s[i[0]]=(i[3]-val)/(i[3]-i[2])
            sum=sum+s[i[0]]
    M=[]
    str=''
    for i in sorted(s.items(),key=lambda item:item[1],reverse=True):
        str=GET.IntToStr(GET.StrToInt(str+i[0]))
        d=i[1]
        if sum>1:
            d=d/sum
        M.append([str,d])
    return M
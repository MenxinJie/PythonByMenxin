1.五角数
NUM=1
for n in range(1,101):
    def Pentagonalnumber(n):
        global NUM
        pentagonalnumber=n*(3*n-1)/2
        if NUM%10==0:
            print('%6d'%pentagonalnumber)
            NUM+=1
        else:
            print('%6d'%pentagonalnumber,end=' ')
            NUM+=1
    Pentagonalnumber(n)

#2.显示各位数字之和
NUM=0
n=int(input('请输入一个整数：'))
def sumDigits(n):
    global NUM
    NUM += n%10
    n = n//10
    if n>0:
        sumDigits(n)
    else:
        print('它的各位数字之和为：%d'%NUM)
sumDigits(n)

#3.升序显示三个数
num1,num2,num3=map(float,input('请输入三个数（中间用逗号隔开）：').split(','))
def displaySortedNumber(num1,num2,num3):
    print(sorted([num1,num2,num3]))
    return num1,num2,num3
displaySortedNumber(num1,num2,num3)

#4.求未来值
COUNT=0
investmentAmount=float(input('请输入投资额：'))
monthlyInterestRate=float(input('请输入年利率：'))
years=int(input('您想查看多少年后的未来值：'))
print('*******************************************')
print('[years]',end='  ')
print('[future Value]')
def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    global COUNT
    investmentAmount+=investmentAmount*(monthlyInterestRate/100)
    COUNT+=1
    if COUNT<=years:
        print('%4d'%COUNT,end='       ')
        print('%.2f'%investmentAmount)
        futureInvestmentValue(investmentAmount,monthlyInterestRate,years)
    else:
        print('*******************************************')
futureInvestmentValue(investmentAmount,monthlyInterestRate,years)

#5.输出一段字符
NUM=1
ch1=input('开头字符：')
ch2=input('末尾字符：')
numberPerLine=int(input('每行打印几个？'))
print('******************************************')
def printChars(ch1,ch2,numberPerLine):
    global NUM
for x in range(ord(ch1),ord(ch2)+1):
    if NUM%numberPerLine==0:
        print(chr(x))
        NUM+=1
    else:
        print(chr(x),end='   ')
        NUM+=1
printChars(ch1,ch2,numberPerLine)

#6.判断某年有多少天
for year in range(2010,2021):
    def numberOfDaysInAYear(year):
        if year%100==0:
            if year%400==0:
                print('%d年全年共有366天'%year)
            else:
                print('%d年全年共有365天'%year)
        else:
            if year%4==0:
                print('%d年全年共有366天'%year)
            else:
                print('%d年全年共有365天'%year)
    numberOfDaysInAYear(year)

#7.求两点之间的距离
x1,y1=map(float,input('请输入第一个点的坐标：').split(','))
x2,y2=map(float,input('请输入第二个点的坐标：').split(','))
def distace(x1,y1,x2,y2):
    d=((x1-x2)**2+(y1-y2)**2)**(1/2)
    print('两点之间的距离是：%.2f'%d)
distace(x1,y1,x2,y2)

#8.梅森素数
print('p      2^p-1')
for i in range(3,200):
    def MersennePrime(i):
        num=0
        for j in range(1,i+1):
            if i%j==0:
                num+=1
        if num<3:
            for p in range(1,32):
                if i==2**p-1:
                    print('%d     %4d'%(p,i))
    MersennePrime(i)

#9.打印时间    
import time
print ('time.time(): %f'%time.time())
print (time.localtime(time.time()))
print (time.asctime(time.localtime(time.time())))

#10.摇骰子
RES=0
import numpy as np
def DiYiLun():
    global RES
    a = np.random.choice([1,2,3,4,5,6])
    b = np.random.choice([1,2,3,4,5,6])
    if a+b==2 or a+b==3 or a+b==12:
        print('你摇出了%d+%d=%d，你输了！'%(a,b,a+b))
    elif a+b==7 or a+b==11:
        print('你摇出了%d+%d=%d，你赢了！'%(a,b,a+b))
    else:
        RES += (a+b)
        print('你摇出了%d+%d=%d'%(a,b,a+b))
        print('结果是%d'%(a+b))
        XiaYiLun()

def XiaYiLun():
    c = np.random.choice([1,2,3,4,5,6])
    d = np.random.choice([1,2,3,4,5,6])
    if c+d==7:
        print('你摇出了%d+%d=%d，你输了！'%(c,d,c+d))
    elif c+d == RES :
        print('你摇出了%d+%d=%d，你赢了！'%(c,d,c+d))
    else:
        XiaYiLun()

if __name__ == "__main__":
    DiYiLun()
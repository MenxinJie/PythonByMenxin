#1.
C=float(input('输入摄氏温度：'))
F=(9/5)*C+32
print('%.1f摄氏度=%.1f华氏度'%(C,F))

#2.
import math
r,l=map(float,input('请输入圆柱的半径和高（中间用逗号隔开）：').split(','))
area=r*r*math.pi
volume=area*l
print('圆柱的底面积为：%.4f，圆柱的体积为：%.2f'%(area,volume))

#3.
feet=float(input('请输入英尺数：'))
meter=feet*0.305
print('%.5f英尺=%.4f米'%(feet,meter))

#4.
M=float(input('请输入水量（单位千克）：'))
i=float(input('请输入初始温度（单位：摄氏度）：'))
f=float(input('请输入最终温度（单位：摄氏度）：'))
Q=M*(f-i)*4184
print('把%.3f千克水从%.3f摄氏度加热到%.3f摄氏度需要%.1f焦耳能量。'%(M,i,f,Q))

#5.
blance,interestrate=map(float,input('请输入差额和年利率（中间用逗号隔开）：').split(','))
interest=blance*(interestrate/1200)
print('您下月要付利息：%.5f'%interest)

#6.
v0,v1,t=map(float,input('请输入初始速度(m/s)，末速度(m/s)和时间(t)：').split(','))
a=(v1-v0)/t
print('平均加速度为：%.4f'%a)

#7.
num=float(input('请输入每月存款数：'))
MonthInterest=0.05/12
month1=num*(1+MonthInterest)
month2=(num+month1)*(1+MonthInterest)
month3=(num+month2)*(1+MonthInterest)
month4=(num+month3)*(1+MonthInterest)
month5=(num+month4)*(1+MonthInterest)
month6=(num+month5)*(1+MonthInterest)
print('六个月后您的账户总额为：%.2f'%month6)

#8.
num=int(input('请输入一个0到1000的整数：'))
qian=num//1000
bai=(num//100)
if bai==10:
    bai=0
shi=(num%100)//10
ge=(num%100)%10
result=qian+bai+shi+ge
print('%.0d的各位数字之和是%.0d'%(num,result))
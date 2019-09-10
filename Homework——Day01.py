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

#9.
r=float(input('请输入五边形顶点到中心的距离：'))
import math
s=2*r*math.sin(math.pi/5)
Area=5*s*s/(4*math.tan(math.pi/5))
print("五边形的面积是：%.2f"%Area)

#10.
import math
X1,Y1=map(float,input('请输入第一个点的坐标：').split(','))
X2,Y2=map(float,input('请输入第二个点的坐标：').split(','))
x1=math.radians(X1)
x2=math.radians(X2)
y1=math.radians(Y1)
y2=math.radians(Y2)
radius=6371.01
d=radius*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print('这两点之间的距离是：%.11fkm'%d)

#11.有问题
import math
s=float(input('请输入五角形的边长：'))
Area=(5*s*s)/4*(math.tan(math.pi/5))
print('五角形的面积是：%.14f'%Area)

# 12.有问题
import math
n,s=map(float,input('请输入正多边形的边数及边长（中间用逗号隔开）：').split(','))
Area=n*s*s/4*math.tan(math.pi/n)
print('面积为：%.14f'%Area)

#13.
a=int(input('请输入一个ASCII值(0~127)：'))
print(a,'对应的符号为：',chr(a))

#14.
name=input('请输入姓名：')
time=float(input('请输入一周的工作时间：'))
hourlypay=float(input('请输入每小时报酬：'))
federaltax=float(input('请输入联邦预扣税率（0.00）：'))
statetax=float(input('请输入州预扣税率（0.00）：'))
pay=time*hourlypay
federalpay=federaltax*pay
statepay=statetax*pay
total=federalpay+statepay
netpay=pay-total
print('雇员姓名：',name)
print('工作时间：',time)
print('每小时报酬：$%.2f'%hourlypay)
print('本周工资：$%.2f'%pay)
print('扣除:')
print('    联邦税：$%.2f'%federalpay)
print('    州税：$%.2f'%statepay)
print('    总扣除：$%.2f'%total)
print('实发工资：$%.2f'%netpay)

#15.
num=input('请输入一个四位整数：')
num1=num[::-1]
print('结果为：',num1)

#16.
#加密一串文本并将密文写入本地保存。
#不会！
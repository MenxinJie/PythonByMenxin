# 1.
a,b,c=map(float,input('请输入a,b,c的值（中间用逗号隔开）：').split(','))
delta=b**2-4*a*c
r1=(-b + delta**0.5)/2*a
r2=(-b - delta**0.5)/2*a
if delta>0:
    print(r1,r2)
elif delta<0:
    print('无实根')
else:
    print(r1)

# 2.
import numpy as np
i = np.random.choice([1,99])
j = np.random.choice([1,99])
print('%d+%d=?'%(i,j))
res=i+j
num=int(input('请输入结果：'))
if num==res:
     print('恭喜你答对了！🎉')
else:
     print('答错了，继续努力！😂')

# 3.
today=int(input('今天星期几？请告诉我：'))
days=int(input('您要查找几天之后？请告诉我：'))
res=(days%7)+today
if res>6:
    res-=6
if res==0:
    print('%d天之后是星期日'%days)
elif res==1:
    print('%d天之后是星期一'%days)
elif res==2:
    print('%d天之后是星期二'%days)
elif res==3:
    print('%d天之后是星期三'%days)
elif res==4:
    print('%d天之后是星期四'%days)
elif res==5:
    print('%d天之后是星期五'%days)
else:
    print('%d天之后是星期六'%days)

# 4.
a,b,c=map(int,input('请输入三个整数：').split(','))
if a>b>c:
    print('%d < %d < %d'%(c,b,a))
elif a>c>b:
    print('%d < %d < %d'%(b,c,a))
elif b>c>a:
    print('%d < %d < %d'%(a,c,b))
elif b>a>c:
    print('%d < %d < %d'%(c,a,b))
elif c>a>b:
    print('%d < %d < %d'%(b,a,c))
elif c>b>a:
    print('%d < %d < %d'%(a,b,c))

# 5.
k1,p1=map(float,input('请输入第一种包装的重量（kg）和价格（￥）:').split(','))
k2,p2=map(float,input('请输入第二种包装的重量（kg）和价格（￥）:').split(','))
res1=p1/k1
res2=p2/k2
if res1>res2:
    print('第二种包装性价比更高！')
elif res1<res2:
    print('第一种包装性价比更高！')
else:
    print('都一样，买哪个都行！')

# 6.
mouth,year=map(int,input('请输入月份和年份（中间用逗号隔开）：').split(','))
if mouth in ['1','3','5','7','8','10','12']:
    print('%d年%d月有31天！'%(year,mouth))
else:
    if mouth==2 and year%4==0:
        print('%d年%d月有29天！'%(year,mouth))
    else:
        print('%d年%d月有30天！'%(year,mouth))

# 7.
import numpy as np
res=np.random.choice(['正','反'])
user=input('硬币已弹起，正还是反？请输入你的猜测：')
if res==user:
    print('你猜对了！')
else:
    print('你猜错了！')

# 8.
user=input('剪刀（0），石头（1），布（2），你出什么？')
import numpy as np
com=np.random.choice([0,2])
if user==com:
    print('平局！')
else:
    if user==0 and com==1:
        print('你输了！')
    elif user==1 and com==2:
        print('你输了！')
    elif user==2 and com==0:
        print('你输了！')
    else:
        print('你赢了！')

# 9.
y,m,q=map(int,input('请输入年份，月份，日期（中间用逗号隔开）：').split(','))
if m==1:
    m=13
    y-=1
if m==2:
    m=14
    y-=1
j=(y/100)//1
k=y%100
h=(q+((26*(m+1)/10)//1)+k+(k/4)//1+(j/4)//1+5*j)%7
if h==0:
    print('这天是星期六！')
elif h==1:
    print('这天是星期天！')
elif h==2:
    print('这天是星期一！')
elif h==3:
    print('这天是星期二！')
elif h==4:
    print('这天是星期三！')
elif h==5:
    print('这天是星期四！')
elif h==6:
    print('这天是星期五！')
   
# 10.
import numpy as np
a=np.random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
b=np.random.choice(['梅花','黑桃','方块','红桃'])
print('您抽出的牌是：',b,a)

# 11.
num=input('请输入一个三位整数：')
num1=num[::-1]
if num==num1:
    print(num,'是一个回文数！')
else:
    print(num,'不是一个回文数！')

# 12.
a,b,c=map(float,input('请输入三角形的三边长度：').split(','))
if a+b>c and a+c>b and b+c>a:
    print('周长为：%d'%(a+b+c))
else:
    print('输入不合法！')

# 13.
z,f,zz,ff,=0,0,0,0
a=int(input('请输入一个整数：'))
if a==0:
    print('无效！')
else:
    if a>0:
        z+=1
        zz+=a
    elif a<0:
        f+=1
        ff+=a
    while True:
        b=int(input('请输入一个整数：'))
        if b>0:
            z+=1
            zz+=b
        elif b<0:
            f+=1
            ff+=b
        else:
            print('*****************************************')
            print('负数有%d个,正数有%d个'%(f,z))
            print('负数的和为%d,正数的和为%d'%(ff,zz))
            print('总和为%d'%(ff+zz))
            print('平均值为%f'%((ff+zz)/(f+z)))
            print('*****************************************')

# 14.
a=10000
b=0.05
c=0
while c<= 10:
    d=0
    a=a*(1+0.05)
    x1=a
    while d<4:
        x2=x1*(1+0.05)
        x3=x2*(1+0.05)
        x4=x3*(1+0.05)
        d+=1
    print('从%d年之后起，大学四年的总学费为：%.2d'%(c,x1+x2+x3+x4))
    c+=1
print(c-1,'年之后的学费是：%.2f'%a)

# 15.
num=1
for i in range(100,1000):
    if i%5==0 and i%6==0:
        if num%10==0:
            print('%d'%i)
            num+=1
        else:
            print('%d'%i,end=' ')
            num+=1
    
# 16.
n1=1
while n1**2<=12000:
    n1+=1
print('使得它的平方大于12000的最小正整数为：%d'%n1)
n2=1
while n2**3<=12000:
    n2+=1
print('使得它的平方大于12000的最小正整数为：%d'%n2)

# 17.
num=0
for i in range(1,50001):
    num=num+(1/i)
print('从左到右：',num)
num=0
for i in range(50000,0,-1):
    num=num+(1/i)
print('从右到左：',num)

# 18.
num=0
for a in range(1,98,2):
    for b in range(3,100,2):
        num=num+a/b
print(num)

# 19.
num=0
for i in range(1,100001):
    num=num+4*((-1)**(i+1)/(2*i-1))
    if i%10000==0:
        print('i=%d时，Π=%f'%(i,num))

# 20.
for i in range(6,10000):
    num=0
    for k in range(1,i):
        if i%k==0:
            num+=k
    if i==num:
        print(num,end='   ')

# 21.
num=0
for a in range(1,8):
    for b in range(1,8):
        if a!=b:
            print('%d%d'%(a,b))
            num+=1
print('一共有%d种组合'%num)

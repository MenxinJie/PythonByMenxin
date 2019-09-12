#1.成绩分级
def ScoreGrade()):
    list1=list(map(int,input('Please enter score:').split(',')))
    list2=sorted(list1)
    best=list2[-1]
    for i in range(0,len(list1)):
        if best>=list1[i]>=best-10:
            print('Student %d score is %d and grade is A !'%(i,list1[i]))
        elif best-10>list1[i]>=best-20:
            print('Student %d score is %d and grade is B !'%(i,list1[i]))
        elif best-20>list1[i]>=best-30:
            print('Student %d score is %d and grade is C !'%(i,list1[i]))
        elif best-30>list1[i]>=best-40:
            print('Student %d score is %d and grade is D !'%(i,list1[i]))
        else:
            print('Student %d score is %d and grade is E !'%(i,list1[i]))
if __name__ == '__main__':
    ScoreGrade()

#2.逆序读取列表
def Nixu():
    list_ = list(map(int,input('Please enter integers：').split(',')))
    print(list_[::-1])
if __name__ == '__main__':
    Nixu()

#3.统计列表里元素的个数
def Statistics():
    list_=list(map(int,input('Please enter integers between 1 and 100：').split(',')))
    set_=set(list_)
    for i in set_:
        number=0
        for j in list_:  
            if j==i:
                number+=1
        print('Number %d has %d '%(i,number))
if __name__ == '__main__':
    Statistics()

4.第1题和第3题的结合
def Statistics():
    list_=list(map(int,input('Please enter grade ：').split(' ')))
    total=0
    good=0
    for i in range(0,len(list_)):
        total += list_[i]
    average=total/len(list_)
    for grade in list_:
        if grade >= average:
            good+=1
    print('    The average score is %d '%average)
    print('   %d students with scores greater than or equal to the average score!'%good)
    print('   %d students with lower than average scores!'%(len(list_)-good))
if __name__ == '__main__':
    Statistics()

#5.随机产生一串数字，然后统计每个数字个数
import numpy as np
import sys
sys.setrecursionlimit(100000)   #加大最大递归深度，否则会报错
NUM=0
LIST1=list(x for x in range(0,10))
LIST2=[]
counts=[0,0,0,0,0,0,0,0,0,0]
def Statistics():
    global LIST1,LIST2
    if len(LIST2) < 1000:
        List()
    else:
        for i in LIST2:
            counts[i]+=1
        print('1000个随机数中0~9的个数分别为',counts)    
def List():
    global NUM,LIST1,LIST2
    if NUM != 1000:
        LIST2.append(np.random.choice(LIST1))
        NUM += 1
        List()
    else:
        Statistics()
if __name__ == '__main__':
    Statistics()

#6.输出最小元素的下标
def IndexOfSmallestElement():
    list1=list(map(int,input('Please enter a list of numbers:').split(',')))
    list2=sorted(list1)
    num=0
    for i in list1:
        if i==list2[0]:
            print('The subscript of the smallest element is：%d'%num)
        else:
            num+=1
if __name__ == '__main__':
    indexOfSmallestElement()

#7.打乱一个列表并返回这个列表
import random
lst=list(map(int,input('Please enter a list of number:').split(' ')))
def Shuffle(lst):
    random.shuffle(lst)
    for i in lst:
       print(i,end=' ')
if __name__ == '__main__':
    Shuffle(lst)

#8.消除重复
lst=list(map(int,input('Please enter a list of number:').split(' ')))
def eliminateDupLicates(lst):
    set1=set(lst)
    for i in set1:
        print(i,end=' ')   
if __name__ == '__main__':
    eliminateDupLicates(lst)

#9.检测是否排序
lst=list(map(int,input('Please enter a list of number:').split(' ')))
def isSorted(lst):
    if lst != sorted(lst):
        print('Not sorted !')
    else:
        print('Already sorted !')
if __name__ == '__main__':
    isSorted(lst)

#10.冒泡排序
lst=list(map(int,input('Please enter a list of number:').split(' ')))
def MaoPaoSort(lst):
    while lst != sorted(lst):
        for i in range(0,len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i] #不能分两行写，会刷新列表
    else:
        print(lst)
if __name__ == '__main__':
    MaoPaoSort(lst)

# #11.不会！！
# def puke():
#     # import sys
#     # sys.setrecursionlimit(100000)
#     import random
#     import numpy as np
#     list_=([x+y for x in ['黑桃','红桃','方块','梅花'] for y in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']])
#     random.shuffle(list_)
#     YZ=[]
#     RES=[]
#     NUM=0
#     choice()
# def choice():
#     globals YZ,RES,NUM
#     if len(YZ)!=4:
#         i=np.random.choice(list_)
#         if i[0:1] not in YZ:
#             YZ.append(i[0:1])
#             RES.append(i)   
#         else:
#             choice()
#     else:
#         print(NUM)
#         print(RES)
# if __name__ == '__main__':
#     puke()

#12.判断序列包含具有相同值的连续四个数字
def isconsecutivefour():
    num=0
    list_=list(map(int,input('请输入一个整数序列（用逗号隔开）:').split(',')))
    for i in range(0,len(list_)-3):
        if list_[i]==list_[i+1]==list_[i+2]==list_[i+3]:
            if num==0:
                print('这个序列包含具有相同值的连续四个数字！')
                num+=1
    if num==0:
        print('不包含！')
if __name__ == '__main__':
    isconsecutivefour()

#13.检测SSN
def Ssn():
    ssn='111-222-3333'
    list_=str(input('请输入SSN号码（ddd-ddd-dddd）:'))
    a=list_[0]+list_[1]+list_[2]
    b=list_[4]+list_[5]+list_[6]
    c=list_[8]+list_[9]+list_[10]+list_[11]
    if a+'-'+b+'-'+c == ssn:
        print('Ture')
    else:
        print('False')
if __name__ == '__main__':
    Ssn()

#14.
def Find():
    a=str(input('请输入第一个字符串：'))
    b=str(input('请输入第二个字符串：'))
    res=b.find(a)
    if res==-1:
        print(a,'不是',b,'的子串')
    else:
        print(a,'是',b,'的子串')
if __name__ == '__main__':
    Find()

# 15.睡觉

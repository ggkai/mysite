'''
https://matplotlib.org/gallery/index.html
https://matplotlib.org/tutorials/index.html
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

#曲线图
plt.figure(1)
a=[1,2,3,4]
plt.plot(a)

plt.figure(2)
plt.plot([1,2,3,4],[1,4,9,16],'ro')

plt.figure(3)
x=np.linspace(-2,2,10)
y=2*x+1
z=x**2
plt.plot(x,y,label='linear line')
plt.plot(x,z,color='red',label='square line',linewidth=1.0,linestyle='--')
plt.legend()#加图例
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.spines['top'].set_color('None')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.spines['right'].set_color('None')


plt.figure(4)
b=np.arange(0,5,0.2)
plt.plot(b,b,'r--',b,b**2,'bs',b,b**3,'g^')

#直方图
plt.figure(5)
c=100+15*np.random.randn(1000)
plt.hist(x=c,bins=50,density=1,color='g',alpha=0.5)
plt.xlabel('x')#加轴标签
plt.ylabel('y')#加轴标签
plt.title('histogram')#加标题
plt.text(x=60,y=0.025,s=r'$\mu=100,\sigma=15$')#加标注
plt.axis(xmin=40,xmax=160,ymin=0,ymax=0.04)
plt.annotate(s='hello',xy=(120,0.01),xytext=(140,0.02),arrowprops = dict(color='k',arrowstyle='->'))#加点标注
plt.grid(True)

#柱状图
plt.figure(6)
d=np.arange(10)
e=np.random.uniform(0,10,10)
f=np.random.uniform(0,10,10)
plt.bar(x=d,height=e,width=0.3,edgecolor='w')
plt.bar(x=d+0.3,height=f,width=0.3,edgecolor='w')

plt.figure(7)
d=np.arange(10)
e=np.random.uniform(0,10,10)
f=np.random.uniform(0,10,10)
plt.bar(x=d,height=e,width=0.5,edgecolor='w',facecolor='#9999ff')
plt.bar(x=d,height=-f,width=0.5,edgecolor='w',facecolor='#ff9999')
for x, y in zip(d,e): #数据加标签
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(d,f): #数据加标签
    plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')

#散点图
plt.figure(8)
e=np.random.randn(1,100)
f=np.random.randn(1,100)
g=np.arctan2(e,f)
plt.scatter(x=e,y=f,s=25,c=g,alpha=0.4,marker='o')#c是散点的颜色，s是散点的大小

#饼状图
plt.figure(9)
h=[u'part1',u'part2',u'part3']
i=[60,30,10]
j=['r','y','b']
plt.pie(x=i,labels=h)

#箱线图
plt.figure(10)
k=pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','e'])
plt.boxplot(x=k)

#3D散点图
fig=plt.figure(11)
ax=Axes3D(fig)
l=np.random.normal(0,1,100)
m=np.random.normal(0,1,100)
n=np.random.normal(0,1,100)
ax.scatter(xs=l, ys=m, zs=n)

#3D线型图
fig=plt.figure(12)
ax=Axes3D(fig)
o=np.linspace(-6*np.pi,6*np.pi,100)
p=np.sin(o)
q=np.cos(o)
ax.plot(xs=o,ys=p,zs=q)

#3D柱状图
fig=plt.figure(13)
ax=Axes3D(fig)
x = [0, 1, 2, 3, 4, 5, 6]
for i in x:
  y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  z = abs(np.random.normal(1, 10, 10))
  ax.bar(left=y, height=z,zs=i, zdir='y', color=['r', 'g', 'b', 'y'])

#3D曲面图
fig=plt.figure(14)
ax=Axes3D(fig)
x=np.arange(-2,2,0.1)
y=np.arange(-2,2,0.1)
x,y=np.meshgrid(x,y)
z=np.sqrt(x**2+y**2)
ax.plot_surface(X=x,Y=y,Z=z,cmap=plt.cm.winter)

#3D线型散点混合图
fig=plt.figure(15)
ax=Axes3D(fig)
x1=np.linspace(-3*np.pi,3*np.pi,500)
y1=np.sin(x1)
z1=np.cos(x1)
ax.plot(xs=x1,ys=y1,zs=z1)

x2=np.random.normal(0,1,100)
y2=np.random.normal(0,1,100)
z2=np.random.normal(0,1,100)
ax.scatter(xs=x2,ys=y2,zs=z2)

#等高线
plt.figure(16)
x=np.linspace(-3,3,10)
y=np.linspace(-3,3,10)
x,y=np.meshgrid(x,y)
z=(1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
plt.contourf(x,y,z,8,alpha=0.75,cmap=plt.cm.hot)
cb = plt.colorbar(orientation='horizontal')#添加颜色带，默认竖直放置
cb.set_label('meters')
C=plt.contour(x,y,z,8,colors='black')
plt.clabel(CS=C,inline=True, fontsize=10)

#图片
plt.figure(17)
x=np.linspace(0,1,9).reshape(3,3)
plt.imshow(X=x,interpolation='nearest',cmap='bone',origin='lower')
plt.colorbar(shrink=0.9)

#动画
fig=plt.figure(18)
ax=plt.subplot()
x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))
def animate(i):
    line.set_ydata(np.sin(x+i/10.0))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
ani=animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=False)
#ani.save('line_animation.mp4',fps=30,extra_args=['-vcodec', 'libx264'])#保存动画

#趋势线和平均线
plt.figure(19)
a = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
b = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(a, b, deg=1)#deg=1表示1阶
p = np.poly1d(z)
font = {'family':'SimHei'} #设置使用的中文字体为SimHei
plt.rc('font',**font)#设置显示中文字体
plt.plot(a,b,label='data',color='c')#曲线
plt.plot(a,p(a),label='Trend Lines趋势线',color='m')#趋势线
plt.axhline(b.mean(),color='y')#平均线
plt.legend()#添加图例
#plt.savefig('TrendLines.png')

plt.show()
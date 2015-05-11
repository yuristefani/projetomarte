import numpy as np
import matplotlib.pyplot as plt

t=3.1415
x=(-2*1684.5*abs(np.tan(t))+((2*1684.5*np.tan(t))**2-4*(abs(np.tan(t))**2+1)*(1684.5**2-1714.5**2))**0.5)/(2*(abs(np.tan(t))**2+1))
y=(1714.5**2-x**2)**0.5
g=((y-1684.5)**2+x**2)**0.5
t=0
xx=list()
yy=list()
t0=273-50
emi=0.8
ab=0.7
temp=list()
m=0.003
m2=36/(10*900)

temp2=list()
plae=0.09
litros=10
tempa=list()
tempa.append(290)
plaa=0.7
temp.append(t0)
k=list()
yy=list()
taxa=10
yyy=list()
yyy.append(t0)

mult=1
ll=list()
lp=list()
for j in range(10):
    if j==9:
        for l in range(1,501):
            y=l/10
            ll.append(y)
            temp2=list()
            yy=list()
            xx=list()
            k=list()
            tempa=list()
            m3=36/(y*4200)
            
            m4=(m2**(-1)+m3**(-1))**(-1)
            temp2.append(temp[-1])
            yy.append(yyy[-1])
            yy.append(yyy[-1])
            for i in range(2468):
                if i>=617 and i <=1851:
                    t=((i-617)/(1234))*np.pi
                    x=(-2*1684.5*abs(np.tan(t))+((2*1684.5*np.tan(t))**2-4*(abs(np.tan(t))**2+1)*(1684.5**2-1734.5**2))**0.5)/(2*(abs(np.tan(t))**2+1))
                    y=(1734.5**2-x**2)**0.5
                    g=((y-1684.5)**2+x**2)**0.5
                    g=559*0.36**(g/50)
                    temp2.append(temp2[-1]+m*(g*ab*np.sin(t)/(1-(1-ab)*0.74)+((temp2[-1])**4)*5.67*(10**(-8))*emi*((0.74*ab)/(1-0.74*ab*(1-ab))-1)))
                else:
                    temp2.append(temp2[-1]+m*((temp2[-1])**4*5.67*10**(-8)*emi)*((0.74*ab)/(1-0.74*ab*(1-ab))-1))
                    g=0
                if 293<yy[-1] and yy[-1]>yy[-2]:
                        yy.append(yy[-1]+(g*plaa-((yy[-1])**4)*5.67*(10**(-8))*plae-((yy[-1]-temp2[-1])**4)*5.67*(10**(-8))*plae-1.2*(yy[-1]-temp2[-1]))*(m4))
                        tempa.append(yy[-1])
                else:
                    yy.append(yy[-1]+(g*plaa-((yy[-1])**4)*5.67*(10**(-8))*plae-((yy[-1]-temp2[-1])**4)*5.67*(10**(-8))*plae-1.2*(yy[-1]-temp2[-1]))*m2)
                    if i <1234:
                        tempa.append(293)
                    else:
                        tempa.append(tempa[-1])
                xx.append(i/100)
                k.append(g)
            lp.append(tempa[-1])
    else:
        for i in range(2468):
            if i>=617 and i <=1851:
                t=((i-617)/1234)*np.pi
                x=(-2*1684.5*abs(np.tan(t))+((2*1684.5*np.tan(t))**2-4*(abs(np.tan(t))**2+1)*(1684.5**2-1734.5**2))**0.5)/(2*(abs(np.tan(t))**2+1))
                y=(1734.5**2-x**2)**0.5
                g=((y-1684.5)**2+x**2)**0.5
                g=559*0.36**(g/50)
                temp.append(temp[-1]+m*(g*np.sin(t)*ab//(1-(1-ab)*0.74)+((temp[-1])**4)*5.67*(10**(-8))*emi*((0.74*ab)/(1-0.74*ab*(1-ab))-1)))
            else:
                temp.append(temp[-1]+m*(temp[-1])**4*5.67*10**(-8)*emi*((0.74*ab)/(1-0.74*ab*(1-ab))-1))
                g=0
            yyy.append(yyy[-1]+m2*(g*plaa-((yyy[-1])**4)*5.67*(10**(-8))*plae-((yyy[-1]-temp[-1])**4)*5.67*(10**(-8))*plae-1.2*(yyy[-1]-temp[-1])))
del temp2[0]
del yy[0]
del yy[0]
print(len(tempa))
print(len(temp2))
print(len(yy))
for i in range(len(temp2)):
    yy[i]-=273
    temp2[i]-=273
    tempa[i]-=273
    
for i in range(len(lp)):
    lp[i]-=273
line, = plt.plot(ll,lp, lw=2)
plt.show()
line, = plt.plot(xx,k, lw=2)
plt.show()
line, = plt.plot(xx,temp2, lw=2)
plt.show()
line, = plt.plot(xx,yy, lw=2)
plt.show()
line, = plt.plot(xx,tempa, lw=2)
plt.show()
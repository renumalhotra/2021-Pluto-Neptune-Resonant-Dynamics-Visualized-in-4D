import rebound
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd

sim = rebound.Simulation()
sim.units = ('yr','AU','Msun')
G = sim.G

### READING IN OBJECTS FROM HORIZONS, comment out lines 13-14 if objects are to be added manually

labels = ['Sun','Neptune','Pluto']
sim.add(labels)

### MANUALLY ADDING OBJECTS, uncomment lines 18-23 to use this method

# a_N = 30.275 #neptune distance
# a_P = 39.805 #pluto distance

# sim.add(m=1.0) #adding Sun
# sim.add(m=5e-5, a=a_N, e=0.0129, inc=0.031,Omega=2.299,omega=-2.004, f = -0.458) #adding Neptune
# sim.add(m=0,e=0.25, a=a_P*1.01, inc=0.299,Omega=1.925,omega=2.013,f=-5.071) #adding Pluto

sun = sim.particles[0]
neptune = sim.particles[1]
pluto = sim.particles[2]

sim.move_to_com()
fig = rebound.OrbitPlot(sim,slices=True)
sim.integrator = 'whfast'

# setting integration time, timestep, and array of time intervals
totaltime = 20000
timestep = 5
ntimes = int(totaltime/timestep +1)
times = np.linspace(0,totaltime,ntimes)
n = int(totaltime/neptune.P)

# pluto x y z values
xp = np.zeros(ntimes)
yp = np.zeros(ntimes)
zp = np.zeros(ntimes)

# neptune x y z values
xn = np.zeros(ntimes)
yn = np.zeros(ntimes)
zn = np.zeros(ntimes)

# integrating particles and saving x y z values of pluto and neptune to empty arrays created in lines 41-48
for j, time in enumerate(times):
    sim.integrate(time)
    xp[j] = pluto.x
    yp[j] = pluto.y
    zp[j] = pluto.z
    xn[j] = neptune.x
    yn[j] = neptune.y
    zn[j] = neptune.z

# calculating average angular speed of neptune    
omega = 2*np.pi/neptune.P 

# calculating rotation angle of neptune at each time interval based on average angular speed
thetas = []
for i in times:
    thetas.append(-(omega*i)+(9*np.pi/180.))

# pluto rotated x y values
xpRot = []
ypRot = []

# neptune rotated x y values
xnRot = []
ynRot = []


# rotating x y values of neptune and pluto using calculated angles
for i, theta in enumerate(thetas):
    R = np.array([np.cos(theta), -np.sin(theta), np.sin(theta), np.cos(theta)]).reshape(2,2)
    
    xy_n = np.ones(2).reshape(2,1)
    xy_n[0] = xn[i]
    xy_n[1] = yn[i]
    xy_n_rot = np.matmul(R,xy_n)
    xnRot.append(xy_n_rot[0])
    ynRot.append(xy_n_rot[1])
    
    xy_p = np.ones(2).reshape(2,1)
    xy_p[0] = xp[i]
    xy_p[1] = yp[i]
    xy_p_rot = np.matmul(R,xy_p)
    xpRot.append(xy_p_rot[0])
    ypRot.append(xy_p_rot[1])

data = pd.DataFrame()

data['xp'] = np.array(xp)
data['yp'] = np.array(yp)
data['zp'] = np.array(zp)
data['xpRot'] = np.array(xpRot)
data['ypRot'] = np.array(ypRot)
data['xn'] = np.array(xn)
data['yn'] = np.array(yn)
data['zn'] = np.array(zn)
data['xnRot'] = np.array(xnRot)
data['ynRot'] = np.array(ynRot)

data.to_csv('rebound_data.txt', sep = ' ', index = False)

plt.rc('font', family='serif')
plt.figure(figsize=(10,10),frameon=False)
plt.scatter(0,0,s=400,label='Sun',color='orange')
plt.plot(xpRot,ypRot,'-',label = 'Pluto',color='blue')
plt.plot(xnRot, ynRot, '-', label = 'Neptune',color='red')
plt.xlim(-50,50)
plt.ylim(-60,60)
plt.minorticks_on()
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.tick_params(which='major',bottom='on',left='on',direction='in',length=10)
plt.tick_params(which='minor',bottom='on',left='on',direction='in',length=5)
#plt.title('Rotating Frame xy plot',fontsize=24)
plt.xlabel('x (AU)',fontsize=24)
plt.ylabel('y (AU)',fontsize=24)
plt.legend(fontsize=24,loc=1)
#plt.savefig('xy_plot.jpg',bbox_inches='tight',dpi=300)

plt.figure(figsize=(10,10))
plt.plot(xpRot,zp,'-',label = 'Pluto',color='blue')
plt.plot(xnRot, zn, '-', label = 'Neptune',color='red')
plt.scatter(0,0,s=400,label='Sun',color='orange')
plt.xlim(-50,50)
plt.ylim(-40,40)
plt.minorticks_on()
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.tick_params(which='major',bottom='on',left='on',direction='in',length=10)
plt.tick_params(which='minor',bottom='on',left='on',direction='in',length=5)
#plt.title('Rotating Frame xz plot',fontsize=24)
plt.xlabel('x (AU)',fontsize=24)
plt.ylabel('z (AU)',fontsize=24)
plt.legend(fontsize=24,loc=1)
#plt.savefig('xz_plot.jpg',bbox_inches='tight',dpi=300)

plt.figure(figsize=(10,10))
plt.scatter(0,0,s=400,label='Sun',color='orange')
#plt.scatter(0,0,s=1000,label='Sun',marker='o',facecolors='none',edgecolors='orange')
plt.plot(ypRot,zp,'-',label = 'Pluto',color='blue')
plt.plot(ynRot, zn, '-', label = 'Neptune',color='red')
plt.xlim(-50,50)
plt.ylim(-40,40)
plt.minorticks_on()
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.tick_params(which='major',bottom='on',left='on',direction='in',length=10)
plt.tick_params(which='minor',bottom='on',left='on',direction='in',length=5)
#plt.title('Rotating Frame yz plot',fontsize=24)
plt.xlabel('y (AU)',fontsize=24)
plt.ylabel('z (AU)',fontsize=24)
plt.legend(fontsize=24,loc=1)
#plt.savefig('yz_plot.jpg',bbox_inches='tight',dpi=300)


fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.scatter3D(0, 0, 0, c='orange',s=400,label='Sun')
ax.plot3D(data.xpRot,data.ypRot,data.zp,color='blue',label='Pluto')
ax.plot3D(data.xnRot,data.ynRot,data.zn,color='red',label='Neptune')
ax.view_init(15,-9)
ax.set_zlim(-50,50)
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
ax.set_xlabel('x (AU)',fontsize=24)
ax.set_ylabel('y (AU)',fontsize=24)
ax.set_zlabel('z (AU)',fontsize=24)
plt.legend(fontsize=24)
plt.savefig('xyz_plot.jpg',bbox_inches='tight',dpi=300)
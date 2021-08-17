import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd

data = pd.read_csv('rebound_data.txt',sep = ' ')
# print(data.head())
# print(len(data))

xp = data.xp
yp = data.yp
zp = data.zp
xpRot = data.xpRot
ypRot = data.ypRot
xn = data.xn
yn = data.yn
zn = data.zn
xnRot = data.xnRot
ynRot = data.ynRot

plt.rc('font', family='serif')

# the following four functions are used to generate frames that are combined into an animation in animator.py
# for plotter_xy, plotter_yz, and plotter_xz, you can either plot the full orbits in each frame or use a background image to reduce file size and runtime
# the plt.plot lines in these three functions are used to plot the full orbits in each frame
# img = plt.imread('background_image_name.jpg') and plt.imshow are used to implement a background image
# be sure to comment out the method you do not wish to use
# for background images, these must be user generated and the limits for the  extent argument in plt.imshow must be user determined

def plotter_xy(frame_num):
    fig = plt.figure(figsize=(16,10))
    plt.xlim(-50,70)
    plt.ylim(-50,50)
    plt.scatter(0,0,s=200,label='Sun',color='black')
    plt.plot(xnRot,ynRot,label='Neptune orbit',color='red',alpha=0.5)
    plt.plot(xpRot,ypRot,label='Pluto orbit',color='blue',alpha=0.25)
    plt.scatter(xnRot[frame_num],ynRot[frame_num],label='Neptune',color='red',s=50)
    plt.scatter(xpRot[frame_num],ypRot[frame_num],label='Pluto',color='blue',s=100)
    # img = plt.imread('xy_plot_noframe.jpg')
    # plt.imshow(img,extent=[-55,50,-53,50])
    plt.minorticks_on()
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.tick_params(which='major',bottom='on',left='on',direction='in',length=10)
    plt.tick_params(which='minor',bottom='on',left='on',direction='in',length=5)
    plt.xlabel('x (AU)',fontsize=24)
    plt.ylabel('y (AU)',fontsize=24)
    plt.legend(fontsize=16,loc=1)
    return fig

def plotter_yz(frame_num):
    fig = plt.figure(figsize=(16,10))
    plt.xlim(-50,50)
    plt.ylim(-40,40)
    plt.scatter(0,0,s=1000,label='Sun',marker='o',facecolors='none',edgecolors='orange')
    plt.plot(ynRot,zn,label='Neptune orbit',color='red',alpha=0.5)
    plt.plot(ypRot,zp,label='Pluto orbit',color='blue',alpha=0.25)
    # img = plt.imread('yz_plot_background.jpg')
    # plt.imshow(img,extent=[-50,50,-40,40])
    plt.scatter(ynRot[frame_num],zn[frame_num],label='Neptune',color='red',s=50)
    plt.scatter(ypRot[frame_num],zp[frame_num],label='Pluto',color='blue',s=100)
    plt.minorticks_on()
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.tick_params(which='major',bottom='on',left='on',direction='in',length=10)
    plt.tick_params(which='minor',bottom='on',left='on',direction='in',length=5) 
    plt.xlabel('y (AU)',fontsize=24)
    plt.ylabel('z (AU)',fontsize=24)
    plt.legend(fontsize=16,loc=1)
    return fig

def plotter_xz(frame_num):
    fig = plt.figure(figsize=(16,10))
    plt.xlim(-50,50)
    plt.ylim(-40,40)
    plt.scatter(0,0,color='orange',s=500,label='Sun')
    plt.plot(xnRot,zn,label='Neptune orbit',color='red',alpha=0.5)
    plt.plot(xpRot,zp,label='Pluto orbit',color='blue',alpha=0.25)
    # img = plt.imread('xz_plot_background.jpg')
    # plt.imshow(img,extent=[-50,50,-40,40])
    plt.scatter(xnRot[frame_num],zn[frame_num],label='Neptune',color='red',s=50)
    plt.scatter(xpRot[frame_num],zp[frame_num],label='Pluto',color='blue',s=100)
    plt.minorticks_on()
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.tick_params(which='major',bottom='on',left='on',direction='in',length=10)
    plt.tick_params(which='minor',bottom='on',left='on',direction='in',length=5)
    plt.xlabel('x (AU)',fontsize=24)
    plt.ylabel('z (AU)',fontsize=24)
    plt.legend(fontsize=16,loc=1)
    return fig

def plotter_xyz(frame_num):
    fig = plt.figure(figsize=(18,15))
    ax = plt.axes(projection='3d')
    ax.set_zlim(-50,50)
    ax.set_xlim(-50,50)
    ax.set_ylim(-50,50)
    ax.scatter3D(0, 0, 0, c='orange',s=300,label='Sun') 
    ax.plot3D(data.xpRot,data.ypRot,data.zp,color='blue',label='Pluto',alpha=0.25)
    ax.plot3D(data.xnRot,data.ynRot,data.zn,color='red',label='Neptune',alpha=0.25)
    ax.scatter3D(xnRot[frame_num],ynRot[frame_num],zn[frame_num],label='Neptune',c='red',s=50)
    ax.scatter3D(xpRot[frame_num],ypRot[frame_num],zp[frame_num],label='Pluto',c='blue',s=100) 
    ax.view_init(15,-9)
    ax.set_xlabel('x (AU)',fontsize=24)
    ax.set_ylabel('y (AU)',fontsize=24)
    ax.set_zlabel('z (AU)',fontsize=24)
    plt.legend(fontsize=24,loc=1)
    return fig

N_frames = len(xp)

for i in range(N_frames):
    fig1 = plotter_xy(i) #change which function is called in this line depending on which animation you wish to make
    fig1.savefig('tmp_frames/_tmp%3i.jpg'%i,bbox_inches='tight',dpi=100)
    plt.close(fig1)

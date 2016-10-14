# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:50:24 2016

http://stackoverflow.com/questions/7819498/plotting-ellipsoid-with-matplotlib
created by minillinim
"""

import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

''' your ellipsoid and center in matrix form'''
#A = np.array([[80,30,0], [30,40,0], [0,0,60]])
A = np.array([[-5,5,-7], [5, -2, -9], [-7,-9,-5]])
eival,eivec = np.linalg.eig(A)
center = [0,0,0]

''' find the rotation matrix and radii of the axes'''
U, s, rotation = linalg.svd(A)
radii = 1.0/np.sqrt(s)
#print 'rotation',rotation
#print 'SSSSSSSSSSS', s
#print 'eigenvalues', eival
#print 'radii',radii
#print 'eigenvectors', eivec

''' now carry on with EOL's answer'''
u = np.linspace(0.0, 2.0 * np.pi, 100)
v = np.linspace(0.0, np.pi, 100)
'''radii[0]=eival[2]=z, radii[1]=eival[0]=x, radii[2]=eival[1]=z'''
x = radii[1] * np.outer(np.cos(u), np.sin(v))
y = radii[2] * np.outer(np.sin(u), np.sin(v))
z = radii[0] * np.outer(np.ones_like(u), np.cos(v))
for i in range(len(x)):
    for j in range(len(x)):
        #[x[i,j],y[i,j],z[i,j]] = np.dot([x[i,j],y[i,j],z[i,j]], rotation) + center
        [x[i,j],y[i,j],z[i,j]] = np.dot([x[i,j],y[i,j],z[i,j]], eivec) + center

''' plot'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z,  rstride=4, cstride=4, color='b', alpha=0.2)

ax.plot([center[0],eivec[0,0]/eival[0]],[center[1],eivec[0,1]/eival[0]],[center[2],eivec[0,2]/eival[0]], lw=3, color='y') # major
ax.plot([center[0],eivec[1,0]/eival[1]],[center[1],eivec[1,1]/eival[1]],[center[2],eivec[1,2]/eival[1]], lw=3, color='g') # major
ax.plot([center[0],eivec[2,0]/eival[2]],[center[1],eivec[2,1]/eival[2]],[center[2],eivec[2,2]/eival[2]], lw=3, color='r') # major
plt.show()
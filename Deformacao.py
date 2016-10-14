# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:09:21 2015

@author: paulo_000
"""
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy as np
from matplotlib import rcParams

rcParams['figure.figsize'] = 10, 8 #tamanho da figura
pi=np.pi
fi=30
x,y = np.mgrid[-5:5:10j, -5:5:10j]
origin_matrix = np.matrix([[-2, -2],
                           [2,-2],
                           [2,2],
                           [-2,2]])

#==============================================================================
# Rotação Antihorária
#==============================================================================
fig = plt.figure()#(facecolor='white') # Or any other color

fig.subplots_adjust(hspace=.3)# espaço entre subplots

ax = fig.add_subplot(231, xlim=(-6, 6), ylim=(-6, 6))#121
plt.grid()
ax.set_aspect('equal')

U = x*np.cos(fi*pi/180)-y*np.sin(fi*pi/180)
W = y*np.cos(fi*pi/180)+x*np.sin(fi*pi/180)

transform_matrix = np.matrix([[np.cos(fi*pi/180), -np.sin(fi*pi/180)], [np.sin(fi*pi/180), np.cos(fi*pi/180)]])
result_matrix = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix, color='red', alpha=0.4))
ax.set_title(u"Rotação Antihorária", size=16, weight='bold')
ax.set_xlabel(r'$\binom {cos \omega \/\ -sin \omega} {sin \omega \/\ cos \omega }$',size=24)

plt.quiver(x,y,U,W,color='DarkRed')

#==============================================================================
# Rotação Horária
#==============================================================================
ax = fig.add_subplot(232, xlim=(-6, 6), ylim=(-6, 6))#122
plt.grid()
ax.set_aspect('equal')

U = x*np.cos(fi*pi/180)+y*np.sin(fi*pi/180)
W = y*np.cos(fi*pi/180)-x*np.sin(fi*pi/180)

transform_matrix = np.matrix([[np.cos(fi*pi/180), np.sin(fi*pi/180)], [-np.sin(fi*pi/180), np.cos(fi*pi/180)]])
result_matrix = (transform_matrix * origin_matrix.transpose()).transpose()

ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix, color='blue', alpha=0.4))
ax.set_title(u"Rotação Horária", size=16, weight='bold')
ax.set_xlabel(r'$\binom {cos \omega \/\ sin \omega} {-sin \omega \/\ cos \omega }$',size=24)

plt.quiver(x,y,U,W,color='DarkRed');
#==============================================================================
# Cisalhamento Simples
#==============================================================================
ax = fig.add_subplot(233, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

L = x*1+y*np.tan(fi*pi/180)
V = y*1

transform_matrix = np.matrix([[1, np.tan(fi*pi/180)],[0, 1]])
result_matrix = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix, color='green', alpha=0.4))
ax.set_title(u"Cisalhamento Simples", size=16, weight='bold')
ax.set_xlabel(r'$\binom {1 \/\ \gamma} {0 \/\ 1 }$',size=24)

plt.quiver(x,y,y*np.tan(fi*pi/180),0,color='DarkRed')

#==============================================================================
# Cisalhamento Puro
#==============================================================================
ax = fig.add_subplot(234, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

R = x*1.5
S = -y*0.7

transform_matrix = np.matrix([[1.5, 0],[0, 0.7]])
result_matrix = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix, color='red', alpha=0.4))
ax.set_title(u"Cisalhamento Puro", size=16, weight='bold')
ax.set_xlabel(r'$\binom {1 \/\ 0} {0 \/\ 1 }$',size=24)

plt.quiver(x,y,R,S,color='DarkRed')

#==============================================================================
# Dilatação Simples
#==============================================================================
ax = fig.add_subplot(235, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

delta= 0.7

transform_matrix = np.matrix([[1 + delta, 0],[0, 1 + delta]])
result_matrix = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix, color='blue', alpha=0.4))
ax.set_title(u"Dilatação Simples", size=16, weight='bold')
ax.set_xlabel(r'$\binom {(1+\Delta) \/\ 0} {0 \/\ (1+\Delta) }$',size=24)

plt.quiver(x,y,x+delta,y+delta,color='DarkRed')

#==============================================================================
# Deformação Pura
#==============================================================================
ax = fig.add_subplot(236, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

M = x*0.9+y*1.1
N = x*1.1-y*0.7

transform_matrix = np.matrix([[0.9, 1.1],[1.1, 0.7]])
result_matrix = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix, color='green', alpha=0.4))
ax.set_title(u"Deformação Pura", size=16, weight='bold')
ax.set_xlabel(r'$\binom {(1+\epsilon{xx}) \/\ \epsilon{xy}} {\epsilon{xy} \/\ (1+\epsilon{xy}) }$',size=24)

plt.quiver(x,y,M,N,color='DarkRed')

plt.show();

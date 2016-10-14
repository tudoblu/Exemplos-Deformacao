# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:22:10 2015

@author: paulo_000
"""
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
import numpy as np
from matplotlib import rcParams

#rcParams['figure.figsize'] = 8, 10.5 #tamanho da figura
rcParams['figure.figsize'] = 13, 7 #tamanho da figura


pi=np.pi
fi=30
x,y = np.mgrid[-5:5:10j, -5:5:10j]
origin_matrix = np.matrix([[-2, -2],
                           [2,-2],
                           [2,2],
                           [-2,2]])
                           
#==============================================================================
# Cisalhamento Puro
#==============================================================================
fig = plt.figure()#(facecolor='white') # Or any other color
fig.subplots_adjust(hspace=.2)# espaço entre subplots

ax = fig.add_subplot(231, xlim=(-6, 6), ylim=(-6, 6))
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
# Cisalhamento Simples
#==============================================================================

ax = fig.add_subplot(232, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')


L = x*1+y*np.tan(fi*pi/180)
V = y*1

transform_matrix = np.matrix([[1, np.tan(fi*pi/180)],[0, 1]])
result_matrix1 = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix1, color='green', alpha=0.4))
ax.set_title(u"Cisalhamento Simples", size=16, weight='bold')
ax.set_xlabel(r'$\binom {1 \/\ \gamma} {0 \/\ 1 }$',size=24)

plt.quiver(x,y,y*np.tan(fi*pi/180),0,color='DarkRed')
#==============================================================================
# Cisalhamento Puro seguido por Cisalhamento Simples
#==============================================================================
from textwrap import wrap

plt.rcParams["axes.titlesize"] = 8
ax = fig.add_subplot(233, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

P = 1.5*(x*1+y*np.tan(fi*pi/180))
Q = -y*0.7

transform_matrix = np.matrix([[1.5, 0],[0, 0.7]])
result_matrix2 = (transform_matrix * result_matrix1.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix2, color='red', alpha=0.4))
title = ax.set_title("\n".join(wrap(u"Cisalhamento Puro seguido por Cisalhamento Simples",30)),size=16, weight='bold')
fig.tight_layout()
title.set_y(1.0)
ax.set_xlabel(r'$\binom {1 \/\ 0} {0 \/\ 1 } superposto\/por\/\binom {1 \/\ \gamma} {0 \/\ 1 }$',size=20)
#print result_matrix2
plt.quiver(x,y,P,Q,color='blue')
#==============================================================================
# Cisalhamento Simples 2
#==============================================================================
ax = fig.add_subplot(234, xlim=(-6, 6), ylim=(-6, 6))
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
# Cisalhamento Puro 2
#==============================================================================
ax = fig.add_subplot(235, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

R = x*1.5
S = -y*0.7

transform_matrix = np.matrix([[1.5, 0],[0, 0.7]])
result_matrix1 = (transform_matrix * origin_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix1, color='red', alpha=0.4))
ax.set_title(u"Cisalhamento Puro", size=16, weight='bold')
ax.set_xlabel(r'$\binom {1 \/\ 0} {0 \/\ 1 }$',size=24)

plt.quiver(x,y,R,S,color='DarkRed')
#==============================================================================
# Cisalhamento Simples seguido por Cisalhamento Puro 2
#==============================================================================
from textwrap import wrap

plt.rcParams["axes.titlesize"] = 8
ax = fig.add_subplot(236, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

P = 1.5*(x*1+y*np.tan(fi*pi/180))
Q = -y*0.7

transform_matrix = np.matrix([[1.5, 0],[0, 0.7]])
result_matrix4 = (transform_matrix * result_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix4, color='red', alpha=0.4))
title = ax.set_title("\n".join(wrap(u"Cisalhamento Simples seguido por Cisalhamento Puro",30)),size=16, weight='bold')
fig.tight_layout()
title.set_y(1.0)
ax.set_xlabel(r'$\binom {1 \/\ \gamma} {0 \/\ 1 } superposto\/por\/\binom {1 \/\ 0} {0 \/\ 1 }$',size=20)
#print result_matrix4
plt.quiver(x,y,P,Q,color='blue')

#==============================================================================
# Cisalhamento Simples seguido por Cisalhamento Puro 2
#==============================================================================
from textwrap import wrap

plt.rcParams["axes.titlesize"] = 8
ax = fig.add_subplot(236, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

P = 1.5*(x*1+y*np.tan(fi*pi/180))
Q = -y*0.7

transform_matrix = np.matrix([[1.5, 0],[0, 0.7]])
result_matrix2 = (transform_matrix * result_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix2, color='red', alpha=0.4))
title = ax.set_title("\n".join(wrap(u"Cisalhamento Simples seguido por Cisalhamento Puro",30)),size=16, weight='bold')
fig.tight_layout()
title.set_y(1.0)
ax.set_xlabel(r'$\binom {1 \/\ \gamma} {0 \/\ 1 } superposto\/por\/\binom {1 \/\ 0} {0 \/\ 1 }$',size=20)

plt.quiver(x,y,P,Q,color='blue')

#==============================================================================
# Cisalhamento Simples seguido por Cisalhamento Puro
#==============================================================================
from textwrap import wrap

plt.rcParams["axes.titlesize"] = 8
ax = fig.add_subplot(236, xlim=(-6, 6), ylim=(-6, 6))
plt.grid()
ax.set_aspect('equal')

P = 1.5*(x*1+y*np.tan(fi*pi/180))
Q = -y*0.7

transform_matrix = np.matrix([[1.5, 0],[0, 0.7]])
result_matrix2 = (transform_matrix * result_matrix.transpose()).transpose()
ax.clear()
ax.grid()
ax.add_patch(Polygon(origin_matrix, color='black'))
ax.add_patch(Polygon(result_matrix2, color='red', alpha=0.4))
title = ax.set_title("\n".join(wrap(u"Cisalhamento Simples seguido por Cisalhamento Puro",30)),size=16, weight='bold')
fig.tight_layout()
title.set_y(1.0)
ax.set_xlabel(r'$\binom {1 \/\ \gamma} {0 \/\ 1 } superposto\/por\/\binom {1 \/\ 0} {0 \/\ 1 }$',size=20)

plt.quiver(x,y,P,Q,color='blue')
plt.show()
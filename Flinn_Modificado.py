# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 14:12:09 2015

@author: ctq1
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:16:45 2015

@author: paulo_000
"""
from matplotlib import pyplot as plt
from numpy import *
import numpy as np
from matplotlib import rcParams

x = [1, np.e, np.e**2, np.e**3, np.e**4, np.e**5, np.e**6, np.e**7, np.e**8]
y = [1, np.e, np.e**2, np.e**3, np.e**4, np.e**5, np.e**6, np.e**7, np.e**8]

#==============================================================================
# '''Construção do gráfico'''
#==============================================================================
rcParams['figure.figsize'] = 9, 9#tamanho da figura
ax = plt.gca()#get current axis

plt.xlim(0,8)
plt.ylim(0,8)


y5 = plt.plot(np.log(x),5*np.log(y),'r--')
plt.text(1.1,7, '$k = 5$', rotation = 79, color = 'red')
y2 = plt.plot(np.log(x),2*np.log(y),'g--')
plt.text(3.1,7, '$k = 2$', rotation = 63, color = 'green')
xy = plt.plot(np.log(x),np.log(y),'b--')
plt.text(6.6,7.1, '$k = 1$', rotation = 45, color = 'blue')
plt.text(4,6, u'$Transição\  guirlanda / cluster$', rotation = 45, color = 'blue')
x2 = plt.plot(2*np.log(x),np.log(y),'g--')
plt.text(7,3.9, '$k = 0.5$', rotation = 26, color = 'green')
x4 = plt.plot(np.log(x),np.log(y)/5,'r--')
plt.text(7,1.6, '$k = 0.2$', rotation = 11, color = 'red')
plt.fill_between([0,8],[0,8],facecolor='darkkhaki', alpha=0.3)

#==============================================================================
# '''ln S1/S3'''
#==============================================================================
xy6 = plt.plot(np.log(x),6-np.log(x),'#800000',linewidth=0.2)
plt.text(1,5, r'$ln \frac{S_1}{S_3} = 6$', rotation = 315, color = 'maroon')
xy4 = plt.plot(np.log(x),4-np.log(x),'#800000',linewidth=0.2)
plt.text(1,3, r'$ln \frac{S_1}{S_3} = 4$', rotation = 315, color = 'maroon')
xy2 = plt.plot(np.log(x),2-np.log(x),'#800000',linewidth=0.2)
plt.text(1,1, r'$ln \frac{S_1}{S_3} = 2$', rotation = 315, color = 'maroon')

ax.set_aspect('equal')

#==============================================================================
# '''Textos no gráfico'''
#==============================================================================
ax.set_title("$Eigenvalues$", size=20, weight='bold')
ax.set_xlabel(r'$ln \frac{S_2}{S_3}$', size=18)
ax.set_ylabel(r'$ln \frac{S_1}{S_2}$', size=18)
plt.text(0.05,7, r'$Clusteres\ uniaxiais$', size=14, rotation = 90, color = '0.2')
plt.text(5,0.1, r'$Guirlandas\ uniaxiais$', size=14, rotation = 0, color = '0.2')

ax.grid(True)
plt.show();  
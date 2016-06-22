import matplotlib.pyplot as plt
import numpy as np

#"Mcr %  (frame) crossTypeMcr %
l1 = [ 94.21, 94.29 ]
l2 = [ 97.86, 97.86 ]
l3 = [ 83.24, 92.52 ]
l4 = [ 96.06, 98.35 ]

numLit = 4+1
numLitx = numLit - 0
index = np.arange(1,numLitx,1)

y = '['
for i in range(1,numLit):
    _y = 'l%d,'%i
    y = y+_y
y = y[:-1]+"]"
exec("y = %s"%y)
print len(y)
'''
'''

y0 = [ele[0] for ele in y]
y1 = [ele[1] for ele in y]

plt.figure(figsize=(8,8))
bar_width = 0.4
opacity = 0.3

rects1 = plt.bar(index, y0, bar_width,
                 alpha=opacity,
                 color='b',
                 label='ADL-level')

rects2 = plt.bar(index+bar_width, y1, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Location-level')

xlabel = [
'BayesNet+\n Bedroom',
'J48+\n Bedroom',
'BayesNet+\n Livingroom',
'J48+\n Livingroom',
]

def numbering(elelist):
    reList = []
    for a,ele in enumerate(elelist):
        __etmp = '(%s). %s'%(chr(a+96+1),ele)
        reList.append(__etmp)
    return reList

xlabel = numbering (xlabel)

def autolabel(rects,offset,hioff):
    i = 1
    for rect in rects:
        plt.text(i+bar_width/3*offset, hioff, '%0.2f'% float(rect),
               rotation=90,fontsize=24)
        i += 1

autolabel(y0,1,28)
autolabel(y1,4,54)

#plt.xlabel(' ')
plt.ylabel('Recognition rate (%)', fontsize = 24)
plt.xticks(index, xlabel, rotation = 60, fontsize=20)
#plt.set_xticklabels(xlabel)
plt.ylim(0, 120)
plt.xlim(1,numLitx,1)
#plt.title('line_regression & gradient decrease')
plt.legend(loc='best', fontsize = 20)
plt.tight_layout()
plt.show()

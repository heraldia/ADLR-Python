from pychart import *
import sys

'''
data = [("foo", 10),("bar", 20), ("baz", 30), ("ao", 40)]

ar = area.T(size=(150,150), legend=legend.T(),
            x_grid_style = None, y_grid_style = None)

plot = pie_plot.T(data=data, arc_offsets=[0,10,0,10],
                  shadow = (20, -2, fill_style.gray50),
                  label_offset = 25,
                  arrow_style = arrow.a3)
ar.add_plot(plot)
ar.draw()
'''


def plo(filename):
    f1 = file(filename,'r')
    angle = set()
    for line in f1.readlines():
        sStr = line.split('\t')
        stri = sStr[2].strip()
        angle.add(stri)
        #l=list(angle)
        #l.sort()
    print angle
#    angleDict = dict()

def plo1(filename):
    f1 = file(filename,'r')
    for line in f1.readlines():
        sStr = line.split('\t')
        striA = sStr[0].strip()
        striF = sStr[1].strip()
        print striA, striF




if __name__=="__main__":
    filename = "Cooking_angle.dat"
    plo1(filename)



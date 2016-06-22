import numpy as np
import pylab as pl

def getLightDistribution():
    filename = 'predictOutputBedroom.arff'
    lightNight = []
    lightDay = []
    for ele in open(filename):
        if 'WorkingonPCathome' in ele and '%' in ele:
            eleList = ele.split(',')
            _hour = int(eleList[2])
            _light = float(eleList[0])
            if _hour >= 17 or _hour <=7:
                lightNight.append(_light)
            else : lightDay.append(_light)
    print lightNight
    print lightDay
    return lightNight, lightDay


lightNight, lightDay = getLightDistribution()


lightDayNP = np.array(lightDay)
pl.hist(lightDayNP)

lightNightNP = np.array(lightNight)
pl.hist(lightNightNP)

#pl.legend([lightDayNP, lightNightNP], ('lightDay, lightNight'), 'best', numpoints=1)
#pl.legend()

pl.xlabel('Light value')
pl.ylabel('Frequency')
pl.show()

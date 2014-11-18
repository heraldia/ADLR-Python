import os

def copyBunch():
    os.system('del *.txt')
    os.system('del *.dat')
    os.system('copy g:\\class\\Semester5\\research\\ADLRecorder\\code\\python\\SoundActivityAnalysis\\activityPrediction.txt soundPrediction.dat')
    #os.system('copy g:\\class\\Semester5\\research\\ADLRecorder\\code\\python\\WifiTableDB\\wifiFingerPrinting1.txt wifiPrediction.dat')
    os.system('copy g:\\class\\Semester5\\research\\ADLRecorder\\code\\python\\Orientation\\Report_distri.dat orientationPrediction.dat')
    os.system('copy g:\\class\\Semester5\\research\\ADLRecorder\\code\\python\\WifiTableDB\\test.dat wifiPrediction.dat')

def selectP():
    os.system('python soundDb.py > soundDbTest.dat')
    os.system('python wifiDb.py > wifiDbTest.dat')
    os.system('python delWifiOutdoor.py')
    #os.system('del wifiDbTest.dat')




if __name__=="__main__":
    copyBunch()
    selectP()
    from predictionAsAWhole import predictionAsAWhole
    predictionAsAWhole()


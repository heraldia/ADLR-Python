'''
refer :
e d:/class/Semester5/research/audioProcessing/code/mfccMsvn/test4.py

2015-10-3 11:36:05
'''
import pylab as pl
from matplotlib.colors import LogNorm
from matplotlib.backends.backend_pdf import PdfPages
import os

global pp

def plotPWrapper(args, dirname, filenames): #{{{2
    for filename in filenames:
        plotP(dirname +'\\'+filename)

def plotP(filePath): #{{{3
    fp = open(filePath,'r+')
    yList = []
    e = fp.readline();
    el = e.split(',')
    yList = map(float,el[3:-1])
    fp.close()

    (dirx,filenameM) = os.path.split(filePath)

    dirname = os.path.dirname(filePath)
    m_type = str(dirname.split('\\')[-1])

    (filenameM, x) = os.path.splitext(filenameM)
    __plotDotsP(yList, filenameM,m_type)

def __plotDotsP(yAxis, filenameM,m_type): #{{{4

    global pp
    #filenameM = 'a'
    fig = pl.figure()
    pl.plot(yAxis)# use pylab to plot x and y
    #pl.scatter( yAxis)# use pylab to plot x and y
    #pl.plot( yAxis, 'k--', drawstyle='steps-post', label='steps-post')
    pl.title(filenameM+'_'+ 'First coefficients')
    pl.xlabel('Frames' + '  ' + m_type)
    #pl.show()# show the plot on the screen
    fig.savefig(pp, format='pdf')


def plot_main(filePath): #{{{1
    '''
    run this after
    d:/class/Semester5/research/audioProcessing/code/mfccMsvn/python_speech_features/example.py
    plot first coefficients mfcc into a pdf file
    '''
    dirname = os.path.dirname(filePath)
    #print dirname.split('\\')
    m_type = str(dirname.split('\\')[-1])
    global pp
    pp = PdfPages(m_type+'.pdf')
    os.path.walk(dirname, plotPWrapper,None)

    #plotP(filePath)
    pp.close()

if __name__ == '__main__':
    strx='None'
    #filePath = 'd:\class\Semester5\\research\ADLRecorder\code\python\SDL\\files\Bus\Bus_%s_mfcc\\'%strx
    #filePath = 'd:\class\Semester5\\research\\audioProcessing\code\gmmHmm\hmm-speech-recognition-0.1\\audio\cutting\_mfcc\\'
    filePath =  'files/Bathroom/Bathroom_cooking2_mfcc/'
    filePath = filePath.lstrip()
    #'./_mfcc\\'
    plot_main(filePath)

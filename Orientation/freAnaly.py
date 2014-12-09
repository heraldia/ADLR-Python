import os
#import numpy as np

#_DEBUG = True
_DEBUG = False

class FreAnaly:
    def analyAngle(self, filename):
        myfile=open(filename)
        fOut = file(filename[:-4]+'_angle.dat','w')
        Dic={}
        try:
         for line in myfile:
          linein=line.split('\t')
          key=linein[2]
          if _DEBUG == True:
              print key
              print "-" * 30
          if Dic.has_key(key) :
              Dic[key] +=1
          else:
              Dic[key] = 1

        finally:
            myfile.close()
        keyall=Dic.keys()
        keyall.sort()
        #np.sort(keyall)
        for keyin in keyall:
            print keyin,"\t",Dic[keyin]
            fOut.write(str(keyin) + "\t "+ str(Dic[keyin])+'\n')

        fOut.close()

    def analyAngle(self, filename, option=0 ):
        myfile=open(filename)
        if option == 1 :
            fOut = file(filename[:-4]+'_angle_analy.dat','w')
        else :
            fOut = file(filename[:-4]+'_angle.dat','w')
        Dic={}
        try:
         for line in myfile:
          linein=line.split('\t')
          key=linein[2]
          if _DEBUG == True:
              print key
              print "-" * 30
          if Dic.has_key(key) :
              Dic[key] +=1
          else:
              Dic[key] = 1

        finally:
            myfile.close()
        keyall=Dic.keys()
        keyall.sort()
        #np.sort(keyall)
        for keyin in keyall:
            #print keyin,"\t",Dic[keyin]
            if option == 1 :
                fOut.write(str(keyin) + "\t "+ str(Dic[keyin])+'\n')
            else:
                fOut.write(str(keyin) + '\n')
        fOut.close()

    def generaAllFileAngle(self):
        os.system('del *_angle*.dat')
        import glob
        for filename in glob.glob(r'./*.dat'):
            if "Report_distri" in filename:
                continue
            self.analyAngle(filename)
            self.analyAngle(filename,1)

if __name__=="__main__":
    freAnaly = FreAnaly()
    freAnaly.generaAllFileAngle()

# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3
import glob
#import os.path


_DEBUG = True
#_DEBUG = False
"""
if _DEBUG == True:
    import pdb
    pdb.set_trace()
"""

def count():
    totalCount()
    totalUsedRecord()


def totalUsedRecord():
    return 0


def totalCount():
    totalRecordCount = 0
    for dbFilename in\
    glob.glob(r'd:/class/Semester5/research/ADLRecorder/code/Android/DbRecords/db/*.db'):
    #glob.glob(r'c:\Users\Phil\workspace\wifiFingerprinting\db\db\wifiFingerPrinting*.db'):
    #glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/o/nexussensors*.db'):
        #print dbFilename
        if _DEBUG == True:
             print dbFilename.split('/')[-1]
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql0 = "select time from sensorspackage where id = 1 "
        sql1 = "select time from sensorspackage where id = (select max(id) from sensorspackage) "
        sql2 = "select max(id) from sensorspackage"
        cu.execute(sql0)
        res0 = cu.fetchone()
        cu.execute(sql1)
        res1 = cu.fetchone()
        cu.execute(sql2)
        res2 = cu.fetchone()
        print res0[0],';',res1[0],';',res2[0]

        '''
        for line in res2:
            for f in line:
                if _DEBUG == True:
                    print "Records totally %d"%f
                totalRecordCount += f
                '''
        totalRecordCount += res2[0]

    print "Total number of records is %d ."%totalRecordCount

def processDirectory ( args, dirname, filenames ):
    print 'Directory',dirname
    for filename in filenames:
        print ' File',filename

if __name__=="__main__":
    print "database info:"
    count()
    #os.path.walk(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/', processDirectory, None )
    #d:\class\Semester5\research\ADLRecorder\code\Android\DbRecords\

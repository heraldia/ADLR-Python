# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3
import glob
import os.path


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
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
    #glob.glob(r'c:\Users\Phil\workspace\wifiFingerprinting\db\db\wifiFingerPrinting*.db'):
    #glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/o/nexussensors*.db'):
        if _DEBUG == True:
            print dbFilename
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql2 = "select max(id) from sensorspackage"
        #sql2 = "select max(id) from wifirssi"
        cu.execute(sql2)
        res = cu.fetchall()
        for line in res:
            for f in line:
                if _DEBUG == True:
                    print f
                totalRecordCount += f

    print "Total number of records is %d ."%totalRecordCount

def processDirectory ( args, dirname, filenames ):
    print 'Directory',dirname
    for filename in filenames:
        print ' File',filename

if __name__=="__main__":
    count()
    #os.path.walk(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/', processDirectory, None )

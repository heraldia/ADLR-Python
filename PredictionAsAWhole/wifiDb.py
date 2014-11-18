# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3
import glob

DBCOUNT = 19

_DEBUG = True
"""
if _DEBUG == True:
    import pdb
    pdb.set_trace()
"""
def select(sequenceNum):

    #print "-"*60
    db1_1 = "c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors"
    db1_2 = "%s"%sequenceNum
    db1_3 = ".db"
    dbFilename = db1_1 + db1_2 + db1_3
    #print "-"*60
    #print dbFilename
    conn = sqlite3.connect(dbFilename)
    conn.isolation_level = None
    cu = conn.cursor()
    sql2 = "select * from wifirssi"
    sql1_1 = "select "
    sql1_2_1 = "activity,"
    sql1_2_2 = "action,"
    sql1_3 = "ORION140, NETGEAR54, Cheese\
        HPPrint45, Judhajeet, NETGEAR17, DespicableLadies,\
        Baking, unit204 \
        ,time from wifirssi"

    if sequenceNum <= 13:
        sql1_2 = sql1_2_1
    else:
        sql1_2 = sql1_2_2

    sql1 = sql1_1+sql1_2+sql1_3
    cu.execute(sql1)
    res = cu.fetchall()
    for line in res:
        for f in line:
            print f,
            print '\t',
        print
        #print '-'*60

def iterator():
    for sequenceNum in range(9,DBCOUNT):
        if sequenceNum == 10 or sequenceNum ==11 or sequenceNum == 12 \
           or sequenceNum == 15 :
               continue
        #if i != 10:
        select(sequenceNum)


if __name__=="__main__":
    #select(9)
    iterator()

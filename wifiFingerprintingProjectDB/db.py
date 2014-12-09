# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3
import glob

_DEBUG = False

def select():
    """
if _DEBUG == True:
    import pdb
    pdb.set_trace()
    """
for dbFilename in glob.glob(r'c:/Users/Phil/workspace/wifiFingerprinting/db/db/*.db'):
    conn = sqlite3.connect(dbFilename)
    conn.isolation_level = None
    cu = conn.cursor()
    sql2 = "select * from wifirssi"
    sql1 = "select location, ORION140,NETGEAR54,Cheese\
            HPPrint45, Judhajeet, NETGEAR17,DespicableLadies,\
            Baking, unit204 \
            from wifirssi"
    cu.execute(sql1)
    res = cu.fetchall()
    for line in res:
        for f in line:
            print f,
        print
    #print '-'*60


if __name__=="__main__":
    #print("main")
    select()

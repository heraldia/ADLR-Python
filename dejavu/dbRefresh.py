import time, MySQLdb


def dbRefresh(option):
    conn=MySQLdb.connect(host="localhost",user="root",passwd="virtual",db="dejavu",charset="utf8")

    cursor = conn.cursor()

    if option == 0:
        sql = "drop table songs"
        n = cursor.execute(sql)
        print n
    if option == 1:
        sql = "drop table fingerprints"
        n = cursor.execute(sql)
        print n

    cursor.close()
    conn.close()

def dbInfor(option=0):
    conn=MySQLdb.connect(host="localhost",user="root",passwd="virtual",db="dejavu",charset="utf8")

    cursor = conn.cursor()

    sql = "select * from songs"
    cursor.execute(sql)

    res = cursor.fetchall()
    # print 'row:', cu.rowcount
    for line in res:
        for f in line:
            print f,
        print
    #print '-'*60
    cursor.close()
    conn.close()

def dbRefreshWrapper():
    dbRefresh(1)
    dbRefresh(0)

if __name__=="__main__":
    dbRefresh(1)
    #dbInfor()
    #dbRefreshWrapper()

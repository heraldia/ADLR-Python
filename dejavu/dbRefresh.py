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


if __name__=="__main__":
    dbRefresh(0)
    dbRefresh(1)

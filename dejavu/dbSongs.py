import MySQLdb as mysql

_DEBUG = True
"""
if _DEBUG == True:
    import pdb
    pdb.set_trace()
"""
try:
    conn=mysql.connect(host='localhost',user='root',passwd='virtual',db='dejavu',port=3306)
    cur=conn.cursor()
    cur.execute('select * from songs')
    res = cur.fetchall()
    for line in res:
        for f in line:
            print f,
        print
        #print '-'*60
    cur.close()
    conn.close()
except mysql.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

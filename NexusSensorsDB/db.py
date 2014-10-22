# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3

DBCOUNT = 16

def select(sequenceNum, action='NULL'):
    # sequenceNum = 8
    db1_1 = "c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors"
    db1_2 = "%s" % sequenceNum
    db1_3 = ".db"
    db1 = db1_1 + db1_2 + db1_3
    conn = sqlite3.connect(db1)
    conn.isolation_level = None
    cu = conn.cursor()
    #cu.execute("select * from sensorspackage where id < 10")

    sqla = "select * from sensorspackage"
    sql1_1 = "select "
    sql1_2_1 = "*"
    sql1_2_2 = "id,mLight,mOrientationSensor,mOrientation,mStepCounter,\
            mBooleanStepDetecorm,"
    sql1_2_2_1 = "activity"
    sql1_2_2_2 = "action"
    sql1_2_3 = ",soundFile,time "

    if sequenceNum <= 13:
        sql1_2_2_f = sql1_2_2_1
    else:
        sql1_2_2_f = sql1_2_2_2

    sql1_2 = sql1_2_2 + sql1_2_2_f + sql1_2_3
    sql1_3 = "from sensorspackage"
    sql1 = sql1_1 + sql1_2_1 + sql1_3

    #sql2 = " where action like '%s'" % action
    #sql2 = " where action like \"%s\"" % action

    if sequenceNum <= 13:
        sql2 = " where activity like '%s'" % action
    else:
        sql2 = " where action like '%s'" % action

    if action == 'NULL':
        sqlF = sql1
    else:
        sqlF = sql1 + sql2


    cu.execute(sqlF)
    res = cu.fetchall()
    # print 'row:', cu.rowcount
    for line in res:
        for f in line:
            print f,
        print
    #print '-'*60

def indoorAction():
    action1 = 'Working on PC at home'
    action2 = 'Working on PC'
    action3 = 'Working %'
    action4 = 'Walking at home'
    action5 = 'Bathroom'
    action6 = 'Washing %'
    action7 = 'Cooking'
    action8 = 'Breakfast'
    action9 = 'Lunch'
    action10 = 'Dinner'
    action11 = 'Midnight snack'
    action12 = 'Eating'

    #action1 = 'Working'
    #action5 = ' '
    for actionNum in range(1,13):
        actionS = 'action%s'%actionNum
        action = locals()[actionS]
        print '%s'%action+'-----------'
        for sequenceNum in range(1, DBCOUNT+1):
            print '-----------%s'%sequenceNum+'-----------'
            select(sequenceNum, action)

#def deleteGPSinfo():

def allAction():
    for sequenceNum in range(1, DBCOUNT+1):
        print '-----------%s'%sequenceNum+'-----------'
        select(sequenceNum)

if __name__=="__main__":
    #print("main")
    #sequenceNum = 1
    #indoorAction()
    allAction()

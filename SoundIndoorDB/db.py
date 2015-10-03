# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3
import glob
from delDuplicates import *

DBCOUNT = 18

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

    #sqla = "select * from sensorspackage"
    sql1_1 = "select "
    #sql1_2_1 = "*"
    sql1_2_1 = "id, "
    sql1_2_1 = " "
    sql1_2_2_1 = "activity "
    sql1_2_2_2 = "action "
    sql1_2_3 = "soundFile, "
    #sql1_2_3 = ",soundFile,time "

    if sequenceNum <= 13:
        sql1_2_2_f = sql1_2_2_1
    else:
        sql1_2_2_f = sql1_2_2_2

    sql1_2 = sql1_2_1 + sql1_2_3 + sql1_2_2_f
    #sql1_2 = sql1_2_1 + sql1_2_2_f + sql1_2_3
    sql1_3 = "from sensorspackage"
    sql1 = sql1_1 + sql1_2 + sql1_3

    #sql2 = " where action like '%s'" % action
    #sql2 = " where action like \"%s\"" % action

    if sequenceNum <= 13:
        sql2 = " where activity like '%s'" % action
    else:
        sql2 = " where action like '%s'" % action

    sql3 = ' AND soundFile !=""'

    if action == 'NULL':
        sqlF = sql1 + sql3
    else:
        sqlF = sql1 + sql2 + sql3


    cu.execute(sqlF)
    #print sqlF
    res = cu.fetchall()
    # print 'row:', cu.rowcount
    for line in res:
        for f in line:
            print f,
        print
    #print '-'*60

def indoorActionSound(actionList):

    actionList = [\
    #'Working on PC at home', 'Walking at home',\
    'Bathroom',\
    'Washing in bathroom',\
    'Washing dishes',\
    'Cooking',\
    'Chopping',\
    'Breakfast',\
    'Lunch',\
    'Dinner',\
    'Midnight snack',\
   'Eating','Music'\

    ] #,'Bus','Walking outside','Waiting for a bus']

    for action in actionList:
        #print ' -----------------%s-----------------'%action
        for sequenceNum in range(10, DBCOUNT+1):
            if sequenceNum == 8 or sequenceNum ==11 or sequenceNum == 12 \
               or sequenceNum == 15 :
                   continue
            # print '-----------%s'%sequenceNum+'-----------'
            select(sequenceNum, action)


#2015-09-27 14:59:19
def eventsSound(actionList):

    for action in actionList:
        #print ' -----------------%s-----------------'%action
        '''
        for sequenceNum in range(10, DBCOUNT+1):
            if sequenceNum == 8 or sequenceNum ==11 or sequenceNum == 12 \
               or sequenceNum == 15 :
                   continue
            # print '-----------%s'%sequenceNum+'-----------'
            '''
        select(action)


#2015-9-27 17:25:18
def select(action):
    m_filename = action+".dat"
    fp = open(m_filename,'w+')
    for dbFilename in\
    glob.glob(r'd:/class/Semester5/research/ADLRecorder/code/Android/DbRecords/db/*.db'):
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        tempDbFilename = dbFilename.split('/')[-1][3:]
        print tempDbFilename

        #print tempDbFilename[-4]
        if tempDbFilename[0]=='n' and (tempDbFilename[-4]=='3' or\
            tempDbFilename[-4]=='0' or\
            tempDbFilename[-4]=='9' or \
            (tempDbFilename[-4]=='7' and \
            tempDbFilename[-5]!='1')  ):
            #sqlF = "select id, activity, soundFile, time from sensorspackage where activity= '%s'"%action
            sqlF = "select soundFile, activity from sensorspackage where activity= '%s'"%action
        else: #tempDbFilename[0]=='a':
            #sqlF = "select id, action, soundFile, time from sensorspackage where action= '%s'"%action
            sqlF = "select soundFile, action from sensorspackage where action= '%s'"%action

        #print sqlF
        cu.execute(sqlF)
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        if res is not None:
            for line in res:
                if (line[0] is not None) and line[0] !="":
                    for f in line:
                        if f is not None:
                            print f,';',
                            fp.write(f+';')
                    fp.write('\n')
                    print
    fp.close()

#2015-09-27 15:05:24
def selectx(action):
    for dbFilename in\
    glob.glob(r'd:/class/Semester5/research/ADLRecorder/code/Android/DbRecords/db/*.db'):
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        tempDbFilename = dbFilename.split('/')[-1][3:]
        print tempDbFilename

        #print tempDbFilename[-4]
        if tempDbFilename[0]=='n' and (tempDbFilename[-4]=='3' or\
            tempDbFilename[-4]=='0' or\
            tempDbFilename[-4]=='9' or \
            (tempDbFilename[-4]=='7' and \
            tempDbFilename[-5]!='1')  ):
            #sqlF = "select id, activity, soundFile, time from sensorspackage where activity= '%s'"%action
            sqlF = "select soundFile, activity from sensorspackage where activity= '%s'"%action
        else: #tempDbFilename[0]=='a':
            #sqlF = "select id, action, soundFile, time from sensorspackage where action= '%s'"%action
            sqlF = "select soundFile, action from sensorspackage where action= '%s'"%action

        #print sqlF
        cu.execute(sqlF)
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        for line in res:
            for f in line:
                print f,';',
            print
        print '-'*60

def allAction():
    for sequenceNum in range(1, DBCOUNT+1):
        if sequenceNum == 8 or sequenceNum ==11 or sequenceNum == 12 \
           or sequenceNum == 15 :
               continue
        print '-----------%s'%sequenceNum+'-----------'
        select(sequenceNum)

if __name__=="__main__":
    #print("main")
    #sequenceNum = 1
    #indoorActionSound()
    #singleAction()

    actionList = [\
    #'Working on PC at home', 'Walking at home',\
    'Washing in bathroom',\
    'Washing dishes',\
    'Bathroom',\
    'Cooking',\
    'Bus',\
    'Driving',\
    'Walking outside',\
    'Waiting for a bus']

    eventsSound(actionList)
    delDuplicates(actionList)
    import os
    os.system('del *.dat')
    countP(actionList)

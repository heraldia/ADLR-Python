# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3
import glob
import os
import re


#_DEBUG = True
_DEBUG = False
"""
if _DEBUG == True:
    import pdb
    pdb.set_trace()
"""

def count():
    totalUsedRecord()


def totalUsedRecord():
    return 0

patt = re.compile(r'^[2014-]', re.I|re.U|re.X)

def selectP(action):
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
        sequenceNum = filter(str.isdigit, dbFilename)
        if int(sequenceNum) == 9 :
            continue
        if _DEBUG == True:
            print ':' + sequenceNum + "-" * 20
            print dbFilename
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql2_select = "select  "
        sql2_attributes = ", mOrientation , mOrientationSensor "
        sql2_attribuActivity = "activity"
        sql2_attribuAction = "action"
        sql2_time = ", time "
        sql2_soundFile = ", soundFile "
        sql2_from = " from sensorspackage"
        sql2_like1 = " where activity like '%s'" % action
        sql2_like2 = " where action like '%s'" % action

        if int(sequenceNum) <= 13:
            sqlF = sql2_select + sql2_attribuActivity + sql2_attributes + \
            sql2_soundFile + sql2_time + sql2_from + sql2_like1
        else:
            sqlF = sql2_select + sql2_attribuAction + sql2_attributes + \
                sql2_soundFile + sql2_time + sql2_from + sql2_like2

        #sqlF = "select * from sensorspackage"

        cu.execute(sqlF)
        res = cu.fetchall()
        #if cu.rowcount > 0:
        #print cu.rowcount
        for line in res:
            for f in line:
                '''
                #if _DEBUG == True:
                fStr = f.encode('utf-8')
                if patt.match(fStr):
                    sStr = fStr.split(' ')
                    print sStr[1],
                else:
                    print f,
                #type(f),
                '''
                print f,
                print '\t',
            print
            #print line

        #print "-"*30


def selectPP(activities):
    for activity in activities :
        selectP(activity)

if __name__=="__main__":
    indoorActivitySet = set(['Bathroom','Cooking','Chopping', \
        'Washing in bathroom',\
        'Dinner','Breakfast','Midnight snack','Eating',\
                'Lunch',\
        #'Working on PC at home',
                'Washing dishes'])
    selectPP(indoorActivitySet)

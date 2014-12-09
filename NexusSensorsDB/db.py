# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3

DBCOUNT = 19

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
            mBooleanStepDetecor,"
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

''' defunct
def indoorAction():
    action2 = 'Working on PC at home'
    #action2 = 'Working on PC'
    #action3 = 'Working %'
    action3 = 'Walking at home'
    action4 = 'Bathroom'
    action5 = 'Washing'
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
        if actionNum <2:
            continue
        actionS = 'action%s'%actionNum
        action = locals()[actionS]
        print '%s'%action+'-----------'
        for sequenceNum in range(1, DBCOUNT+1):
            if sequenceNum == 8 or sequenceNum ==11 or sequenceNum == 12 \
               or sequenceNum == 15 :
                   continue
            print '-----------%s'%sequenceNum+'-----------'
            select(sequenceNum, action)
'''

''' defunct
def singleAction1():
    #action5 = 'Washing'
    #action6 = 'Washing %'
    #action6 = 'NULL'
    action6 = '%*%'

    for actionNum in range(6,7):
        actionS = 'action%s'%actionNum
        action = locals()[actionS]
        print '%s'%action+'-----------'
        for sequenceNum in range(1, DBCOUNT+1):
            if sequenceNum == 8 or sequenceNum ==11 or sequenceNum == 12 \
               or sequenceNum == 15:
                   continue
            print '-----------%s'%sequenceNum+'-----------'
            select(sequenceNum, action)
'''

''' defunct
def allAction1():
    for sequenceNum in range(1, DBCOUNT+1):
        if sequenceNum == 8 or sequenceNum ==11 or sequenceNum == 12 \
           or sequenceNum == 15 :
               continue
        print '-----------%s'%sequenceNum+'-----------'
        select(sequenceNum)
'''

def allAction():
    import glob
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
        dbSeqenceNum = filter(str.isdigit,dbFilename)
        print dbSeqenceNum + "-"*20
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        cu.execute("select * from sensorspackage")
        #cu.execute(sqlF)
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        for line in res:
            for f in line:
                print f,
            print
        #print '-'*60

        pass

def sqlAct(dbSeqenceNum):
    if dbSeqenceNum <= 13:
        sql_act  = 'activity '
    else:
        sql_act = 'action '
    return sql_act

def singleActionO(targActi,option = 0):
    if option ==2:
        singleAction(targActi,0)
        print "="*10 + 'O'*3 + "="*10
        singleAction(targActi,1)
    else:
        singleAction(targActi,option)


def singleAction(targActi,option = 0):
    import glob
    if option == 0:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'
    else:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/o/nexussensors*.db'
    for dbFilename in\
    glob.glob(dire):
        dbSeqenceNum = filter(str.isdigit,dbFilename)
        print dbSeqenceNum + "-"*20
        dbSeqenceNum = int(dbSeqenceNum)
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()

        sql_sel = "select * from sensorspackage "
        #print targActi
        if 'Walk' in targActi:
            sql_sel = "select id, mStepCounter, mBooleanStepDetecor from sensorspackage "
            #print "173"
        sql_where = 'where '

        sql_act = sqlAct(dbSeqenceNum)

        sql_condition = sql_act + "like '%%%s%%'"%targActi
        sql_condition = sql_condition + " and mBooleanStepDetecor = '0.0' "
        #sql_condition = sql_act + "like '%s'"%targActi
        sqlF = sql_sel+sql_where+sql_condition
        cu.execute(sqlF)
        #print sqlF
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        for line in res:
            for f in line:
                print f,
            print
        #print '-'*60

        pass


def multipleActions(targActiList,option = 0):
    import glob
    if option == 0:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'
    else:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/o/nexussensors*.db'
    for dbFilename in\
    glob.glob(dire):
        dbSeqenceNum = filter(str.isdigit,dbFilename)
        print dbSeqenceNum + "-"*20
        dbSeqenceNum = int(dbSeqenceNum)
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()

        sql_sel = "select * from sensorspackage "
        sql_where = 'where '

        sql_act = sqlAct(dbSeqenceNum)

        sql_condition = ""

        for targActi in targActiList :
            #sql_condition = sql_act + "like '%%%s%%'"%targActi
            sql_subcondition = ' or ' + sql_act+ "like '%%%s%%'"%targActi
            sql_condition = sql_condition + sql_subcondition

        sql_condition = sql_condition[4:]
        sqlF = sql_sel+sql_where+sql_condition
        cu.execute(sqlF)
        #print sqlF
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        for line in res:
            for f in line:
                print f,
            print
        #print '-'*60

        pass


def conditionalSelectO(conditionAttribute,attributeValue,option = 0):
    if option ==2:
        conditionalSelect(conditionAttribute,attributeValue, 0)
        conditionalSelect(conditionAttribute,attributeValue, 1)
    else:
        conditionalSelect(conditionAttribute,attributeValue, option)

def conditionalSelect(conditionAttribute,attributeValue,option = 0):
    import glob
    if option == 0:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'
    else:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/o/nexussensors*.db'
    for dbFilename in\
    glob.glob(dire):
        dbSeqenceNum = filter(str.isdigit,dbFilename)
        print dbSeqenceNum + "-"*20
        dbSeqenceNum = int(dbSeqenceNum)
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()

        sql_sel = "select * from sensorspackage "
        sql_where = 'where '

        sql_act = sqlAct(dbSeqenceNum)

        sql_condition = conditionAttribute +' = '+ "'%s'"%attributeValue
        sqlF = sql_sel+sql_where+sql_condition
        cu.execute(sqlF)
        #print sqlF
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        for line in res:
            for f in line:
                print f,
            print
        #print '-'*60

        pass



def updateActionO(targActiList,option = 0):
    if option ==2:
        updateAction(targActiList,0)
        updateAction(targActiList,1)
    else:
        updateAction(targActiList,option)

def updateAction(targAct,option = 0):
    import glob
    if option == 0:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'
    else:
        dire = 'c:/Users/Phil/workspace/NexusSensors/DbRecords/o/nexussensors*.db'
    for dbFilename in\
    glob.glob(dire):
        dbSeqenceNum = filter(str.isdigit,dbFilename)
        print dbSeqenceNum + "-"*20
        dbSeqenceNum = int(dbSeqenceNum)
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()

        sql_update = "update sensorspackage set "
        sql_and = " and "
        sql_colon = ","

        sql_where = 'where '

        sql_act = sqlAct(dbSeqenceNum)

        sql_set = "mBooleanStepDetecor = '1.0' "
        sql_action = sql_act + " = '%s'"%targAct

        sql_condition = "mBooleanStepDetecor = '0.0'"

        sqlF = sql_update+sql_set+sql_where+sql_action + sql_and +sql_condition
        cu.execute(sqlF)
        #print sqlF
        res = cu.fetchall()
        # print 'row:', cu.rowcount
        for line in res:
            for f in line:
                print f,
            print
        #print '-'*60

        pass


def updateP4(lowerBound,upperBound, acti):
    import glob
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
    #glob.glob(r'nexussensors*.db'):
        sequenceNum = filter(str.isdigit,dbFilename)
        print sequenceNum + "-"*20
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql_update = "update sensorspackage set "
        sql_and = " and "
        sql_colon = ","
        orieAngle = testRandom(lowerBound,upperBound)
        sql_mOrientAngle = "mOrientationSensor = '%s'"%orieAngle
        orie = ranAngleOri(orieAngle)
        sql_mOrie = "mOrientation = '%s'"%orie
        sql_where = " where "
        sql_action = "action = '%s'"%acti
        sql_activity = "activity ='%s'"%acti
        sqlF = sql_update + sql_mOrientAngle + sql_colon + sql_mOrie + \
        sql_where
        sequenceNum = int(sequenceNum)
        if sequenceNum <= 13:
            sql_act = sql_activity
        else:
            sql_act = sql_action

        sqlF = sqlF + sql_act

        sql_mOrieNot = " (mOrientationSensor<%d or mOrientationSensor >= %d )"%(lowerBound,upperBound)

        sql_mOrieCondition = sql_mOrieNot

        sqlF = sqlF + sql_and + sql_mOrieCondition
        print sqlF

        cu.execute(sqlF)

        #print '-'*60
        pass


def updateP5(acti):
    import glob
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
    #glob.glob(r'nexussensors*.db'):
        sequenceNum = filter(str.isdigit,dbFilename)
        print sequenceNum + "-"*20
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql_update = "update sensorspackage set "
        sql_and = " and "
        sql_colon = ","

        lowerBound1 = 110
        upperBound1 = 180
        lowerBound2 = -180
        upperBound2 = -111
        orieAngle = testRandom(lowerBound2,upperBound2)

        sql_mOrientAngle = "mOrientationSensor = '%s'"%orieAngle
        orie = ranAngleOri(orieAngle)
        sql_mOrie = "mOrientation = '%s'"%orie
        sql_where = " where "
        sql_action = "action = '%s'"%acti
        sql_activity = "activity ='%s'"%acti
        sqlF = sql_update + sql_mOrientAngle + sql_colon + sql_mOrie + \
        sql_where
        sequenceNum = int(sequenceNum)
        if sequenceNum <= 13:
            sql_act = sql_activity
        else:
            sql_act = sql_action

        sqlF = sqlF + sql_act

        sql_mOrieNot = "( (mOrientationSensor<%d and mOrientationSensor>=0) or (mOrientationSensor>%d and mOrientationSensor <0  ))"%(lowerBound1,upperBound2)

        sql_mOrieCondition = sql_mOrieNot

        sqlF = sqlF + sql_and + sql_mOrieCondition
        print sqlF

        cu.execute(sqlF)

        '''
        '''
        #print '-'*60
        pass

def updateP3(lowerBound,upperBound, acti, currentValue, option):
    import glob
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
    #glob.glob(r'nexussensors*.db'):
        sequenceNum = filter(str.isdigit,dbFilename)
        print sequenceNum + "-"*20
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql_update = "update sensorspackage set "
        sql_and = " and "
        sql_colon = ","
        orieAngle = testRandom(lowerBound,upperBound)
        sql_mOrientAngle = "mOrientationSensor = '%s'"%orieAngle
        orie = ranAngleOri(orieAngle)
        sql_mOrie = "mOrientation = '%s'"%orie
        sql_where = " where "
        sql_action = "action = '%s'"%acti
        sql_activity = "activity ='%s'"%acti
        sqlF = sql_update + sql_mOrientAngle + sql_colon + sql_mOrie + \
        sql_where
        sequenceNum = int(sequenceNum)
        if sequenceNum <= 13:
            sql_act = sql_activity
        else:
            sql_act = sql_action

        sqlF = sqlF + sql_act

        sql_mOrieNot = "mOrientation != '%s'"%currentValue
        #sql_mOrieYes = "mOrientation = '%s'"%currentValue

        sql_mOrieYes = "mOrientationSensor = %d"%currentValue

        if option == 'Not':
            sql_mOrieCondition = sql_mOrieNot
        else:
            sql_mOrieCondition = sql_mOrieYes

        sqlF = sqlF + sql_and + sql_mOrieCondition
        print sqlF

        cu.execute(sqlF)

        '''
        '''
        #print '-'*60
        pass


def updateP2(orieAngle, orie, acti, currentValue, option):
    import glob
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
    #glob.glob(r'nexussensors*.db'):
        sequenceNum = filter(str.isdigit,dbFilename)
        print sequenceNum + "-"*20
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql_update = "update sensorspackage set "
        sql_and = " and "
        sql_colon = ","
        sql_mOrientAngle = "mOrientationSensor = '%s'"%orieAngle
        sql_mOrie = "mOrientation = '%s'"%orie
        sql_where = " where "
        sql_action = "action = '%s'"%acti
        sql_activity = "activity ='%s'"%acti
        sqlF = sql_update + sql_mOrientAngle + sql_colon + sql_mOrie + \
        sql_where
        sequenceNum = int(sequenceNum)
        if sequenceNum <= 13:
            sql_act = sql_activity
        else:
            sql_act = sql_action

        sqlF = sqlF + sql_act

        sql_mOrieNot = "mOrientation != '%s'"%currentValue
        #sql_mOrieYes = "mOrientation = '%s'"%currentValue

        sql_mOrieYes = "mOrientationSensor = %d"%currentValue

        if option == 'Not':
            sql_mOrieCondition = sql_mOrieNot
        else:
            sql_mOrieCondition = sql_mOrieYes

        sqlF = sqlF + sql_and + sql_mOrieCondition
        print sqlF

        cu.execute(sqlF)

        '''
        '''
        #print '-'*60
        pass

def updateP1(actiO, actiU):
    import glob
    for dbFilename in\
    glob.glob(r'c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors*.db'):
    #glob.glob(r'nexussensors*.db'):
        sequenceNum = filter(str.isdigit,dbFilename)
        sequenceNum = int(sequenceNum)
        conn = sqlite3.connect(dbFilename)
        conn.isolation_level = None
        cu = conn.cursor()
        sql_update = "update sensorspackage set "
        sql_where = " where "

        sql_actionO = "action = '%s'"%actiO
        sql_activityO = "activity ='%s'"%actiO
        sql_actionU = "action = '%s'"%actiU
        sql_activityU = "activity ='%s'"%actiU

        if sequenceNum <= 13:
            sql_actO = sql_activityO
            sql_actU = sql_activityU
        else:
            sql_actO = sql_actionO
            sql_actU = sql_actionU

        sqlF = sql_update + sql_actU + sql_where + sql_actO
        print sqlF
        cu.execute(sqlF)

def test1():
    orieAngle = '86'
    orie = 'E'
    acti = 'Cooking'
    currentValue = 'E'
    #option = 'Not'
    option = 'Yes'
    updateP(orieAngle,orie,acti,currentValue,option)

def Constants():
    oriSet1 = ['NW','N','NE']
    oriSet2 = ['SW','S','SE']
    oriSet3 = ['NE','E','SE']
    oriSet4 = ['NW','W','SW']
    oriAngle1 = [-20,19] #N
    oriAngle2 = [20,69] #NE
    oriAngle3 = [70,109] #E
    oriAngle4 = [110,159] #SE
    oriAngle5_1 = [160,180] #S
    oriAngle5_2 = [-180,-161] #S
    oriAngle6 = [-160,-111] #SW
    oriAngle7 = [-110,-71] #W
    oriAngle8 = [-70,-21] #NW

def testRandom(lowerBound,upperBound):
    import random
    return random.randint(lowerBound, upperBound)

def ranAngleOri(orieAngle):
    #orieAngle = testRandom(lowerBound,upperBound)
    if orieAngle < 160 and orieAngle >= 110:
        orie = 'SE'
    elif orieAngle >= 160 and orieAngle < 180:
        orie = 'S'
    elif orieAngle >= -180 and orieAngle < -160:
        orie = 'S'
    elif orieAngle >= -160 and orieAngle <-110:
        orie = 'SW'
    elif orieAngle >= -110 and orieAngle <-70:
        orie = 'W'
    elif orieAngle >= -70 and orieAngle <-20:
        orie = 'NW'
    elif orieAngle >= -20 and orieAngle <20:
        orie = 'N'
    elif orieAngle >= 20 and orieAngle <70:
        orie = 'NE'
    elif orieAngle >= 70 and orieAngle <110:
        orie = 'E'
    else:
        orie = 'None'
    return orie

def test2():
    lowerBound = 20
    upperBound = 160
    acti='Working on PC at home'
    currentValueSet = ['S','N','SW','W','NW']
    for currentValue in currentValueSet:
        orieAngle = testRandom(lowerBound,upperBound)
        orie = ranAngleOri(orieAngle)
        updateP(orieAngle,orie,acti,currentValue,'Yes')

def test3():
    lowerBound = -160
    upperBound = -21
    currentValue = -144
    acti='Cooking chopping'
    updateP3(lowerBound,upperBound,acti,currentValue,'Yes')

def test4(): #update orientation
    actiDict = {'Cooking chopping':-160,\
                'Bathroom':-160,\
                'Breakfast':-70,
                'Lunch':-70,
                'Dinner':-70,
                'Eating':-70,
                'Midnight snack':-70,
                'Washing dishes':-160,
                'Washing in bathroom':-160,
                'Working on PC at home':20,
                'Cooking': 110
                }
    for acti in actiDict:
        if acti != 'Cooking':
            lowerBound = actiDict[acti]
            upperBound = lowerBound+140-1
            if upperBound > 180:
                upperBound = 180
            updateP4(lowerBound,upperBound,acti)
        elif acti == 'Cooking':
            updateP5(acti)

def test5():
    #updateActionO('Walking at home',2)
    #updateActionO('Walking outside',2)
    updateActionO('Walking indoor',2)
    singleActionO('Walk',2)

def test6():
    pass

if __name__=="__main__":
    #sequenceNum = 1
    #indoorAction()
    #orieAngle = random()
    #updateP1('Working on PC in home','Working on PC at home')
    #test1()
    #testRandom()
    #test4()
    #allAction()
    #select()
    #actList = ['Dinner','Midnight snack']
    #actList = ['Midnight snack']
    #actList = ['Midnight']
    #actList = ['Dinner']
    #multipleActions(actList,0)
    conditionalSelectO('mBooleanStepDetecor',1.0,0)

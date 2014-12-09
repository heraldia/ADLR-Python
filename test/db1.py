import sqlite3

sequenceNum = 17
action = "Working on PC"
db1_1 = "c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors"
db1_2 = "%s"%sequenceNum
db1_3 = ".db"
db1 = db1_1 + db1_2 + db1_3
conn = sqlite3.connect(db1)
conn.isolation_level = None
cu = conn.cursor()
#cu.execute("select * from sensorspackage where id < 10")

sql1 = "select * from sensorspackage"
sql2 = " where action like '%s'" % action
#sql2 = " where action like \"%s\"" % action
#sql2 = " where action NOT NULL"
#sql2 = " where activity like '%s'" % action
#sqlF = sql1
sqlF = sql1 + sql2
#sqlF1 = "select distinct action from sensorspackage"
#sqlF1 = "select distinct action from wifirssi"
sqlF1 = "select id from wifirssi where action= 'laundry' "
#sqlF1 = "select id from sensorspackage where action like '%wrong%' "
cu.execute(sqlF1)
res = cu.fetchall()
# print 'row:', cu.rowcount
for line in res:
    for f in line:
        print f,
    print
print '-'*60

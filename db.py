# http://anony3721.blog.163.com/blog/static/5119742010716104442536/
import sqlite3

conn = sqlite3.connect("c:/Users/Phil/workspace/NexusSensors/DbRecords/nexussensors8.db")
conn.isolation_level = None
cu = conn.cursor()
#cu.execute("select * from sensorspackage where id < 10")

action = 'Working on PC at home'
sql = "select * from sensorspackage where activity like '%s'"
cu.execute(sql % action)
res = cu.fetchall()
print 'row:', cu.rowcount
for line in res:
    for f in line:
        print f,
    print
print '-'*60

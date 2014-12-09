
import re

f1=open('activityList1.txt','r').read()
f1 = re.sub('Cooking chopping','Chopping',f1)
f_w=open('activityList.txt','wb')
f_w.write(f1)
f_w.close()
